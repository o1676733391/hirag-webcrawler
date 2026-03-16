import requests
import certifi
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urldefrag
from pathlib import Path
from collections import defaultdict
import re


def is_english_url(full_url, domain):
    parsed = urlparse(full_url)

    if parsed.scheme not in ('http', 'https'):
        return False
    if parsed.netloc != domain:
        return False

    path = parsed.path.lower().strip('/')
    if not path:
        return True

    first_segment = path.split('/')[0]

    # Nếu URL có prefix ngôn ngữ thì chỉ giữ English
    locale_pattern = r'^[a-z]{2}(?:-[a-z]{2})?$'
    if re.match(locale_pattern, first_segment):
        return first_segment in {'en', 'en-us', 'en-gb'}

    # Chặn một số slug ngôn ngữ phổ biến không phải English
    non_english_prefixes = {
        'vi', 'zh', 'zh-cn', 'zh-hans', 'zh-hant', 'ja', 'ko', 'fr', 'de', 'es', 'it',
        'pt', 'pt-br', 'ru', 'th', 'id', 'tr', 'pl', 'nl', 'ar'
    }
    if first_segment in non_english_prefixes:
        return False

    return True


def normalize_internal_page_url(current_url, href, domain):
    if not href or href.startswith('#') or href.startswith('mailto:') or href.startswith('javascript:'):
        return None

    joined_url = urljoin(current_url, href)
    clean_url, _ = urldefrag(joined_url)

    if not is_english_url(clean_url, domain):
        return None

    parsed = urlparse(clean_url)

    # Bỏ các đường dẫn bảo vệ email của Cloudflare và tài nguyên không phải HTML page
    if '/cdn-cgi/l/email-protection' in parsed.path.lower():
        return None

    blocked_ext = (
        '.pdf', '.zip', '.rar', '.7z',
        '.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg', '.ico',
        '.mp4', '.mp3', '.wav', '.avi', '.mov', '.mkv',
        '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx'
    )
    if parsed.path.lower().endswith(blocked_ext):
        return None

    return clean_url

def crawl_link_tree(url, max_depth=2):
    visited = set()
    tree = {}

    def get_links(current_url, depth):
        if depth > max_depth or current_url in visited:
            return
        
        visited.add(current_url)
        domain = urlparse(url).netloc
        
        try:
            response = requests.get(current_url, timeout=10, verify=certifi.where())
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            links = []

            for a_tag in soup.find_all('a', href=True):
                link = a_tag['href']
                full_url = normalize_internal_page_url(current_url, link, domain)
                if full_url:
                    links.append(full_url)
            
            # Lưu cấu trúc vào cây
            tree[current_url] = list(dict.fromkeys(links))

            # Đệ quy để đào sâu hơn
            for link in links:
                get_links(link, depth + 1)
        except Exception as e:
            print(f"Lỗi khi crawl {current_url}: {e}")

    get_links(url, 0)
    return tree


def extract_dropdown_categories(url):
    """Lấy nhóm link từ menu dropdown (ví dụ: Products, Resources, ...)."""
    categories = defaultdict(list)

    try:
        response = requests.get(url, timeout=10, verify=certifi.where())
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        domain = urlparse(url).netloc

        # Ưu tiên các khu vực menu điều hướng
        containers = soup.select('nav, header, .menu, .navbar, .navigation')
        if not containers:
            containers = [soup]

        for container in containers:
            for li_tag in container.select('li'):
                top_link = li_tag.find('a', href=True)
                if not top_link:
                    continue

                # Tìm link con trong dropdown/submenu
                child_links = li_tag.select('ul a[href], .dropdown-menu a[href], .sub-menu a[href]')
                if not child_links:
                    continue

                category_name = ' '.join(top_link.get_text(' ', strip=True).split())
                if not category_name:
                    continue

                for a_tag in child_links:
                    link = a_tag['href']
                    full_url = normalize_internal_page_url(url, link, domain)
                    if full_url:
                        categories[category_name].append(full_url)

        # Loại trùng, giữ thứ tự
        return {name: list(dict.fromkeys(links)) for name, links in categories.items() if links}
    except Exception as e:
        print(f"Lỗi khi lấy dropdown categories từ {url}: {e}")
        return {}


def categorize_links_by_keyword(link_tree):
    """Phân loại theo URL/path nếu không bắt được dropdown rõ ràng."""
    keyword_map = {
        'Products': ['product', 'products', 'solution', 'solutions'],
        'Resources': ['resource', 'resources', 'blog', 'news', 'webinar', 'whitepaper', 'case-study', 'docs'],
        'Support': ['support', 'help', 'service', 'faq', 'contact'],
        'Company': ['company', 'about', 'team', 'career', 'investor'],
    }

    categorized = defaultdict(list)
    all_links = []

    for parent, children in link_tree.items():
        all_links.append(parent)
        all_links.extend(children)

    all_links = list(dict.fromkeys(all_links))

    for link in all_links:
        lower_link = link.lower()
        matched = False

        for category, keywords in keyword_map.items():
            if any(keyword in lower_link for keyword in keywords):
                categorized[category].append(link)
                matched = True

        if not matched:
            categorized['Other'].append(link)

    return {name: list(dict.fromkeys(links)) for name, links in categorized.items() if links}


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9]+', '_', text)
    return text.strip('_') or 'category'


def export_link_tree_to_txt(link_tree, output_file):
    lines = ["=== LINK TREE ===", ""]
    for parent, children in link_tree.items():
        lines.append(f"[Parent] {parent}")
        for child in children:
            lines.append(f"  - {child}")
        lines.append("")

    Path(output_file).write_text('\n'.join(lines), encoding='utf-8')


def export_categories_to_txt(categories, output_dir):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    summary_lines = ["=== CATEGORIES ===", ""]
    for category, links in categories.items():
        summary_lines.append(f"[{category}] ({len(links)} links)")
        for link in links:
            summary_lines.append(f"  - {link}")
        summary_lines.append("")

        file_name = f"category_{slugify(category)}.txt"
        (output_path / file_name).write_text(
            '\n'.join([f"=== {category} ===", ""] + [f"- {link}" for link in links]),
            encoding='utf-8'
        )

    (output_path / 'categories_summary.txt').write_text('\n'.join(summary_lines), encoding='utf-8')

# Thử nghiệm với một website (Hãy thay bằng URL bạn muốn)
target_url = "https://www.arbin.com/"
link_structure = crawl_link_tree(target_url, max_depth=1)
dropdown_categories = extract_dropdown_categories(target_url)

# Nếu không lấy được dropdown rõ ràng thì fallback sang phân loại theo keyword URL
category_structure = dropdown_categories if dropdown_categories else categorize_links_by_keyword(link_structure)

export_link_tree_to_txt(link_structure, 'link_tree.txt')
export_categories_to_txt(category_structure, 'categories_export')

for parent, children in link_structure.items():
    print(f"\n[Parent]: {parent}")
    for child in children[:5]: # Chỉ in 5 link con đầu tiên để ví dụ
        print(f"  └── [Child]: {child}")

print("\nĐã export:")
print("- link_tree.txt")
print("- categories_export/categories_summary.txt")
print("- categories_export/category_<ten_category>.txt")
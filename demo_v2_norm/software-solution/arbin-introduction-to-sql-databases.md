# Metadata

| Field | Value1 |
|------|------|
| Title | Arbin Introduction to SQL Databases |
| Page Type | Software |
| Source URL | https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html |
| Category | Database Management |
| Last Updated | 2024-11 |

# Overview

An SQL database is a type of relational database that uses Structured Query Language (SQL) to manage and manipulate data. It stores information in tables, which are organized into rows and columns. Each table can be linked to other tables through relationships defined by keys, ensuring data integrity and enabling complex queries. SQL databases support operations such as creating, reading, updating, and deleting data (often abbreviated as CRUD). They also provide tools for querying data, ensuring consistency, and enforcing rules through constraints. Arbin supports SQL databases including PostgreSQL and Microsoft SQL Server. They are widely used in applications ranging from small projects to large-scale enterprise systems due to their robustness, scalability, and flexibility. Arbin has migrated in-file datastore to SQL database and streaming datastore to support the need for complex system integration and cloud-focused applications.

# Key Features

| Feature | Description |
|---------|-------------|
| Structured Data Storage | Data is stored in a structured format using tables, which makes it easy to organize, manage, and query. |
| Data Integrity and Accuracy | SQL databases support ACID (Atomicity, Consistency, Isolation, Durability) properties, ensuring reliable transactions and maintaining data accuracy even in the case of system failures or crashes. |
| Powerful Query Language | The use of SQL allows for complex queries to retrieve, update, and manipulate data efficiently. SQL is a standardized language, making it easier to transfer skills between different SQL database systems. |
| Data Relationships | SQL databases use foreign keys to establish relationships between tables, enabling complex data models and ensuring data consistency across related tables. |
| Data Security | SQL databases offer robust security features, including user authentication and authorization, to control access to sensitive data. |
| Scalability | SQL databases can handle large volumes of data and complex queries, and many systems offer horizontal and vertical scaling options to manage increased load. |
| Transaction Management | SQL databases handle multiple operations as a single transaction, allowing for operations to be completed in a consistent manner or rolled back if an error occurs. |
| Data Integrity Constraints | SQL databases allow the definition of constraints such as primary keys, foreign keys, and unique constraints to enforce rules at the data level and maintain data quality. |
| Backup and Recovery | Most SQL databases offer built-in backup and recovery solutions, helping to protect data against loss and corruption. |
| Mature Ecosystem | SQL databases benefit from a mature ecosystem with numerous tools for development, management, and optimization, as well as strong community and vendor support. |
| Standardization | SQL is a standardized language, which means that skills and queries are generally transferable between different SQL database systems, such as MySQL, PostgreSQL, and SQL Server. |

# Centralized Datastore System (CDS)

In our CDS service, we support customers using remote SQL databases, cloud SQL databases, and streaming data solutions to solve complex data management requirements.

# On-Premise Database Server Setup

All servers are under company or enterprise control with private Network (LAN) to maximize data security and privacy. Your data is not transferred outside of the company network and your IP secrets will not depend on the cloud or data center service. There is a big ongoing debate about where to keep your data; private server room or cloud service is better security. We are providing on-premises options to meet your company requirements.

## Local Master Database Server and Remote Replicate Database Server

| Advantage | Description |
|-----------|-------------|
| Write/Read | Master Database Server is higher data persistency. |
| Performance | Higher performance and synchronization between Master and Replicate Servers. |
| Data Analysis | High Speed data analysis, query, and export from replicate Server without impact on current Master Database Performance. |
| Backup Management | Easily manage Backup and restore databases. |

| Disadvantage | Description |
|--------------|-------------|
| Centralization | Cannot centralize Local Servers to one single-large database server. |
| Network Requirement | Requiring high speed network to ensure synchronization bandwidth between Master and Replicate Server. |

## Local Database Server & Remote Centralized Database Server

| Advantage | Description |
|-----------|-------------|
| Write/Read | Local and Remote are independent from each other. |
| Global Database | Forming a global database server for all test databases. |
| Data Persistence | Greater data persistence in Local Database without disruption. |
| Performance | High performance in data analysis in Remote Database Server. |

| Disadvantage | Description |
|--------------|-------------|
| Maintenance | Difficult to maintain data synchronization between Local and Remote Database. |
| Performance | Lower performance if checking data consistency between Local and Remote Server. |

# Hybrid-Cloud Database Server Setup

All the remote databases will be hosted in AWS, GCP, Azure, and other Hosting Servers at datacenter to keep your data backup remotely. This option allows you to keep a copy of your data on cloud servers, but not only cloud database services.

| Advantage | Description |
|-----------|-------------|
| Backup Policy | Having a remote backup policy to prevent disastrous incidents at local office will lose all valuable tests data. |
| Data Sharing | Sharing data with remote teams. |

| Disadvantage | Description |
|--------------|-------------|
| Network Latency | Due to network latency between office to cloud service provider, there is a potential risk of data inconsistency between local and off-site servers. |
| Synchronization | Difficulty managing data synchronization between Local and Remote. |

# On-Cloud Database Service Setup

Using RDS (Relational Database Service) on cloud reduces cost and management compared to your own hosting environment. However, there is no replication feature between Local Database and RDS.

# Data Logging Performance

A comparative analysis between PostgreSQL and Microsoft SQL Server (MSSQL) was conducted across different query complexities and data volumes. While both databases demonstrated similar performance for smaller datasets, PostgreSQL shows better performance with increasing data volume.

| Database | Access (pps) | MSSQL (pps) | PostgreSQL (pps) | Kafka (pps) |
|----------|--------------|-------------|------------------|-------------|
| Insertion Rate | 2000 | 80,000 | 100,000 | unlimited |
| Query Rate | 2000 | 200,000 | 333,000 | OnDemand |

*All units in pps (points per second). Arbin data point takes 10 bytes in size, which contains two floats (1 byte per float number) and two unsigned char (4 bytes per char) which adds up to 10 bytes.*

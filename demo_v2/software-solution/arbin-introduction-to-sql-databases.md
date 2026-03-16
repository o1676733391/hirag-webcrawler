# Source

- URL: https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html

# Content

#  Arbin Introduction to  
SQL Databases
![ARBIN-AAF-Arbin-Introduction-to-SQL-Databases](https://www.arbin.com/wp-content/uploads/2024/11/ARBIN-AAF-Arbin-Introduction-to-SQL-Databases.png)
Table of Contents

**An SQL database** is a type of relational database that uses Structured Query Language (SQL) to manage and manipulate data. It stores information in tables, which are organized into rows and columns. Each table can be linked to other tables through relationships defined by keys, ensuring data integrity and enabling complex queries.
SQL databases support operations such as creating, reading, updating, and deleting data (often abbreviated as CRUD). They also provide tools for querying data, ensuring consistency, and enforcing rules through constraints.
Arbin supports SQL databases including PostgreSQL, and Microsoft SQL Server. They are widely used in applications ranging from small projects to large-scale enterprise systems due to their robustness, scalability, and flexibility.
Arbin has been migrated in-file datastore to SQL database and streaming datastore to support the need of complex system integration and cloud focus applications.
##  Arbin Datastore Overview
![ARBIN-Many schedules can reference to one or multiple sub-schedules and default global setting from running schedule and allow to overwrite in sub-schedules](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-Many-schedules-can-reference-to-one-or-multiple-sub-schedules-and-default-global-setting-from-running-schedule-and-allow-to-overwrite-in-sub-schedules.png)
In the local database, we support the coexistence and backup of multiple databases, including MSSQL, PostgreSQL, and MS-ACCESS. Data is backed up using the Master-Slave method. Additionally, we employ local caching technology to prevent data loss caused by failures to store data points in the database.
For remote databases, we support MSSQL and PostgreSQL. Similarly, we use the Master-Slave method to achieve data backup. Additionally, we have a dedicated local cache for remote databases to buffer data that fails to be stored due to network latency or the unavailability of the remote database.
In the local database, we support the coexistence and backup of multiple databases, including MSSQL, PostgreSQL, and MS-ACCESS. Data is backed up using the Master-Slave method. Additionally, we employ local caching technology to prevent data loss caused by failures to store data points in the database.
##  Advantages
### [Structured Data Storage](https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html)
Data is stored in a structured format using tables, which makes it easy to organize, manage, and query.
### [Data Integrity and Accuracy](https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html)
SQL databases support ACID (Atomicity, Consistency, Isolation, Durability) properties, ensuring reliable transactions and maintaining data accuracy even in the case of system failures or crashes.
### [Powerful Query Language](https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html)
The use of SQL allows for complex queries to retrieve, update, and manipulate data efficiently. SQL is a standardized language, making it easier to transfer skills between different SQL database systems.
### [Data Relationships](https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html)
SQL databases use foreign keys to establish relationships between tables, enabling complex data models and ensuring data consistency across related tables.
### [Data Security](https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html)
SQL databases offer robust security features, including user authentication and authorization, to control access to sensitive data.
### [Scalability](https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html)
SQL databases can handle large volumes of data and complex queries, and many systems offer horizontal and vertical scaling options to manage increased load.
### [Transaction Management](https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html)
SQL databases handle multiple operations as a single transaction, allowing for operations to be completed in a consistent manner or rolled back if an error occurs.
### [Data Integrity Constraints](https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html)
SQL databases allow the definition of constraints such as primary keys, foreign keys, and unique constraints to enforce rules at the data level and maintain data quality.
### [Backup and Recovery](https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html)
Most SQL databases offer built-in backup and recovery solutions, helping to protect data against loss and corruption.
### [Mature Ecosystem](https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html)
SQL databases benefit from a mature ecosystem with numerous tools for development, management, and optimization, as well as strong community and vendor support.
### [Standardization](https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html)
SQL is a standardized language, which means that skills and queries are generally transferable between different SQL database systems, such as MySQL, PostgreSQL, and SQL Server.
##  Centralized Datastore System (CDS)
[ ](https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html)
In our CDS service, we support customers using remote SQL databases, cloud SQL databases, and streaming data solutions to solve complex data management requirements.
![ARBIN-Centralized Datastore System \(CDS\)](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-Centralized-Datastore-System-CDS.png)
##  On-Premise database server setup
[ ](https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html)
All servers are under company or enterprise control with private Network (LAN) to maximize data security and privacy.
[ ](https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html)
Your data is not transferred outside of the company network and your IP secrets will not depend on the cloud or data center service.
[ ](https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html)
There is a big on-going debate about where to keep your data private server room or cloud service is better security.
[ ](https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html)
We are providing on-premises option to meet your company requirements.
### [Local Master Database Server and Remote Replicate Database Server.](https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html)
![ARBIN-Local Master Database Server and Remote Replicate Database Server](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-Local-Master-Database-Server-and-Remote-Replicate-Database-Server.png)
### [Advantages](https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html)
  * 1 Write/Read (Master Database Server is higher data persistency.
  * Higher performance and synchronization between Master and Replicate Servers
  * High Speed data analysis, query, and export from replicate Server without impact on current Master Database Performance.
  * Easily manage Backup and restore databases.

### [Disadvantage](https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html)
  * Cannot centralized Local Servers to one single-large database server.
  * Requiring high speed network to ensure synchronization bandwidth between Master and Replicate Server.

### [Local Database Server & Remote Centralized Database Server.](https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html)
![ARBIN-AAF-Local Database Server & Remote Centralized Database Server](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-AAF-Local-Database-Server-Remote-Centralized-Database-Server.png)
### [Advantages](https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html)
  * 2-Write/Read (Local and Remote) are independent from each other's.
  * Forming a global database server for all test databases.
  * Greater data persistence in Local Database without disruption.
  * High performance in data analysis in Remote Database Server.

### [Disadvantage](https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html)
  * Difficult to maintenance data synchronization between Local and Remote Database.
  * Lower performance if checking data consistency between Local and Remote Server.

##  Hybrid-Cloud database server setup
[ ](https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html)
All the remote databases will be hosted in AWS, GCP, Azure, and others Hosting Servers at datacenter to keep your data backup remotely.
[ ](https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html)
This option allows you to keep a copy of your data on cloud servers, but not only cloud database services.
![ARBIN-AAF-Hybrid-Cloud database server setup](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-AAF-Hybrid-Cloud-database-server-setup.png)
### [Advantages](https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html)
  * Having a remote backup policy to prevent disastrous incidents at local office will lose all valuable tests data.
  * Sharing data with remote teams.

### [Disadvantage](https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html)
  * Due to network latency between office to cloud service provider, there is a potential risk of data inconsistency between local and off-side servers.
  * Difficulty managing data synchronization between Local and Remote.

##  On-Cloud database service setup
Using RDS (Relational Database Service) on cloud reduces cost and management compared to your own hosting environment. However, there is no replication feature between Loca Database and RDS.
![ARBIN-AAF-On-Cloud database service setup](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-AAF-On-Cloud-database-service-setup.png)
##  Data Logging Performance
[ ](https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html)
A comparative analysis between PostgreSQL and Microsoft SQL Server (MSSQL) was conducted across different query complexities and data volumes.
[ ](https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html)
While both databases demonstrated similar performance for smaller datasets, PostgreSQL is clearly better performance with increasing data volume.
Insertion/Query Rate Comparison
Database
Access (pps)
MSSQL (pps)
PostgreSQL (pps)
Kafka (pps)
Insertion Rate
2000
80,000
100,000
unlimited
Query Rate
2000
200,000
333,000
OnDemand
*All units in pps (point per second)  
Arbin data point takes 10 bytes in size, which contains two floats (1byte per float number) and two unsigned char (4 byte per char) which adds up to 10 bytes.

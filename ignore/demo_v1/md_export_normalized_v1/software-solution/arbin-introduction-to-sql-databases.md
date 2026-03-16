# Metadata

| Field        | Value                                               |
| ------------ | --------------------------------------------------- |
| Title        | Arbin Introduction to SQL Databases                 |
| Page Type    | Article                                            |
| Source URL   | https://www.arbin.com/software-solution/arbin-introduction-to-sql-databases.html |
| Category     | Software                                           |
| Last Updated |                                                     |

# Overview

An SQL database is a type of relational database that uses Structured Query Language (SQL) to manage and manipulate data. It stores information in tables, which are organized into rows and columns. Each table can be linked to other tables through relationships defined by keys, ensuring data integrity and enabling complex queries. SQL databases support operations such as creating, reading, updating, and deleting data (often abbreviated as CRUD). They also provide tools for querying data, ensuring consistency, and enforcing rules through constraints. Arbin supports SQL databases including PostgreSQL and Microsoft SQL Server.

# Key Features

| Feature | Description |
|---------|-------------|
| Structured data storage | Data is stored in a structured format using tables, which makes it easy to organize, manage, and query. |
| Data integrity and accuracy | SQL databases support ACID (Atomicity, Consistency, Isolation, Durability) properties, ensuring reliable transactions and maintaining data accuracy even in the case of system failures or crashes. |
| Powerful query language | The use of SQL allows for complex queries to retrieve, update, and manipulate data efficiently. SQL is a standardized language, making it easier to transfer skills between different SQL database systems. |
| Data relationships | SQL databases use foreign keys to establish relationships between tables, enabling complex data models and ensuring data consistency across related tables. |
| Data security | SQL databases offer robust security features, including user authentication and authorization, to control access to sensitive data. |
| Scalability | SQL databases can handle large volumes of data and complex queries, and many systems offer horizontal and vertical scaling options to manage increased load. |
| Transaction management | SQL databases handle multiple operations as a single transaction, allowing for operations to be completed in a consistent manner or rolled back if an error occurs. |
| Data integrity constraints | SQL databases allow the definition of constraints such as primary keys, foreign keys, and unique constraints to enforce rules at the data level and maintain data quality. |
| Backup and recovery | Most SQL databases offer built-in backup and recovery solutions, helping to protect data against loss and corruption. |
| Mature ecosystem | SQL databases benefit from a mature ecosystem with numerous tools for development, management, and optimization, as well as strong community and vendor support. |
| Standardization | SQL is a standardized language, which means that skills and queries are generally transferable between different SQL database systems, such as MySQL, PostgreSQL, and SQL Server. |

# Technical Specifications

## Electrical Specifications

| Parameter | Value | Unit | Notes |

## Hardware Specifications

| Parameter | Value | Unit | Notes |

## Measurement Specifications

| Parameter | Value | Unit | Notes |

## Environmental / Temperature

| Parameter | Value | Unit | Notes |

## General Specifications

| Parameter | Value | Unit | Notes |

# Test Techniques / Control Modes

| Technique | Description | Key Parameters |
|-----------|-------------|----------------|

# Software Integration

| Software | Description | Capability |
|----------|-------------|------------|

# System Architecture / Infrastructure

| Component | Description |
|-----------|-------------|
| Centralized datastore system (CDS) | Supports customers using remote SQL databases, cloud SQL databases, and streaming data solutions to solve complex data management requirements. |
| On-premise database server setup | All servers are under company or enterprise control with private Network (LAN) to maximize data security and privacy. |
| Hybrid-cloud database server setup | All the remote databases will be hosted in AWS, GCP, Azure, and others Hosting Servers at datacenter to keep your data backup remotely. |
| On-cloud database service setup | Using RDS (Relational Database Service) on cloud reduces cost and management compared to your own hosting environment. |

# Accessories / Optional Modules

| Module | Description | Link |

# Related Products / Systems

| Product | Description | Link |

# Notes

* Arbin has migrated in-file datastore to SQL database and streaming datastore to support the need of complex system integration and cloud focus applications.
* Data is backed up using the Master-Slave method.
* Local caching technology is employed to prevent data loss caused by failures to store data points in the database.
* Arbin data point takes 10 bytes in size, which contains two floats (1 byte per float number) and two unsigned char (4 bytes per char) which adds up to 10 bytes.
* All units in pps (points per second).

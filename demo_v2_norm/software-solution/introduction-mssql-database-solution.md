# Metadata

| Field | Value1 |
|------|------|
| Title | Introduction MSSQL Database Solution |
| Page Type | Software |
| Source URL | https://www.arbin.com/software-solution/introduction-mssql-database-solution.html |
| Category | Database Solutions |
| Last Updated | 2024-09 |

# Overview

Arbin integrated Microsoft SQL Server, a powerful RDBMS, is designed for managing, analyzing, and securing data. It supports a wide range of functionalities and is used across various industries and applications. Since Arbin MITS adopted SQL Server into Data Acquisition, it has provided a flexible way to query and manage testing data effectively.

# Key Features

| Feature | Description |
|---------|-------------|
| Relational Database Management | MSSQL Server organizes data into tables with rows and columns. It supports the relational model, allowing data to be related and queried efficiently. |
| SQL Language | Uses Transact-SQL (T-SQL), an extension of SQL (Structured Query Language) with additional features for procedural programming and error handling. |
| Data Types | Supports a wide range of data types including integer, decimal, varchar, date/time, and more. |
| Indexing | Supports various indexing methods, including clustered and non-clustered indexes, to optimize query performance. |
| Partitioning | Allows tables and indexes to be divided into smaller, more manageable pieces for improved performance. |
| In-Memory OLTP | Provides in-memory processing capabilities to enhance transaction processing and data access speeds. |
| Integration with Microsoft Products | Works seamlessly with other Microsoft products such as Azure, Office, and .NET. |
| Extensibility | Supports custom stored procedures, functions, and user-defined types. It also integrates with various development tools and third-party applications. |

# Technical Specifications

## General Specifications
| Parameter | Value1 |
|-----------|--------|
| Supported Databases | PostgreSQL, Microsoft SQL Server |

# Free Microsoft SQL Server Limitation

SQL Server Express is a lightweight, free edition suitable for small-scale applications, development, and learning. It's limited in features, scalability, and support.

## Database Size Limitation
| Parameter | Value1 |
|-----------|--------|
| Maximum Database Size | 10 GB |

## Resource Limits
| Parameter | Value1 |
|-----------|--------|
| RAM Limit | 1 GB |
| CPU Limit | 1 CPU |

## Community Support
| Parameter | Value1 |
|-----------|--------|
| Support Type | Community forums and online resources |

## Licensing
| Parameter | Value1 |
|-----------|--------|
| Licensing Fees | None |

## Limited Options
| Parameter | Value1 |
|-----------|--------|
| High-Availability Features | Not supported |

## Basic Security
| Parameter | Value1 |
|-----------|--------|
| Security Features | Standard authentication, authorization, and encryption |

## Basic Features
| Parameter | Value1 |
|-----------|--------|
| Core Database Functionality | Suitable for small-scale applications |

## Limited Advanced Features
| Parameter | Value1 |
|-----------|--------|
| Advanced Features | Lacks SSAS, SSRS, SSIS, and advanced data management tools |

## Performance
| Parameter | Value1 |
|-----------|--------|
| High-Availability Features | Not supported |

# Arbin MSSQL Express Edition Architecture Overview

Because Express Edition limits 10GB Storage, we have developed an internal distributed database storage to create multiple 10GB Databases. Even though we have managed to resolve all the performance and bottlenecks in data transactions, it is extremely difficult to manage large data sets or multiple years of data backup. Data backup, restore, and migration are extremely challenging and easily corrupt the datastore. We do not recommend this solution for big-data test-driven use cases.

# Standard & Enterprise Editions

## Comprehensive Features
| Parameter | Value1 |
|-----------|--------|
| SQL Server Features | Includes advanced data management, analytics, and integration services |

## Advanced Capabilities
| Parameter | Value1 |
|-----------|--------|
| High-Availability Features | Supports Always On Availability Groups |

## High Scalability
| Parameter | Value1 |
|-----------|--------|
| Resource Limitations | None |

## Commercial
| Parameter | Value1 |
|-----------|--------|
| Licensing | Requires a license, often based on cores or servers |

## No Size Limits
| Parameter | Value1 |
|-----------|--------|
| Database Size | Virtually unlimited |

## Resource Utilization
| Parameter | Value1 |
|-----------|--------|
| System Resources | Can utilize multiple CPUs and large amounts of RAM |

## Comprehensive Support
| Parameter | Value1 |
|-----------|--------|
| Support Type | Full support from Microsoft |

## Advanced Tools
| Parameter | Value1 |
|-----------|--------|
| Management Tools | Advanced management and monitoring tools for database maintenance |

# Arbin Recommendation for MSSQL Configuration

We recommend using the Local Test Station with MS SQL Express Edition and using a remote Database Server as the enterprise edition to save costs on data licenses and address the need to expand the datastore beyond 10GB. However, database administrators need to regularly purge old data on local database servers.

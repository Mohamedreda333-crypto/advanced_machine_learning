# Project Documentation 

##  Setup & Installation Guide

### Prerequisites
- **SQL Server 2019** or later version
- **AdventureWorksLT2022** sample database
- **TSQL** transaction database
- **SQL Server Management Studio (SSMS)** or Azure Data Studio

### Database Installation Steps

#### AdventureWorksLT2022
1. Download AdventureWorksLT2022 backup file from Microsoft
2. Open SSMS and connect to your SQL Server instance
3. Right-click on Databases → Restore Database
4. Select "Device" and browse to the backup file
5. Execute the restore operation

#### TSQL Database
1. Obtain the TSQL database backup file
2. Follow similar restoration process as above
3. Verify both databases are properly restored

### Execution Instructions
1. Open SQL Server Management Studio
2. Connect to your database instance
3. Open and execute `Project_1_AdventureWorkLT2022.sql`
4. Open and execute `Project_2_TSQL.sql`
5. Analyze query results in the Results pane

##  Database Schema Overview

### AdventureWorksLT2022 Schema
**Core Tables:**
- `SalesLT.Customer` - Customer demographic information
- `SalesLT.Product` - Product catalog and pricing
- `SalesLT.SalesOrderHeader` - Order master data
- `SalesLT.SalesOrderDetail` - Order line items
- `SalesLT.ProductCategory` - Product categorization
- `SalesLT.Address` - Customer and company addresses

**Key Relationships:**
- Customers → Orders (One-to-Many)
- Products → OrderDetails (One-to-Many)
- ProductCategories → Products (One-to-Many)

### TSQL Database Schema
**Core Tables:**
- `Sales.Customers` - Customer information
- `Production.Products` - Product inventory
- `Sales.Orders` - Order headers
- `Sales.OrderDetails` - Order line items
- `HR.Employees` - Employee records
- `Production.Suppliers` - Supplier information
- `Production.Categories` - Product categories
- `Sales.Shippers` - Shipping companies

**Key Relationships:**
- Complex multi-table relationships for complete order processing

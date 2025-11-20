/*
Project: AdventureWorksLT2022 SQL Analysis
Author: [Mohamed Reda Ramadan Khamis]
Date: [10/11/2025]
Description: Comprehensive SQL queries demonstrating database querying techniques
             and business analysis on AdventureWorksLT2022 database.
*/


USE AdventureWorksLT2022 
Go

-- All coloums from customer table
SELECT * FROM SalesLT.Customer; 

-- print 3 couloums (CustomerID, FirstName, Phone) from customer table 
SELECT CustomerID, FirstName, Phone FROM SalesLT.Customer;

-- All coloums from product table
SELECT * FROM SalesLT.Product; 

-- print 2 couloums(ListPrice , second coloum(ListPrice * 1.1))
SELECT ListPrice, ListPrice * 1.1 FROM SalesLT.Product; 

-- I can give a new coloums (name) ucing AS query
SELECT ListPrice, ListPrice * 1.1 as new_Price FROM SalesLT.Product;

-- if i need to name coloum --> new price --> Error 
-- it must use 'new price'
SELECT ListPrice, ListPrice * 1.1 as 'new Price' FROM SalesLT.Product;

-- print all frequently color(red, blue, black,red,blue,....)
SELECT Color FROM SalesLT.Product; 

-- print Unique color only(red, blue, black, White....)
SELECT DISTINCT Color FROM SalesLT.Product; 

SELECT DISTINCT Color, Size FROM SalesLT.Product; 

-- Sorted using ORDERED BY 
-- Ascending(from Small to Large)(Default)
SELECT ListPrice FROM SalesLT.Product ORDER BY ListPrice
SELECT DISTINCT ListPrice FROM SalesLT.Product ORDER BY ListPrice

-- Descending(from large to Small)
SELECT DISTINCT ListPrice FROM SalesLT.Product ORDER BY ListPrice DESC


-- Where Clause --> Filter
SELECT ListPrice FROM SalesLT.Product WHERE ListPrice < 1000 
SELECT Name,ListPrice FROM SalesLT.Product WHERE ListPrice < 1000 OR ListPrice > 5000 
SELECT Name,ListPrice FROM SalesLT.Product WHERE Color = 'red' and ListPrice < 1000 

-- Null
SELECT * FROM SalesLT.Product
SELECT Name,Size FROM SalesLT.Product WHERE Size is not NULL

-- Like predicate --> Check A character string for a pattern
SELECT * FROM SalesLT.Customer 
SELECT FirstName FROM SalesLT.Customer WHERE FirstName LIKE '%o'  -- last character --> 'o'
SELECT FirstName FROM SalesLT.Customer WHERE FirstName LIKE 'o%'  -- Start character --> 'o'
SELECT FirstName FROM SalesLT.Customer WHERE FirstName LIKE '%o%'  -- Contain character --> 'o'

---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
SELECT * FROM SalesLT.ProductCategory

-- select rows from SalesLT.ProductCategory without *
-- select 3 coloums(ProductCategoryID, ParentProductCategoryID , Name) from ProductCategory table
SELECT ProductCategoryID, ParentProductCategoryID , Name FROM SalesLT.ProductCategory

SELECT * FROM SalesLT.Product
-- select 4 coloums(ProductID, Name, ListPrice , and work new coloum-->New Price)
SELECT ProductID, Name, ListPrice,(ListPrice * 1.1) AS 'New Price' FROM SalesLT.Product

SELECT * FROM SalesLT.SalesOrderDetail
-- select 5 coloums (SalesOrderID, ProductID, UnitPrice, OrderQty , add new coloum and sorted Ascending by new coloum)
SELECT SalesOrderID, ProductID, UnitPrice, OrderQty, (UnitPrice * OrderQty) AS Sales 
FROM SalesLT.SalesOrderDetail ORDER BY Sales


SELECT * FROM SalesLT.Customer
-- Coloum Aliases
SELECT CustomerID AS CustomerNo, Title, FirstName, LastName AS Surename FROM SalesLT.Customer

-- Case Expression 
SELECT * FROM SalesLT.Product
SELECT ProductNumber, Name, ListPrice,
    Case Size 
        WHEN 'S' Then 'Small'
        WHEN 'L' Then 'Large'
        WHEN 'M' Then 'Medium'
        WHEN 'XL' Then 'Extra Large'
        ELSE Size
    END As Size
FROM SalesLT.Product


SELECT ProductNumber, ProductID,
    CASE ProductCategoryID 
        When 5 Then 'Mountain Bikes'
        When 6 Then 'Road Bikes'
        When 7 Then 'Touring Bikes'
        ELSE 'Bike Accessories'
    END AS ProductCategoryID
FROM SalesLT.Product

-- Return the first 10 rows
SELECT TOP (10) SalesOrderID, CustomerID, OrderDate FROM SalesLT.SalesOrderHeader
SELECT TOP (10) PERCENT SalesOrderID, CustomerID, OrderDate  FROM SalesLT.SalesOrderHeader ORDER BY OrderDate ASC

-- Handling Nulls
SELECT CustomerID, Title, FirstName,MiddleName , LastName 
FROM SalesLT.Customer
WHERE MiddleName <> N'A.'
ORDER BY MiddleName

SELECT CustomerID, Title, FirstName,MiddleName , LastName 
FROM SalesLT.Customer
WHERE MiddleName = N'A.' or MiddleName is Null
ORDER BY MiddleName

SELECT CustomerID, Title, FirstName,MiddleName , LastName 
FROM SalesLT.Customer
WHERE MiddleName is Null
ORDER BY MiddleName

SELECT CustomerID, Title, FirstName,LastName,
Case  
WHEN MiddleName is NULL THEN 'NA'
ELSE MiddleName
END AS MiddleName
FROM SalesLT.Customer
WHERE MiddleName <> N'A.'
ORDER BY MiddleName


-- Aggregation Function (SUM(), AVG(),COUNT(),MAX(),MIN(),.......)
-- Calculates the total sales amount by summing the TotalDue column
SELECT SUM(TotalDue) AS 'TOTAL SALES' FROM SalesLT.SalesOrderHeader

-- Returns the average list price of all products
SELECT AVG(ListPrice) AS 'Average Price' FROM SalesLT.Product

-- Counts the total number of customers
SELECT COUNT(CustomerID) AS 'Customer Count' FROM SalesLT.Customer

-- Calculates total sales for each customer by summing their TotalDue values
SELECT CustomerID, SUM(TotalDue) AS 'Total Sales of each Customer' 
FROM SalesLT.SalesOrderHeader 
GROUP BY CustomerID

-- Counts how many products exist in each product category
SELECT ProductCategoryID,COUNT(ProductID) AS 'Product Count'
FROM SalesLT.Product
GROUP BY ProductCategoryID


-- Summarizes each customer yearly sales by grouping totals per customer and order year
SELECT CustomerID, YEAR(OrderDate) AS 'Order Year', SUM(TotalDue) AS 'Total Sales of each year' 
FROM SalesLT.SalesOrderHeader
GROUP BY CustomerID, YEAR(OrderDate)

-- Note (WHERE Clause not come with GROUP BY but i will use Having Clause)
-- Returns customers whose total sales exceed 1000 Ascending
SELECT CustomerID,SUM(TotalDue) AS 'Total Sales' FROM SalesLT.SalesOrderHeader
GROUP BY CustomerID
HAVING SUM(TotalDue) > 1000
ORDER BY SUM(TotalDue) 
-- if i need to Sort total sales exceed 1000 Descending:
SELECT CustomerID,SUM(TotalDue) AS 'Total Sales' FROM SalesLT.SalesOrderHeader
GROUP BY CustomerID
HAVING SUM(TotalDue) > 1000
ORDER BY SUM(TotalDue) DESC
-- if I need to use Where:
SELECT CustomerID, TotalDue FROM SalesLT.SalesOrderHeader
WHERE TotalDue > 500
ORDER BY TotalDue


-- Calculates total list price per product category and orders results from highest to lowest total
SELECT ProductCategoryID, SUM(ListPrice) AS 'Total Sales' FROM SalesLT.Product
GROUP BY ProductCategoryID
ORDER BY SUM(ListPrice) DESC


-- Sub Query 
-- Retrieves products that appear in sales orders by filtering ProductID using a subquery
-- Extracts the names of products that have been sold
SELECT ProductID, Name FROM SalesLT.Product
WHERE ProductID IN (
     SELECT ProductID FROM SalesLT.SalesOrderDetail 
)
-- It can use inner join to extracts the names of products that have been sold 
-- IN --> The products are returned once, naturally.
-- INNER JOIN --> Products are returned as duplicates if the same product has been purchased more than once.
-- DISTINCT is applied to remove duplicates, since a product can be sold multiple times
SELECT DISTINCT P.ProductID, P.Name FROM SalesLT.Product AS P
INNER JOIN SalesLT.SalesOrderDetail AS S
ON P.ProductID = S.ProductID


-- Retrieves customers who purchased the product with ID 747,
-- by filtering CustomerID based on matching sales orders and order details
SELECT CustomerID,CONCAT(FirstName,' ',LastName) AS 'Full Name', Phone,EmailAddress 
FROM SalesLT.Customer
WHERE CustomerID IN (
SELECT CustomerID FROM SalesLT.SalesOrderHeader AS SOH
INNER JOIN SalesLT.SalesOrderDetail AS SOD
ON SOH.SalesOrderID = SOD.SalesOrderID
WHERE SOD.ProductID = 747)


-- Returns each product along with its total revenue, calculated by summing LineTotal
-- from SalesOrderDetail for every matching ProductID
SELECT ProductID,(
SELECT SUM(LineTotal) FROM SalesLT.SalesOrderDetail AS SOD 
WHERE SOD.ProductID = P.ProductID) AS 'Total Revenue'
FROM SalesLT.Product AS P


-- Retrieves the distinct products purchased in orders placed by the customer 
SELECT DISTINCT ProductID FROM SalesLT.SalesOrderDetail
    WHERE SalesOrderID IN (
    -- Names of the people who placed the most orders for me 
    SELECT SalesOrderID FROM SalesLT.SalesOrderHeader
    WHERE CustomerID = (
        -- The person who placed the most orders  
        SELECT TOP 1 CustomerID FROM SalesLT.SalesOrderHeader
        GROUP BY CustomerID
        ORDER BY COUNT(SalesOrderID) DESC
        )
)


-- Calculates total revenue generated by each customer by summing all LineTotal values
SELECT C.CustomerID, C.FirstName + ' ' + C.LastName AS 'Customer Name',
SUM(SOD.LineTotal) AS TotalRevenue
FROM SalesLT.Customer AS C
-- JOIN 2 TABLES(SalesLT.Customer,SalesLT.SalesOrderHeader )
INNER JOIN SalesLT.SalesOrderHeader AS SOH ON C.CustomerID = SOH.CustomerID
-- JOIN 2 TABLES(SalesLT.SalesOrderHeader, SalesLT.SalesOrderDetail)
INNER JOIN SalesLT.SalesOrderDetail AS SOD ON SOH.SalesOrderID = SOD.SalesOrderID
WHERE C.CustomerID IN (
     SELECT CustomerID FROM SalesLT.SalesOrderHeader )
GROUP BY C.CustomerID, C.FirstName, C.LastName
ORDER BY TotalRevenue DESC


-- Retrieves the top-selling product by summing the quantity sold for each product
-- The product I found most popular was Light.
SELECT TOP (1) P.ProductID, P.Name AS ProductName, SUM(SOD.OrderQty) AS TotalQuantitySold
FROM SalesLT.Product AS P
INNER JOIN SalesLT.SalesOrderDetail AS SOD ON P.ProductID = SOD.ProductID
GROUP BY p.ProductID, P.Name
ORDER BY TotalQuantitySold DESC


-- Counts the total number of orders placed from each country by linking
-- addresses → customers → sales orders, and returns only countries with orders
SELECT A.CountryRegion AS Country,
COUNT(DISTINCT SOH.SalesOrderID) AS TotalOrders
FROM SalesLT.Address AS A
INNER JOIN SalesLT.CustomerAddress AS CA ON A.AddressID = CA.AddressID
INNER JOIN SalesLT.Customer AS C ON CA.CustomerID = C.CustomerID
INNER JOIN SalesLT.SalesOrderHeader AS SOH ON C.CustomerID = SOH.CustomerID
GROUP BY A.CountryRegion
HAVING COUNT(SOH.SalesOrderID) > 0
ORDER BY TotalOrders



-- Returns customers whose total spending exceeds 5000 by joining
-- Customer --> SalesOrderHeader --> SalesOrderDetail and aggregating LineTotal per customer
SELECT C.CustomerID, C.FirstName + ' ' + C.LastName AS 'Customer Name',
SUM(SOD.LineTotal) AS TotalSpent
FROM SalesLT.Customer AS C
-- JOIN 2 TABLES(SalesLT.Customer,SalesLT.SalesOrderHeader )
INNER JOIN SalesLT.SalesOrderHeader AS SOH ON C.CustomerID = SOH.CustomerID
-- JOIN 2 TABLES(SalesLT.SalesOrderHeader, SalesLT.SalesOrderDetail)
INNER JOIN SalesLT.SalesOrderDetail AS SOD ON SOH.SalesOrderID = SOD.SalesOrderID
GROUP BY C.CustomerID, C.FirstName, C.LastName
HAVING SUM(SOD.LineTotal) > 5000
ORDER BY TotalSpent DESC
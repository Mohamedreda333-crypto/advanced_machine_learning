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
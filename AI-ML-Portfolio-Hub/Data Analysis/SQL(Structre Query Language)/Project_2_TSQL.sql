/*
Project: TSQL(Transection Database) SQL Analysis
Author: [Mohamed Reda Ramadan Khamis]
Date: [20/11/2025]
Description: Comprehensive SQL queries demonstrating database querying techniques
             and business analysis on TSQL(Transection Database) database.
*/

-- Switch to the TSQL database context to execute subsequent statements
USE TSQL 
GO


-- Retrieve a distinct list of customers with their contact and company names, ordered alphabetically by company name
SELECT DISTINCT contactname, companyname
FROM Sales.Customers
ORDER BY companyname ASC;


-- Get unique customer contact and company names sorted by company name
SELECT DISTINCT contactname, companyname
FROM Sales.Customers
ORDER BY companyname ASC;


-- Retrieve all product names that start with the letter 'P'
SELECT productname 
FROM Production.Products 
WHERE productname LIKE 'p%';


-- Select products whose names begin with the letter 'P' using a pattern-matching filter
SELECT productname 
FROM Production.Products 
WHERE productname LIKE 'p%';


-- Retrieve the top 5 products with the lowest unit price, returning only their names
SELECT TOP (5) productname 
FROM Production.Products 
ORDER BY unitprice;
-- Retrieve the top 5 cheapest products, including all available columns
SELECT TOP (5) * 
FROM Production.Products 
ORDER BY unitprice;



-- Retrieve all product names that contain the substring 'GEE' anywhere within the name
SELECT productname 
FROM Production.Products 
WHERE productname LIKE '%GEE%';


-- Retrieve the first and last names of employees whose job title contains the word 'Manager'
SELECT lastname, firstname 
FROM HR.Employees 
WHERE title LIKE '%Manager%';



-- Retrieve customer contact names that start with the letter 'C'
SELECT contactname 
FROM Sales.Customers 
WHERE contactname LIKE 'C%';



-- Retrieve a distinct list of ship names from all orders, sorted alphabetically
SELECT DISTINCT shipname 
FROM Sales.Orders 
ORDER BY shipname;



-- Fetches product names containing 'API' from Production.Products
SELECT productname 
FROM Production.Products 
WHERE productname LIKE '%API%';



-- Retrieves full names of employees by concatenating first and last names, ordered by last name
SELECT CONCAT(firstname, ' ', lastname) 
FROM HR.Employees 
ORDER BY lastname;



-- Retrieves the top 5 shipper company names containing 'ZHISN' from Sales.Shippers
SELECT TOP (5) companyname 
FROM Sales.Shippers 
WHERE companyname LIKE '%ZHISN%';



-- Lists products with their prices and categorizes them as Cheap, Moderate, or Expensive
SELECT productname, unitprice,
    CASE
        WHEN unitprice < 20 THEN 'Cheap'
        WHEN unitprice >= 20 AND unitprice < 50 THEN 'Moderate'
        ELSE 'Expensive'
    END AS PriceCategory
FROM Production.Products
ORDER BY unitprice;



-- Retrieves employees' full names, calculates their age, and categorizes them into age groups
-- Using Between Range (AND)
SELECT CONCAT(firstname, ' ', lastname) AS FullName,
       (YEAR(GETDATE()) - YEAR(birthdate)) AS Age,
       CASE  
           WHEN (YEAR(GETDATE()) - YEAR(birthdate)) BETWEEN 0 AND 12 THEN 'Child'
           WHEN (YEAR(GETDATE()) - YEAR(birthdate)) BETWEEN 13 AND 19 THEN 'Teenager'
           WHEN (YEAR(GETDATE()) - YEAR(birthdate)) BETWEEN 20 AND 39 THEN 'Young Adult'
           WHEN (YEAR(GETDATE()) - YEAR(birthdate)) BETWEEN 40 AND 59 THEN 'Adult'
           ELSE 'Senior'
       END AS AgeCategory
FROM HR.Employees;

-- Another way
SELECT CONCAT(firstname,' ',lastname),(YEAR(GETDATE())-YEAR(birthdate)) AS Age, 
CASE 
    WHEN (YEAR(GETDATE())-YEAR(birthdate)) >= 0 AND (YEAR(GETDATE())-YEAR(birthdate)) <= 12 THEN 'Child' 
    WHEN (YEAR(GETDATE())-YEAR(birthdate)) > 12 AND (YEAR(GETDATE())-YEAR(birthdate)) <= 19 THEN 'Teenager' 
    WHEN (YEAR(GETDATE())-YEAR(birthdate)) > 19 AND (YEAR(GETDATE())-YEAR(birthdate)) <= 39 THEN 'Young Adult' 
    WHEN (YEAR(GETDATE())-YEAR(birthdate)) > 39 AND (YEAR(GETDATE())-YEAR(birthdate)) <= 59 THEN 'Adult' 
    ELSE 'Senior' 
END AS AgeCategory 
FROM HR.Employees


-- INNER Join
-- Returns all orders along with their corresponding order details using an inner join on orderid
SELECT * 
FROM Sales.Orders 
INNER JOIN Sales.OrderDetails 
    ON Orders.orderid = OrderDetails.orderid;


-- Retrieves order shipping details along with unit price and discount from matching order records
SELECT requireddate, shipaddress, shipcity, shipcountry, unitprice, discount 
FROM Sales.Orders 
INNER JOIN Sales.OrderDetails 
    ON Orders.orderid = OrderDetails.orderid;


-- Retrieves order IDs that have matching records in OrderDetails
SELECT Orders.orderid
FROM Sales.Orders 
INNER JOIN Sales.OrderDetails 
    ON Orders.orderid = OrderDetails.orderid;

-------------------------------------------------------------------------------------
SELECT * from Sales.Customers
SELECT * FROM Sales.Orders
-- To Join 2 Tables 
-- Point out That 830 rows as returned
SELECT C.companyname , O.orderdate FROM Sales.Customers AS C
INNER JOIN Sales.Orders AS O
ON C.custid = O.custid


SELECT * FROM Production.Products
SELECT * FROM Production.Categories
-- To Join 2 Tables 
-- Point out That 77 rows as returned
SELECT C.categoryid, C.categoryname, P.productid, P.productname 
FROM Production.Categories AS C
INNER JOIN Production.Products AS P
ON C.categoryid = P.categoryid


-- To join 3 tables
-- 2155 rows will be returned
SELECT * FROM Sales.Customers
SELECT * FROM Sales.Orders
SELECT * FROM Sales.OrderDetails

SELECT * FROM Sales.Customers AS C
INNER JOIN Sales.Orders AS O
ON C.custid = O.custid
INNER JOIN Sales.OrderDetails AS OD
ON O.orderid = OD.orderid

-- Retrieves customers with their orders and corresponding order details using chained inner joins
SELECT C.custid, C.companyname, O.orderid, O.orderdate, OD.productid, OD.qty FROM Sales.Customers AS C
INNER JOIN Sales.Orders AS O
ON C.custid = O.custid
INNER JOIN Sales.OrderDetails AS OD
ON O.orderid = OD.orderid


-- Retrieves detailed customer, supplier, product, and category information for orders 
-- where the order's unit price exceeds 50, ordered by the product price
SELECT 
    C.custid, 
    C.contactname AS 'Customer Contact Name', 
    C.companyname AS 'Customer Company Name',  
    S.contactname AS 'Supplier Contact Name',
    S.companyname AS 'Supplier Company Name',
    PC.categoryname,
    OD.unitprice AS 'Unit Price in Order', 
    P.unitprice AS 'Product Price'
FROM Sales.Customers AS C
INNER JOIN Sales.Orders AS O
    ON C.custid = O.custid
INNER JOIN Sales.OrderDetails AS OD
    ON O.orderid = OD.orderid
INNER JOIN Production.Products AS P
    ON OD.productid = P.productid
INNER JOIN Production.Suppliers AS S
    ON P.supplierid = S.supplierid
INNER JOIN Production.Categories AS PC 
    ON P.categoryid = PC.categoryid
WHERE OD.unitprice > 50 
ORDER BY P.unitprice;






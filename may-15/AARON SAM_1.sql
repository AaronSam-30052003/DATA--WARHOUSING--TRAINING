--CREATION OF DATABASE
CREATE DATABASE ASSIGNMENT;
GO
USE ASSIGNMENT;
--CREATING SCHEMA
CREATE SCHEMA PRO;
GO
-- CREATE THE TABLE NAME PRODUCT
CREATE TABLE PRO.Product (
    ProductID INT PRIMARY KEY IDENTITY(1,1),
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    Price DECIMAL(10, 2),
    StockQuantity INT,
    Supplier VARCHAR(100)
);
GO
--INSERT VALUES INTO PRODUCT TABLE
INSERT INTO PRO.Product (ProductName, Category, Price, StockQuantity, Supplier)
VALUES 
('Laptop', 'Electronics', 70000, 50, 'TechMart'),
('Office Chair', 'Furniture', 5000, 100, 'HomeComfort'),
('Smartwatch', 'Electronics', 15000, 200, 'GadgetHub'),
('Desk Lamp', 'Lighting', 1200, 300, 'BrightLife'),
('Wireless Mouse', 'Electronics', 1500, 250, 'GadgetHub');
GO

--1.CRUD OPERATIONS
--1-Add a new product
INSERT INTO PRO.Product 
VALUES ('Gaming Keyboard', 'Electronics', 3500, 150, 'TechMart');
GO
--2-Update product price
UPDATE PRO.Product
SET Price = Price * 1.10
WHERE Category = 'Electronics';
GO
--3-Delete a product
DELETE FROM PRO.Product
WHERE ProductID = 4;
GO
--4-Read all products
SELECT * FROM PRO.Product
ORDER BY Price DESC;
GO

---END OF CRUD OPERATION----

--2.SORTING AND FILTERING

--5-Sort products by stock quantity
SELECT * FROM PRO.Product
ORDER BY StockQuantity ASC;
GO
--6-Filter products by category
SELECT * FROM PRO.Product
WHERE Category = 'Electronics';
GO
--7-Filter products with AND condition
SELECT * FROM PRO.Product
WHERE Category = 'Electronics' AND Price > 5000;
GO
--8-Filter products with OR condition
SELECT * FROM PRO.Product
WHERE Category = 'Electronics' OR Price < 2000;
GO

---END OF SORTING AND FILERTING----

--3.AGGREGATION AND GROUPING

--9-Calculate total stock value
SELECT SUM(Price * StockQuantity) AS TotalStockValue
FROM PRO.Product;
GO
--10-Average price of each category
SELECT Category, AVG(Price) AS AveragePrice
FROM PRO.Product
GROUP BY Category;
GO
--11-Total number of products by supplier
SELECT COUNT(*) AS ProductCount
FROM PRO.Product
WHERE Supplier = 'GadgetHub';
GO

---END OF AGGREGATION AND GROUPING---

--4.CONDITIONAL AND PATTERN MATCHING

--12-Find products with a specific keyword
SELECT * FROM PRO.Product
WHERE ProductName LIKE '%Wireless%';
GO
--13-Search for products from multiple suppliers
SELECT * FROM PRO.Product
WHERE Supplier IN ('TechMart', 'GadgetHub');
GO
--14-Filter using BETWEEN operator
SELECT * FROM PRO.Product
WHERE Price BETWEEN 1000 AND 20000;
GO

---END OF CONDITIONAL AND PATTERN MATCHING

--5.ADVANCED QUERIES

--15-Products with high stock
SELECT * FROM PRO.Product
WHERE StockQuantity > (SELECT AVG(StockQuantity) FROM PRO.Product);
GO
--16-Get top 3 expensive products
SELECT TOP 3 * FROM PRO.Product
ORDER BY Price DESC;
GO
--17-Find duplicate supplier names
SELECT Supplier FROM PRO.Product
GROUP BY Supplier
HAVING COUNT(*) > 1;
GO
--18-Product summary
SELECT Category, COUNT(*) AS ProductCount, SUM(Price * StockQuantity) AS TotalStockValue FROM PRO.Product
GROUP BY Category;
GO

---END OF ADVANCED QUERIES---

--6.JOIN AND SUBQUERIES

--19-Supplier with most products
SELECT TOP 1 Supplier, COUNT(*) AS ProductCount
FROM PRO.Product
GROUP BY Supplier
ORDER BY ProductCount DESC;
GO
--20-Most expensive product per category
SELECT p.*
FROM pro.Product p, 
     (SELECT Category, MAX(Price) AS MaxPrice FROM pro.Product GROUP BY Category) maxp
WHERE p.Category = maxp.Category AND p.Price = maxp.MaxPrice;
GO

---END OF ASSIGNMENT----















USE ASSIGNMENT;
GO
--CREATE SCHEMA
CREATE SCHEMA INV;
GO
--CREATE TABLE
CREATE TABLE INV.ProductInventory (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50),
    Category VARCHAR(50),
    Quantity INT,
    UnitPrice INT,
    Supplier VARCHAR(50),
    LastRestocked DATE
);
GO
--INSERT VALUES INTO TABLE
INSERT INTO INV.ProductInventory 
VALUES
(1, 'Laptop', 'Electronics', 20, 70000, 'TechMart', '2025-04-20'),
(2, 'Office Chair', 'Furniture', 50, 5000, 'HomeComfort', '2025-04-18'),
(3, 'Smartwatch', 'Electronics', 30, 15000, 'GadgetHub', '2025-04-22'),
(4, 'Desk Lamp', 'Lighting', 80, 1200, 'BrightLife', '2025-04-25'),
(5, 'Wireless Mouse', 'Electronics', 100, 1500, 'GadgetHub', '2025-04-30');
GO

--1.CRUD OPERATIONS

--1.Add a new product
INSERT INTO INV.ProductInventory 
VALUES (6, 'Gaming Keyboard', 'Electronics', 40, 3500, 'TechMart', '2025-05-01');
GO
--2.Update stock quantity
UPDATE INV.ProductInventory
SET Quantity = Quantity + 20
WHERE ProductID = 4;
GO
--3.Delete a discontinued product
DELETE FROM INV.ProductInventory
WHERE ProductID = 2;
GO
--4.Read all products
SELECT * FROM INV.ProductInventory
ORDER BY ProductName ASC;
GO

--END OF CRUD OPERATIONS--

--2.SORTING AND FILTERING

--5.Sort by Quantity
SELECT * FROM INV.ProductInventory
ORDER BY Quantity DESC;
GO
--6.Filter by Category
SELECT * FROM INV.ProductInventory
WHERE Category = 'Electronics';
GO
--7.Filter with AND condition
SELECT * FROM INV.ProductInventory
WHERE Category = 'Electronics' AND Quantity > 20;
GO
--8.Filter with OR condition
SELECT * FROM INV.ProductInventory
WHERE Category = 'Electronics' OR UnitPrice < 2000;
GO

--END OF SORTING AND FILTERING--

--3.AGGREGATION AND GROUPING

--9.Total stock value calculation
SELECT ProductID, ProductName, Quantity * UnitPrice AS TotalValue
FROM INV.ProductInventory;
GO
--10.Average price by category
SELECT Category, AVG(UnitPrice) AS AveragePrice
FROM INV.ProductInventory
GROUP BY Category;
GO
--11.Count products by supplier
SELECT Supplier, COUNT(*) AS ProductCount
FROM INV.ProductInventory
WHERE Supplier = 'GadgetHub'
GROUP BY Supplier;
GO

--END OF AGGREGATION AND GROUPING--

--4.CONDITIONAL AND PATTERN MATCHING

--12.Find products by name prefix
SELECT * FROM INV.ProductInventory
WHERE ProductName LIKE 'W%';
GO
--13.Filter by supplier and price
SELECT * FROM INV.ProductInventory
WHERE Supplier = 'GadgetHub' AND UnitPrice > 10000;
GO
--14.Filter using BETWEEN operator
SELECT * FROM INV.ProductInventory
WHERE UnitPrice BETWEEN 1000 AND 20000;
GO

--5. ADVANCED QUERIES

--15.Top 3 most expensive products
SELECT TOP 3 * FROM INV.ProductInventory
ORDER BY UnitPrice DESC;
GO
--16.Products restocked recently
SELECT * FROM INV.ProductInventory
WHERE LastRestocked >= GETDATE() - 10;
GO
--17.Group by Supplier
SELECT Supplier, SUM(Quantity) AS TotalQuantity
FROM INV.ProductInventory
GROUP BY Supplier;
GO
--18.Check for low stock
SELECT * FROM INV.ProductInventory
WHERE Quantity < 30;
GO

--END OF ADVANCED QUERIES--

--6.JOIN AND SUBQUERIES

--19.Supplier with most products
SELECT TOP 1 Supplier, COUNT(*) AS ProductCount
FROM INV.ProductInventory
GROUP BY Supplier
ORDER BY ProductCount DESC;
GO
--20.Product with highest stock value
SELECT TOP 1 *, (Quantity * UnitPrice) AS StockValue
FROM INV.ProductInventory
ORDER BY StockValue DESC;
GO

--END OF JOIN AND SUB QUERIES--












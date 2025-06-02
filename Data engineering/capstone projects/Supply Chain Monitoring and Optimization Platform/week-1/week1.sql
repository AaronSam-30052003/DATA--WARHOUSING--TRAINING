-- CREATE DATABASE
CREATE DATABASE SupplyChain;
GO
--USE OF DATABASE
USE SupplyChain;
GO
--CREATE SCHEMA
CREATE SCHEMA supply;
GO
-- CREATE SUPLLIERS TABLE
CREATE TABLE supply.Suppliers (
    SupplierID INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(100),
    ContactEmail NVARCHAR(100)
);
GO

-- CREATE INVENTORY TABLE
CREATE TABLE supply.Inventory (
    ItemID INT IDENTITY(1,1) PRIMARY KEY,
    ItemName NVARCHAR(100),
    Stock INT,
    ReorderThreshold INT
);
GO

-- CREATE ORDERS TABLE
CREATE TABLE supply.Orders (
    OrderID INT IDENTITY(1,1) PRIMARY KEY,
    SupplierID INT FOREIGN KEY REFERENCES supply.Suppliers(SupplierID),
    ItemID INT FOREIGN KEY REFERENCES supply.Inventory(ItemID),
    OrderDate DATE,
    DeliveryDate DATE
);
GO

-- INSERT SAMPLE SUPPLIERS VALUE
INSERT INTO supply.Suppliers (Name, ContactEmail)
VALUES 
('bubududu', 'bubududu@gmail.com'),
('Mickeychoki', 'Mickeychoki@qsupply.com'),
('tomie.', 'tomie@goods.com'),
('LogiPro Solutions', 'logistics@logipro.com'),
('Hexaware technologies','hexaware@tech.com');
GO

-- INSERT SAMPLE VALUE INTO INVENTORY
INSERT INTO supply.Inventory (ItemName, Stock, ReorderThreshold)
VALUES 
('Widget A', 20, 30),
('Widget B', 50, 40),
('Gadget X', 15, 25),
('Part Z', 100, 50),
('Assembly Kit 9', 10, 20),
('Gadget A',20,15);
GO

-- INSERT SAMPLE ORDERS VALUES
INSERT INTO supply.Orders (SupplierID, ItemID, OrderDate, DeliveryDate)
VALUES 
(1, 1, '2025-05-01', '2025-05-10'),
(2, 2, '2025-05-03', '2025-05-08'),
(3, 3, '2025-05-05', '2025-05-18'),
(1, 4, '2025-05-06', '2025-05-12'),
(2, 5, '2025-05-08', '2025-05-14'),
(4, 1, '2025-05-10', '2025-05-22'),
(3, 6, '2025-05-11', '2025-05-20'),
(1, 3, '2025-05-12', '2025-05-16'),
(2, 6, '2025-05-13', '2025-05-17'),
(4, 5, '2025-05-14', '2025-05-24');
GO

--BASIC CURD OPERATIONS
-- INSERT NEW SUPPLIERS
INSERT INTO supply.Suppliers (Name, ContactEmail)
VALUES ('Samie', 'samie@gmail.com');
GO
-- INSERT NEW INVENTORY ITEMS
INSERT INTO supply.Inventory (ItemName, Stock, ReorderThreshold)
VALUES ('Widget C', 60, 50);
GO
-- INSERT NEW ORDERS
INSERT INTO supply.Orders (SupplierID, ItemID, OrderDate, DeliveryDate)
VALUES (1, 2, '2025-06-01', '2025-06-10');
GO
-- UPADTE CONTACT EMIAL IN SUPLLIERS
UPDATE supply.Suppliers
SET ContactEmail = 'samieTomie.@gmail.com'
WHERE SupplierID = 2;

-- INCREASE STOCK IN INVENTORY
UPDATE supply.Inventory
SET Stock = Stock + 20
WHERE ItemID = 3;
GO
-- CHANGE DELIVERY DATE IN ORDER-5
UPDATE supply.Orders
SET DeliveryDate = '2025-06-15'
WHERE OrderID = 5;
GO
-- Delete a supplier by SupplierID
DELETE FROM supply.Suppliers
WHERE SupplierID = 5;
GO
-- Delete an order by OrderID
DELETE FROM supply.Orders
WHERE OrderID = 10;
GO
-- VIEW INSERTED DATA
SELECT * FROM supply.Suppliers;
SELECT * FROM supply.Inventory;
SELECT * FROM supply.Orders;
GO

-- CREATE STORED PROCEDURE FOR AUTO REORDER
CREATE OR ALTER PROCEDURE AutoReorder
AS
BEGIN
    UPDATE supply.Inventory
    SET Stock = Stock + 100
    WHERE Stock < ReorderThreshold;
END;
GO


-- RUN AUTO ORDER
EXEC AutoReorder;
GO

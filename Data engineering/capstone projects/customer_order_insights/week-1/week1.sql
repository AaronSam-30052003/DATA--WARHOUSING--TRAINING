-- CREATE DATABASE
CREATE DATABASE customer_orders;
GO
-- USE THE CREATED DATABASE
USE customer_orders;
GO
--CREATE SCHEMA
CREATE SCHEMA orders;
-- CREATE CUSTOMER TABLE
CREATE TABLE orders.customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);
GO

-- CREATE ORDERS TABLE
CREATE TABLE orders.orders (
    order_id INT PRIMARY KEY,
    customer_id INT FOREIGN KEY REFERENCES orders.customers(customer_id) ON DELETE CASCADE,
    order_date DATE,
    delivery_date DATE
);
GO

-- CREATE DELIVERY STATUS TABLE
CREATE TABLE orders.delivery_status (
    status_id INT PRIMARY KEY,
    order_id INT FOREIGN KEY REFERENCES orders.orders(order_id)ON DELETE CASCADE,
    status VARCHAR(50),
    last_updated DATETIME DEFAULT GETDATE()
);
GO
-- INSERT INTO CUSTOMERS
INSERT INTO orders.customers (customer_id, name, email) VALUES
(1, 'Aaron', 'aaron@email.com'),
(2, 'Sobana', 'sobana@email.com'),
(3, 'Choki', 'choki@email.com');
GO

-- INSERT INTO ORDERS
INSERT INTO orders.orders (order_id, customer_id, order_date, delivery_date) VALUES
(101, 1, '2025-05-25', '2025-05-30'),
(102, 1, '2025-05-28', '2025-06-02'),
(103, 2, '2025-05-27', '2025-06-05'),
(104, 3, '2025-05-29', '2025-06-10');
GO

-- INSERT INTO DELIVERY_STATUS
INSERT INTO orders.delivery_status (status_id, order_id, status, last_updated) VALUES
(1, 101, 'Delivered', GETDATE()),
(2, 102, 'In Transit', GETDATE()),
(3, 103, 'Pending', GETDATE()),
(4, 104, 'Delivered', GETDATE());
GO

-- SAMPLE CRUD OPERATIONS ON ORDERS

-- INSERT NEW ORDER (CREATE)
INSERT INTO orders.orders (order_id, customer_id, order_date, delivery_date)
VALUES (105, 1, '2025-05-25', '2025-05-30');
GO

-- SELECT ALL ORDERS (READ)
SELECT * FROM orders.orders;
GO

-- UPDATE DELIVERY DATE FOR AN ORDER (UPDATE)
UPDATE orders.orders
SET delivery_date = '2025-06-01'
WHERE order_id = 101;
GO

-- DELETE AN ORDER BY ORDER_ID 
DELETE FROM orders.orders WHERE order_id = 101;
GO

-- CREATE STORED PROCEDURE TO FETCH DELAYED DELIVERIES FOR A CUSTOMER
CREATE PROCEDURE GetDelayedDeliveries
    @CustomerId INT
AS
BEGIN
    SELECT o.order_id,o.delivery_date
    FROM orders.orders o
    INNER JOIN orders.delivery_status d ON o.order_id = d.order_id
    WHERE o.customer_id = @CustomerId
      AND o.delivery_date < CAST(GETDATE() AS DATE)
      AND d.status <> 'Delivered';
END;
GO

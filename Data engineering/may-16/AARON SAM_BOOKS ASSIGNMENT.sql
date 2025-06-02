USE ASSIGNMENT;
GO
--CREATING SCHEMA
CREATE SCHEMA books;
GO
--CREATION OF TABLE
CREATE TABLE books.Book(
    BookID INT PRIMARY KEY IDENTITY(1,1),
    Title VARCHAR(50),
    Author VARCHAR(50),
    Genre VARCHAR(50),
    Price DECIMAL(10, 2),
    PublishedYear INT,
    Stock INT
);
GO
--INSERT VALUES INTO TABLE
INSERT INTO books.Book VALUES 
('The Alchemist', 'Paulo Coelho', 'Fiction', 300, 1988, 50),
('Sapiens', 'Yuval Noah Harari', 'Non-Fiction', 500, 2011, 30),
('Atomic Habits', 'James Clear', 'Self-Help', 400, 2018, 25),
('Rich Dad Poor Dad', 'Robert Kiyosaki', 'Personal Finance', 350, 1997, 20),
('The Lean Startup', 'Eric Ries', 'Business', 450, 2011, 15);
GO

--1.CRUD OPERATIONS

--1.Add a new book
INSERT INTO books.Book VALUES('Deep Work','Cal Newport','Self-Help', 420, 2016, 35);
GO
--2.Update book price
UPDATE books.Book
SET Price=Price+50
WHERE Genre='Self-Help';
GO
--3.Delete a book
DELETE FROM books.Book
WHERE BookID=4;
GO
--4.Read all books
SELECT * FROM books.Book
ORDER BY Title ASC;
GO

--END OF CRUD OPERATIONS--

--2. SORTING & FILTERING

--5.Sort by price
SELECT *FROM books.Book
ORDER BY Price DESC;
GO
--6.Filter by genre
SELECT *FROM books.Book
WHERE Genre='Fiction';
GO
--7.Filter with AND condition
SELECT* FROM books.Book
WHERE Genre='Self-Help' AND Price >400;
GO
--8.Filter with OR condition
SELECT * FROM books.Book
WHERE Genre = 'Fiction' OR PublishedYear > 2000;
GO

--END OF SORTING & FILTERING--

--3.AGGREGATION & GROUPING

--9.Total stock value
SELECT SUM(Price * Stock) AS TotalStockValue
FROM books.Book;
GO
--10.Average price by genre
SELECT Genre, AVG(Price) AS AveragePrice
FROM books.Book
GROUP BY Genre;
GO
--11.Total books by author
SELECT COUNT(*) AS TotalBooks
FROM books.Book
WHERE Author = 'Paulo Coelho';
GO

--END OF AGGREGATION AND GROUPING--

--4. CONDITIONAL & PATTERN MATCHING

--12.Find books with a keyword in title
SELECT * FROM books.Book
WHERE Title LIKE '%The%';
GO
--13.Filter by multiple conditions
SELECT * FROM books.Book
WHERE Author = 'Yuval Noah Harari' AND Price < 600;
GO
--14.Find books within a price range
SELECT * FROM books.Book
WHERE Price BETWEEN 300 AND 500;
GO

--END OF CONDITIONAL & PATTERN MATCHING--

--5. ADVANCED QUERIES

--15.Top 3 most expensive books
SELECT TOP 3 * FROM books.Book
ORDER BY Price DESC;
GO
--16.Books published before a specific year
SELECT * FROM books.Book
WHERE PublishedYear < 2000;
GO
--17.Group by Genre
SELECT Genre, COUNT(*) AS BookCount
FROM books.Book
GROUP BY Genre;
GO
--18.Find duplicate titles
SELECT Title FROM books.Book
GROUP BY Title
HAVING COUNT(*) > 1;
GO

--END OF  ADVANCED QUERIES--

--6.JOIN & SUBQUERIES

--19.Author with the most books
SELECT TOP 1 Author, COUNT(*) AS BookCount
FROM books.Book
GROUP BY Author
ORDER BY BookCount DESC;
GO
--20.Oldest book by genre
SELECT b.*
FROM books.Book b
JOIN (
    SELECT Genre, MIN(PublishedYear) AS OldestYear
    FROM books.Book b
    GROUP BY Genre
) g ON b.Genre = g.Genre AND b.PublishedYear = g.OldestYear;
GO









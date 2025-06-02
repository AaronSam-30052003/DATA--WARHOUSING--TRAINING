USE ASSIGNMENT;
GO
--CREATE OF SCHEMA
CREATE SCHEMA EMP;
GO
--CREATE TABLE
CREATE TABLE EMP.EmployeeAttendance (
    AttendanceID INT PRIMARY KEY IDENTITY(1,1),
    EmployeeName VARCHAR(100),
    Department VARCHAR(50),
    Date DATE,
    Status VARCHAR(20),
    HoursWorked INT
);
GO
--INSERT VALUES INTO TABLE
INSERT INTO EMP.EmployeeAttendance (EmployeeName, Department, Date, Status, HoursWorked)
VALUES 
('John Doe', 'IT', '2025-05-01', 'Present', 8),
('Priya Singh', 'HR', '2025-05-01', 'Absent', 0),
('Ali Khan', 'IT', '2025-05-01', 'Present', 7),
('Riya Patel', 'Sales', '2025-05-01', 'Late', 6),
('David Brown', 'Marketing', '2025-05-01', 'Present', 8);
GO

--1.CRUD OPERATIONS

--1.Add a new attendance record
INSERT INTO EMP.EmployeeAttendance VALUES('Neha Sharma', 'Finance', '2025-05-01', 'Present', 8);
GO
--2.Update attendance status
UPDATE EMP.EmployeeAttendance
SET Status='Present'
WHERE EmployeeName = 'Riya Patel';
GO
--3.Delete a record
DELETE FROM EMP.EmployeeAttendance
WHERE EmployeeName = 'Priya Singh';
GO
--4.Read all records
SELECT * FROM EMP.EmployeeAttendance
ORDER BY EmployeeName ASC;
GO

--END OF CRUD OPERATIONS---

--2. SORTING AND FILTERING

--5.Sort by Hours Worked
SELECT * FROM EMP.EmployeeAttendance
ORDER BY HoursWorked DESC;
GO
--6.Filter by Department
SELECT * FROM EMP.EmployeeAttendance
WHERE Department = 'IT';
GO
--7.Filter with AND condition
SELECT * FROM EMP.EmployeeAttendance
WHERE Department = 'IT' AND Status = 'Present';
GO
--8.Filter with OR condition
SELECT * FROM EMP.EmployeeAttendance
WHERE Status = 'Absent' OR Status = 'Late';
GO

--END OF SORTING AND FILTERING--

--3.AGGREGATION AND GROUPING

--9.Total Hours Worked by Department
SELECT Department, SUM(HoursWorked) AS TotalHours
FROM EMP.EmployeeAttendance
GROUP BY Department;
GO
--10.Average Hours Worked
SELECT AVG(HoursWorked) AS AverageHoursWorked
FROM EMP.EmployeeAttendance;
GO
--11.Attendance Count by Status
SELECT Status, COUNT(*) AS Count
FROM EMP.EmployeeAttendance
GROUP BY Status;
GO

--END OF AGGREGATION AND GROUPING--

--4.CONDITIONAL AND PATTERN MATCHING

--12.Find employees by name prefix
SELECT * FROM EMP.EmployeeAttendance
WHERE EmployeeName LIKE 'R%';
GO
--13.Filter by multiple conditions
SELECT * FROM EMP.EmployeeAttendance
WHERE HoursWorked > 6 AND Status = 'Present';
GO
--14.Filter using BETWEEN operator
SELECT * FROM EMP.EmployeeAttendance
WHERE HoursWorked BETWEEN 6 AND 8;
GO

--END OF CONDITIONAL AND PATTERN MATCHING--

--5.ADVANCED QUERIES

--15.Top 2 employees with the most hours
SELECT TOP 2 * FROM EMP.EmployeeAttendance
ORDER BY HoursWorked DESC;
GO
--16.Employees who worked less than the average hours
SELECT * FROM EMP.EmployeeAttendance
WHERE HoursWorked <(SELECT AVG(HoursWorked) FROM EMP.EmployeeAttendance);
GO
--17.Group by Status
SELECT Status, AVG(HoursWorked) AS AvergeHours
FROM EMP.EmployeeAttendance
GROUP BY Status;
--18.Find duplicate entries
SELECT EmployeeName, Date, COUNT(*) AS EntryCount
FROM EMP.EmployeeAttendance
GROUP BY EmployeeName, Date
HAVING COUNT(*) > 1;
GO

--END OF ADVANCED QUERIES--

--6.JOIN AND SUBQUERIES

--19.Department with most Present employees
SELECT TOP 1 Department, COUNT(*) AS PresentCount
FROM EMP.EmployeeAttendance
WHERE Status = 'Present'
GROUP BY Department
ORDER BY PresentCount DESC;
GO
--20.Employee with maximum hours per department
SELECT ea.*
FROM EMP.EmployeeAttendance ea
JOIN (
    SELECT Department, MAX(HoursWorked) AS MaxHours
    FROM EMP.EmployeeAttendance
    GROUP BY Department
) d ON ea.Department = d.Department AND ea.HoursWorked = d.MaxHours;
GO

--END OF JOINS AND SUBQUERIES--

















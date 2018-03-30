SELECT column1, column2, ...
FROM table_name;

SELECT * FROM table_name;
#Select all

SELECT DISTINCT column1, column2, ...
FROM table_name;
#Select all distinct values from column1 and column2

SELECT COUNT(DISTNCT column1) FROM table_name;
#Count only allow 1 arguments

SELECT column1, column2
FROM table_name
WHERE condition;

Operator
= equal <> not equal
BETWEEN between two inclusive range - example: WHERE (Price BETWEEN 10 AND 20)
LIKE Search for a pattern
IN Specify multiple possible values for a column1
IS NULL = find value that NULL
IS NOT NULL

LIKE Syntax = regex
% - represent 0, 1 or many characters
_ - underscore represents a single character
WHERE CustomerName LIKE 'a%' - 	Finds any values that starts with "a"

Chain conditions together using AND, OR, NOT

SELECT column1,column2
FROM table_name
ORDER BY column1 ASC|DESC

#Insert into STATEMENT
INSERT INTO table_name (column1, column2,..)
VALUES (value1,value2)

#Insert all coumns
INSERT INTO table_name
VALUES (value1,value2)

#SQL update STATEMENT & make sure you never omit the WHERE clause, ALL RECORDS will be updated!
UPDATE table_name
SET column1 = value1, column2 = value2
WHERE condition;

#Delete all RECORDS
DELETE FROM table_name;

DELETE FROM Customers
WHERE CustomerName='Alfreds Futterkiste';

Limit the amouunt of return
SELECT column1
FROM table_name
WHERE condition
LIMIT num;

SELECT TOP num * FROM table_name
SELECT TOP number PERCENT * FROM table_name #Select top percent of the records from

SELECT MIN(column1)
FROM table_name

SELECT MAX(column1)
FROM table_name

Great Functionality
AVG(column_name), SUM(column_name), 

Customer ALIAS
SELECT CustomerID as ID,
FROM Customers;

SELECT o.OrderID, o.OrderDate, c.CustomerName
FROM Customers AS c, Orders AS o
WHERE c.CustomerName="Around the Horn" AND c.CustomerID=o.CustomerID;

Aliases can be useful when:

There are more than one table involved in a query
Functions are used in the query
Column names are big or not very readable
Two or more columns are combined together

Join offer
SELECT Orders.column_name, Customers.column_name, ...
FROM Orders
INNER JOIN Customers
ON Orders.CustomerID=Customers.CustomerID;

INNER - return records that have matching values in both tables
Left Outer Join - return records that the left table and the matched records from the right table
right Outer Join - return records that the right table and the matched records from the left table
Full Outer Join - return all records when there is a match in either left or right table

Union columns from two tables
SELECT column_name(s) FROM table1
UNION or UNION ALL (Allow duplicate values)
SELECT column_name(s) FROM table2

SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
ORDER BY COUNT(CustomersID) DESC;
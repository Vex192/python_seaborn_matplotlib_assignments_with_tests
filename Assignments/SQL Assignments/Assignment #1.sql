-- Assignment #1
-- Task
/*
Write FOUR queries:
1. Select ALL columns from passengers
2. Select only Name, Sex, Age, and Pclass
3. Show the first 10 rows — all columns
4. Show only Name and Survived — first 5 rows
How many total rows are in the table? Write as a comment.
*/
-- Begin your work here
-- Query 1
SELECT *
FROM passengers;

-- Query 2
SELECT Name, Sex, Age, Pclass
FROM passengers;

-- Query 3
SELECT *
FROM passengers 
WHERE PassengerID <= 10;

-- Query 4
SELECT Name, Survived
FROM passengers
WHERE PassengerId <= 5;
-- There are 30 rows in the table
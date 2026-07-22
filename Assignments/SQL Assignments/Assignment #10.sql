-- Assignment #10
-- Task
/*
Write FOUR queries:
1. Find all passengers with missing Age — count them
2. Find all passengers with known Age
3. Use COALESCE to show Age but display 0 wherever Age is NULL. Show: Name, Age,
COALESCE(Age,0) AS AgeOrZero
4. Find survival rate for passengers WITH known age only
What percentage of passengers have missing age? Write as a comment.
*/
-- Begin your work here
-- Query 1
SELECT * 
FROM passengers 
WHERE Age IS NULL;

-- Query 2
SELECT *
FROM passengers
WHERE Age IS NOT NULL;

-- Query 3
SELECT Name, Age,
       COALESCE(Age, 0) AS AgeOrZero
FROM passengers;

-- Query 4
SELECT ROUND(AVG(Survived * 100.0), 2) AS SuvivalRate
FROM passengers
WHERE Age IS NOT NULL;

-- 20 percent of passengers have missing age
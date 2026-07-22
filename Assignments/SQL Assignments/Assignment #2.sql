-- Assignment #2
-- Task
/*
Write FIVE queries:
1. Find all female passengers
2. Find all passengers in 1st Class (Pclass = 1)
3. Find male passengers in 3rd Class who did NOT survive
4. Find passengers who embarked from "C" OR "Q"
5. Find passengers whose Age is NULL (missing)
How many passengers have missing Age? Write as a comment.
*/
-- Begin your work here
-- Query 1
SELECT *
FROM passengers
WHERE Sex = 'female';

-- Query 2
SELECT *
FROM passengers
WHERE Pclass = 1;

-- Query 3
SELECT *
FROM passengers
WHERE Sex = 'male' AND Pclass = 3 AND Survived = 0;

-- Query 4
SELECT *
FROM passengers
WHERE Embarked = 'C' OR 'Q';

-- Query 5
SELECT *
FROM passengers
WHERE Age IS NULL;
-- 6 passengers have a missing age

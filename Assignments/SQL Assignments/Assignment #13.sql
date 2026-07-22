-- Assignment #13
-- Task
/*
Write FOUR queries:
1. Show all passenger Names in UPPERCASE
2. Find all passengers whose Name contains "Miss" using LIKE "%Miss%"
3. Find all passengers whose Name contains "Mr." — count how many
4. Show Name and NameLength = LENGTH(Name). Show 5 passengers with longest names.
How many passengers have "Miss" in their name? Write as a comment.
*/
-- Begin your work here
-- Query 1
SELECT UPPER(Name) AS UpperCaseName
FROM passengers;

-- Query 2
SELECT *
FROM passengers
WHERE Name LIKE '%Miss%';

-- Query 3
SELECT *
FROM passengers
WHERE Name LIKE '%Mr.%';

-- Query 4
SELECT Name, LENGTH(Name) AS NameLength
FROM passengers
LIMIT 5;

-- 6 passengers have Miss in their name

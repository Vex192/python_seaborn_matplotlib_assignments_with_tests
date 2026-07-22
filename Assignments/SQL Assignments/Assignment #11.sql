-- Assignment #11
-- Task
/*
Write THREE queries:
1. Find all passengers who paid MORE than the average fare. Show Name, Pclass, Fare. (Subquery in
WHERE calculates the average.)
2. Find the passenger who paid the HIGHEST fare using: WHERE Fare = (SELECT MAX(Fare) FROM
passengers)
3. Find all passengers OLDER than the average age. Show Name, Age. Exclude NULLs.
What is the average fare? What is the average age? Write both as comments.
*/
-- Begin your work here
-- Query 1
SELECT Name, Pclass, Fare
FROM passengers
WHERE Fare > (SELECT AVG(Fare) FROM passengers);

-- Query 2
SELECT *
FROM passengers
WHERE Fare = (SELECT MAX(Fare) FROM passengers);

-- Query 3
SELECT Name, Age
FROM passengers
WHERE Age IS NOT NULL AND Age > (SELECT AVG(Age) FROM passengers);

-- Average Fare = 21.203
-- Average Age = 27.208
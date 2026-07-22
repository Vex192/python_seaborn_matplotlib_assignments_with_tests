-- Task 1
/*
Write THREE queries using subqueries:
1. Find all passengers who paid MORE than the average fare
Show: Name, Pclass, Sex, Fare
Sort by Fare descending
Write the average fare as a comment
2. Find the passenger who paid the HIGHEST fare
Use a subquery:
WHERE Fare = (SELECT MAX(Fare) FROM passengers)
Show all columns for that passenger
3. Find all passengers OLDER than the average age
Exclude passengers where Age is NULL
Show: Name, Age, Pclass, Survived
Sort by Age descending
Write: how many passengers are older than average? (as a comment)
*/
-- Query 1
SELECT Name, Pclass, Sex, Fare
FROM passengers
WHERE Fare > (SELECT AVG(Fare) AS AverageFare FROM passengers)
ORDER BY Fare DESC;

-- Query 2
SELECT *
FROM passengers
WHERE Fare = (SELECT MAX(Fare) AS HighestFare FROM passengers);

-- Query 3
SELECT Name, Age, Pclass, Survived
FROM passengers
WHERE Age IS NOT NULL AND
      Age > (SELECT AVG(Age) AS AverageAge FROM passengers)
ORDER BY Age DESC;
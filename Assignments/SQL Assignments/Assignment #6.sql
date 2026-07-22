-- Assignment #6
-- Task
/*
Write FOUR queries:
1. Count passengers by Pclass
2. Count survivors (Survived=1) and non-survivors (Survived=0)
3. Count passengers by Sex
4. Count passengers by Embarked port — which port had most?
Which class had the most passengers? Write as a comment.
*/
-- Begin your work here
-- Query 1
SELECT Pclass, COUNT(*) AS TotalPassengers
FROM passengers
GROUP BY Pclass;

-- Query 2
SELECT Survived, COUNT(*) AS Count
FROM passengers
GROUP BY Survived;

-- Query 3
SELECT Sex, COUNT(*) AS TotalPassengers
FROM passengers
GROUP BY Sex;

-- Query 4
SELECT Embarked, COUNT(*) AS TotalPassengers
FROM passengers
GROUP BY Embarked
ORDER BY Embarked DESC;
-- Embarked = S had the most passengers
-- 3rd Class (Pclass 3) had the most passengers

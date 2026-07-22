-- Assignment #4
-- Task
/*
Write THREE queries:
1. Show Name, Fare, and FareInPounds = Fare × 0.80 rounded to 2 decimals
2. Show Name, SibSp, Parch, and FamilySize = SibSp + Parch + 1
3. Show Name, Age, and AgeDecade = Age / 10 rounded to 0 decimals
How many passengers traveled alone (FamilySize = 1)? Write as a comment.
*/
-- Begin your work here
-- Query 1
SELECT Name, Fare, ROUND(Fare * 0.80, 2) AS FareInPounds
FROM passengers;

-- Query 2
SELECT Name, Sibsp, Parch, (Sibsp + Parch + 1) AS FamilySize
FROM passengers; 

-- Query 3
SELECT Name, Age, ROUND(Age / 10, 0) AS AgeDecade
FROM passengers;
-- 17 people have FamilySize = 1

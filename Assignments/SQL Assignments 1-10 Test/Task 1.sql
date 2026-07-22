-- Task 1
/*
Write FOUR queries on the passengers table:
1. Find all female passengers
Show: Name, Sex, Pclass, Survived
2. Find all passengers in 1st Class who SURVIVED
Show: Name, Pclass, Survived, Fare
3. Find male passengers in 3rd Class who did NOT survive
Show: Name, Sex, Pclass, Survived
4. Find all passengers who embarked from "C" OR "Q"
Show: Name, Embarked, Pclass
Sort by Embarked, then by Name
For each query — write how many rows you got as a comment.
*/
-- Begin your work here
-- Query 1
SELECT Name, Sex, Pclass, Survived
FROM passengers
WHERE Sex = 'female';
-- 16 Rows

-- Query 2
SELECT Name, Pclass, Survived, Fare
FROM passengers
WHERE Pclass = 1 AND Survived = 1;
-- 4 Rows

-- Query 3
SELECT Name, Sex, Pclass, Survived
FROM passengers
WHERE Pclass = 3 AND Sex = 'male' AND Survived = 0;
-- 9 Rows

-- Query 4
SELECT Name, Embarked, Pclass
FROM passengers
WHERE Embarked = 'C' OR 'Q'
ORDER BY Embarked, Name;
-- 3 Rows
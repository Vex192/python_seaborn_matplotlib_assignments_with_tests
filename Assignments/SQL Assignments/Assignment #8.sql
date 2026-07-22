-- Assignment #8
-- Task
/*
Write FOUR queries:
1. Survival RATE by Pclass: AVG(Survived) × 100, round to 1 decimal
2. Survival RATE by Sex — which sex survived more?
3. Average Age, average Fare, and survival rate all grouped by Pclass
4. Survival rate by Embarked port
"Women and children first" — does the data prove this? Write your answer as a comment.
*/
-- Begin your work here
-- Query 1
SELECT Pclass, ROUND(AVG(Survived) * 100, 1) AS SurvivalRate
FROM passengers
GROUP BY Pclass;

-- Query 2
SELECT Sex, ROUND(AVG(Survived) * 100, 1) AS SurvivalRate
FROM passengers
GROUP BY Sex;

-- Query 3
SELECT Pclass, ROUND(AVG(Age), 2) AS AverageAge,
       ROUND(AVG(Fare), 2) AS AverageFare,
       ROUND(AVG(Survived) * 100, 1) AS SurvivalRate
FROM passengers
GROUP BY Pclass;

-- Query 4
SELECT Embarked, ROUND(AVG(Survived) * 100, 1) AS SurvivalRate
FROM passengers
GROUP BY Embarked;
-- female survived the most
-- data proves women and children first

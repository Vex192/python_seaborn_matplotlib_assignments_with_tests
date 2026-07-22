-- Assignment #17
-- Task
/*
Write TWO complete analysis queries:
1. Group by Pclass AND Sex together. Show: Pclass, Sex, count of passengers, survival rate (%),
average Age, average Fare. Sort by Pclass, then survival rate descending.
2. Group by Embarked port. Show: Embarked, count of passengers, survival rate, average Fare. Sort by
survival rate descending.
Which combination of Pclass and Sex had the highest survival rate? Write as a comment.
*/
-- Begin your work here
-- Query 1
SELECT Pclass, Sex, 
       COUNT(*) AS PassengerCount,
       ROUND(AVG(Survived) * 100, 2) AS SurvivalRate,
       ROUND(AVG(Age), 2) AS AverageAge,
       ROUND(AVG(Fare), 2) AS AverageFare
FROM passengers
GROUP BY Pclass, Sex
ORDER BY Pclass, SurvivalRate DESC;

-- Query 2
SELECT Embarked,
       COUNT(*) AS PassengerCount,
       ROUND(AVG(Survived) * 100, 2) AS SurvivalRate,
       ROUND(AVG(Fare), 2) AS AverageFare
FROM passengers
GROUP BY Embarked
ORDER BY SurvivalRate DESC;

/*
Combination of female in Pclass 1 and in Pclass 2
has highest survival rate
*/

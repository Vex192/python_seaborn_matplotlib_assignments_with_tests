-- Assignment #9
-- Task
/*
Write THREE queries:
1. Group by Pclass — show only classes where average Fare is above 20. Use HAVING.
2. Group by Embarked port — show only ports with more than 5 passengers. Use HAVING COUNT(*) > 5.
3. Group by Sex — show only the sex with survival rate above 50%. Use HAVING AVG(Survived) > 0.5.
Explain in a comment: why can you NOT use WHERE instead of HAVING here?
*/
-- Begin your work here
-- Query 1
SELECT Pclass, 
       ROUND(AVG(Fare), 2) AS AverageFare
FROM passengers
GROUP BY Pclass
HAVING AVG(FARE) > 20;

-- Query 2
SELECT Embarked,
       COUNT(*) AS PassengerCount
FROM passengers
GROUP BY Embarked
HAVING COUNT(*) > 5;

-- Query 3
SELECT Sex,
       ROUND(AVG(Survived) * 100, 2) AS SurvivalRate
FROM passengers
GROUP BY Sex
HAVING SurvivalRate > 50;
-- Becuase you can't use aggregate functions like AVG() and SUM() with where
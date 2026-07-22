-- Task 2
/*
Write FOUR queries:
1. Find survival RATE by Pclass
Formula: AVG(Survived) × 100
Round to 1 decimal place
Sort by survival rate descending
2. Find survival RATE by Sex
Which sex had higher survival rate?
Write the answer as a comment
3. Group by Pclass — show ALL of these together:
• Average Age
• Average Fare
• Survival rate %
• Count of passengers
Sort by Pclass ascending
4. Find survival rate by Embarked port
Which port had the highest survival rate?
Write the answer as a comment
*/
-- Begin your work here
-- Query 1
SELECT Pclass, ROUND(AVG(Survived) * 100, 1) AS SurvivalRate
FROM passengers
GROUP BY Pclass
ORDER BY SurvivalRate DESC;

-- Query 2
SELECT Sex, ROUND(AVG(Survived) * 100, 2) AS SurvivalRate
FROM passengers
GROUP BY Sex;

-- Query 3
SELECT Pclass, COUNT(*) AS PassengerCount,
       ROUND(AVG(Age), 2) AS AverageAge,
       ROUND(AVG(Fare), 2) AS AverageFare,
       ROUND(AVG(Survived) * 100, 2) AS SurvivalRate
FROM passengers
GROUP BY Pclass
ORDER BY Pclass ASC;

-- Query 4
SELECT Embarked, ROUND(AVG(Survived) * 100, 2) AS SurvivalRate
FROM passengers
GROUP BY Embarked;
-- female had the highest survival rate
-- port c had the most survival rate
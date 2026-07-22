-- Assignment #19
-- Task
/*
Write ONE complete report query showing:
1. Name, Sex, Age (COALESCE with 0 for NULLs), Pclass
2. TicketClass: First Class / Second Class / Third Class
3. SurvivalStatus: Survived / Did Not Survive
4. FamilySize = SibSp + Parch + 1
5. FareCategory: Expensive (>50) / Moderate (>20) / Cheap (<=20)
6. FareRank = RANK() OVER (PARTITION BY Pclass ORDER BY Fare DESC)
7. Sort by Pclass ascending, then Fare descending
Then write a SUMMARY query: group by Pclass and Sex — show count, survival rate %, average Fare,
average Age.
*/
-- Begin your work here
-- Query 1
WITH QueryReport AS (
    SELECT Name, Sex, 
           COALESCE(Age, 0) AS Age,
           Pclass, Fare,
           (SibSp + Parch + 1) AS FamilySize,
           CASE
               WHEN Pclass = 1 THEN 'First Class'
               WHEN Pclass = 2 THEN 'Second Class'
               WHEN Pclass = 3 THEN 'Third Class'
               ELSE 'Unknown'
           END AS TicketClass,
           CASE
               WHEN Survived = 1 THEN 'Survived'
               WHEN Survived = 0 THEN 'Did Not Survive'
               ELSE 'Unknown'
           END AS SurvivalStatus,
           CASE
               WHEN Fare > 50 THEN 'Expensive'
               WHEN Fare > 20 THEN 'Moderate'
               WHEN Fare <= 20 THEN 'Cheap'
               ELSE 'Unknown'
           END AS FareCategory,
           RANK() OVER (PARTITION BY Pclass ORDER BY Fare DESC) AS FareRank
    FROM passengers
)
SELECT Name, Sex, Pclass, Age, Fare, TicketClass,
       SurvivalStatus, FamilySize, FareCategory, FareRank
FROM QueryReport
ORDER BY Pclass ASC, Fare DESC;

-- Query 2
SELECT Pclass, Sex,
       COUNT(*) AS PassengerCount,
       ROUND(AVG(Survived) * 100, 2) AS SurvivalRate,
       ROUND(AVG(Fare), 2) AS AverageFare,
       ROUND(AVG(Age), 2) AS AverageAge
FROM passengers
GROUP BY Pclass, Sex;

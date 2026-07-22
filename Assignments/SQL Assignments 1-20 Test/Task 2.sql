-- Task 2
/*
Write TWO queries using WITH (CTE):
Query 1:
Step 1 — CTE: Calculate for each Pclass:
• Average Fare (as AvgFare)
• Survival rate % = AVG(Survived) × 100 (as SurvivalRate)
• Total passengers (as TotalPassengers)
Step 2 — SELECT from that CTE:
Show: Pclass, AvgFare, SurvivalRate, TotalPassengers
Sort by SurvivalRate descending
Query 2:
Step 1 — CTE: Add FamilySize = SibSp + Parch + 1
for every passenger
Step 2 — Group by FamilySize:
Show: FamilySize, count of passengers, survival rate %
Sort by survival rate descending
Write one comment: do larger families survive more or less?
*/
-- Query 1
WITH PclassStats AS (
    SELECT Pclass,
           ROUND(AVG(Fare), 2) AS AvgFare,
           ROUND(AVG(Survived) * 100, 2) AS SurvivalRate,
           COUNT(*) AS TotalPassengers
    FROM passengers
    GROUP BY Pclass
)
SELECT Pclass, AvgFare, SurvivalRate, TotalPassengers
FROM PclassStats
ORDER BY SurvivalRate DESC;

-- Query 2
WITH FamilyStats AS (
    SELECT *,
           (SibSp + Parch + 1) AS FamilySize,
           ROUND(AVG(Survived) * 100, 2) AS SurvivalRate,
           COUNT(*) AS PassengerCount
    FROM passengers
    GROUP BY FamilySize
)
SELECT FamilySize, SurvivalRate, PassengerCount
FROM FamilyStats
ORDER BY SurvivalRate DESC;
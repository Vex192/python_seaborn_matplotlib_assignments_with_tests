-- Assignment #16
-- Task
/*
Write TWO queries using WITH (CTE):
1. CTE: Calculate average Fare and survival rate per Pclass. Then SELECT from that CTE and show all
three classes with their stats. Sort by survival rate descending.
2. CTE: Add FamilySize = SibSp + Parch + 1 for every passenger. Then group by FamilySize — show
count and survival rate per family size. Sort by survival rate descending.
Do larger families survive more or less? Write your finding as a comment.
*/
-- Begin your work here
WITH PclassStats AS (
    SELECT Pclass,
           ROUND(AVG(Fare), 2) AS AverageFare,
           ROUND(AVG(Survived) * 100, 2) AS SurvivalRate
    FROM passengers
    GROUP BY Pclass
)
SELECT Pclass, AverageFare, SurvivalRate
FROM PclassStats
ORDER BY SurvivalRate DESC;

-- Query 2
WITH FamilyStats AS (
    SELECT *,
           SibSp + Parch + 1 AS FamilySize,
           Survived
    FROM passengers
)
SELECT FamilySize,
       COUNT(*) AS PassengerCount,
       ROUND(AVG(Survived) * 100, 2) AS SurvivalRate
FROM FamilyStats
GROUP BY FamilySize
ORDER BY SurvivalRate DESC;

-- Larger families tended to survive less often than smaller families.

-- Assignment #20
-- Task
/*
Write ONE advanced query:
• Show only SURVIVORS (Survived = 1)
• Show: Name, Sex, Age, Pclass, Fare, FamilySize = SibSp+Parch+1
• Add SurvivalRankInClass = RANK() OVER (PARTITION BY Pclass ORDER BY Fare DESC)
• Add RunningFare = SUM(Fare) OVER (ORDER BY Pclass, Fare DESC)
• Add AgeGroup: Child (<18), Adult (<60), Senior (>=60) — use COALESCE for NULLs
• Sort by Pclass, then Fare descending
Then write a CTE-based summary:
• CTE: Add FamilySize to all passengers
• Final: Group by Pclass, Sex — show count, survivors, survival rate
• Sort by survival rate descending
Write 3 conclusions as comments: What made the difference between surviving and not surviving?
*/
-- Begin your work here
-- Query 1
SELECT Name, Sex, COALESCE(Age, 'Unknown') AS Age, Pclass, Fare, 
        (SibSp + Parch + 1) AS FamilySize,
        RANK() OVER (PARTITION BY Pclass ORDER BY Fare DESC) AS SurvivalRankInClass,
        SUM(Fare) OVER (ORDER BY Pclass, Fare DESC) AS RunningFare,
        CASE
            WHEN Age < 18 THEN 'Child'
            WHEN Age < 60 THEN 'Adult'
            WHEN Age >= 60 THEN 'Senior'
            ELSE 'Unknown'
        END AS AgeGroup
FROM passengers
WHERE Survived = 1
ORDER BY Pclass, Fare DESC;

-- Query 2
WITH CTESummary AS (
    SELECT *, 
           (SibSp + Parch + 1) AS FamilySize 
    FROM passengers
)
SELECT Pclass, Sex,
       COUNT(*) AS PassengerCount,
       SUM(Survived) AS Survivers,
       ROUND(AVG(Survived) * 100, 2) AS SurvivalRate
FROM CTESummary
GROUP BY Pclass, Sex
ORDER BY SurvivalRate DESC;

-- Higher class and female passengers survived more often.
-- Younger passengers had better odds than older ones.
-- Smaller families and lower fares were less likely to survive.

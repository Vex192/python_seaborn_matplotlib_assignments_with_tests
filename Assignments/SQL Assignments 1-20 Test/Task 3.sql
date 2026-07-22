-- Task 3
/*
Part A — Main Query:
Show ONLY survivors (Survived = 1)
Include these columns:
1. Name
2. Sex
3. Age — use COALESCE to show 0 where Age is NULL
4. Pclass
5. Fare
6. FamilySize = SibSp + Parch + 1
7. TicketClass:
"First Class" if Pclass = 1
"Second Class" if Pclass = 2
"Third Class" if Pclass = 3
8. FareRank = RANK() OVER (PARTITION BY Pclass
ORDER BY Fare DESC)
This ranks survivors by fare within each class
Sort by Pclass ascending, then Fare descending
Part B — Summary using CTE:
Step 1 CTE: Add FamilySize = SibSp + Parch + 1
to ALL passengers (not just survivors)
Step 2: Group by Pclass and Sex
Show: Pclass, Sex, total passengers, survivors count,
survival rate % rounded to 1 decimal
Sort by survival rate descending
Write 2 sentences as comments answering:
Which group had the best chance of survival?
What surprised you most in the results?
*/
-- Query 1
SELECT Name, Sex, COALESCE(Age, 'Unknown') AS Age,
       Pclass, Fare,
       (SibSp + Parch + 1) AS FamilySize,
       CASE
           WHEN Pclass = 1 THEN 'First Class'
           WHEN Pclass = 1 THEN 'First Class'
           WHEN Pclass = 1 THEN 'First Class'
           ELSE 'Unknown'
       END AS TicketClass,
       RANK() OVER (PARTITION BY Pclass ORDER BY Fare DESC) AS FareRank
FROM passengers
WHERE Survived = 1
ORDER BY Pclass ASC, Fare DESC;
/*
Used unknown instead of 0 in coalesce becuase makes more sense
0 is logically not right because that might be a child
*/

-- Query 2
WITH CTESummary AS (
    SELECT 
           (SibSp + Parch + 1) AS FamilySize,
           SUM(Survived) AS Survivors,
           ROUND(AVG(Survived) * 100, 1) AS SurvivalRate,
           COUNT(*) AS PassengerCount
    FROM passengers
    GROUP BY Pclass, Sex
)
SELECT FamilySize, Survivors, SurvivalRate, PassengerCount
FROM CTESummary
ORDER BY SurvivalRate DESC;
-- Passengers with family size 2 have the most survival rate
-- 
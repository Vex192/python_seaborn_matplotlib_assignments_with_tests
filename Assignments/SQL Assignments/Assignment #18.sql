-- Assignment #18
-- Task
/*
IMPORTANT: Before every UPDATE — write a SELECT first to preview what will change.
1. INSERT a new passenger: PassengerId=31, Survived=1, Pclass=1, Name="Dr. Sajjad Shaukat",
Sex="male", Age=40, SibSp=0, Parch=0, Fare=100.00, Embarked="S"
2. UPDATE the Fare for PassengerId=1 from 7.25 to 8.00
3. UPDATE all 3rd Class passengers — increase Fare by 5% (Fare = Fare × 1.05)
4. After each change — run SELECT to confirm it worked
How many total passengers are now in the table after INSERT? Write as a comment.
*/
-- Begin your work here
-- Query 1
INSERT INTO passengers (PassengerID, Survived, Pclass, Name, Sex, 
                        Age, Sibsp, Parch, Fare, Embarked)
VALUES (31, 1, 1, 'Dr. Sajjad Shaukat', 'male', 40, 0, 0, 100.00, 'S');

SELECT *
FROM passengers;

-- Query 2
UPDATE passengers
SET Fare = 8.00
WHERE PassengerID = 1;

SELECT *
FROM passengers;

-- Query 3
UPDATE passengers
SET Fare = ROUND(Fare * 1.05, 2)
WHERE Pclass = 3;

SELECT *
FROM passengers;

-- Current total passengers = 31

# Write your MySQL query statement below
Select Max(salary) as SecondHighestSalary 
From Employee where salary <> (Select Max(salary) from Employee);
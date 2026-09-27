# Write your MySQL query statement below
Update Salary
set sex = Case
when sex = 'm' then 'f'
when sex = 'f' then 'm'
END;
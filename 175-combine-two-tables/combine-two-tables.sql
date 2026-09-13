# Write your MySQL query statement below
Select firstName, lastName, city, state
From Person left outer join Address
on Person.personId = Address.personId
# Write your MySQL query statement below
select product_name, year, price 
from Sales s
Inner Join Product p
on s.product_id = p.product_id
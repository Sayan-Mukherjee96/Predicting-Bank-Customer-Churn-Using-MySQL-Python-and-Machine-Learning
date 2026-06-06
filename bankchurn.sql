use bank;

create table bankchurn(
CustomerId Integer,
SurName char(100),
CreditScore Integer,
Country char(10),
Gender char(10),
Age Integer,
Tenure integer,
Balance Integer,
NumOfProducts Integer,
HasCrCard Integer,
ActiveMember Integer,
Salary Integer,
Exited Integer
);

select * from bankchurn;

/*Display customer details where Age is greater than 50*/

select SurName, Age, Gender, CreditScore
from bankchurn
where Age > '50'
order by Age desc;

/*Retrieve customers having a balance greater than 100000.*/

select CustomerId, SurName, Balance
from bankchurn
having Balance > '100000'
order by Balance desc;

/*Find female customers from Germany who churned.*/

select CustomerId, SurName
from bankchurn
where Gender = 'Female' and Country = 'Germany' and Exited = 1;

/*Retrieve active customers with more than 2 products.*/

SELECT CustomerId, Surname, NumOfProducts
FROM bankchurn
WHERE ActiveMember = 1 AND NumOfProducts > 2;

/*Find customers with zero balance who exited the bank.*/

select CustomerId, Surname, Balance
from bankchurn
where Balance = 0 and Exited = 1;

/*Calculate the average balance of customers by Country.*/

select round(avg(Balance),1) as AvgBalance, Country
from bankchurn
group by Country;

/*Calculate the average credit score of Active customers.*/

select round(avg(CreditScore),1) as Avg_credit_score
from bankchurn
where ActiveMember = 1
group by ActiveMember;

/*Find the average estimated salary by geography.*/

select round(avg(Salary),1) as Avg_Salary, Country
from bankchurn
group by Country;

/*Find the number of active and inactive customers.*/

select count(ActiveMember) as Total_Member, ActiveMember
from bankchurn
group by ActiveMember;






































































































































































































































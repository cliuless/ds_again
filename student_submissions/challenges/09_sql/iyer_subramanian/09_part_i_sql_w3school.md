# Challenge Set 9
## Part I: W3Schools SQL Lab 

*Introductory level SQL*

--

This challenge uses the [W3Schools SQL playground](http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all). Please add solutions to this markdown file and submit.

1. Which customers are from the UK?
IDs: 4,11,16,19,39,53,72
Names: Around the Horn, B's Beverages, Consolidated Holdings, Eastern Connection, Island Trading, North/South, Seven Seas Imports

2. What is the name of the customer who has the most orders?
Ernst Handel

3. Which supplier has the highest average product price?
Aux joyeux ecclésiastiques

4. How many different countries are all the customers from? (*Hint:* consider [DISTINCT](http://www.w3schools.com/sql/sql_distinct.asp).)
21

5. What category appears in the most orders?
Dairy Products

6. What was the total cost for each order?
Select *, SUM(a.Price*a.Quantity) p from(Select * from Products join OrderDetails on Products.ProductID=OrderDetails.ProductID) a group by a.OrderID order by p desc
7. Which employee made the most sales (by total price)?
Laura Callahan
8. Which employees have BS degrees? (*Hint:* look at the [LIKE](http://www.w3schools.com/sql/sql_like.asp) operator.)
Janet Leverling and Steven Buchanan
9. Which supplier of three or more products has the highest average product price? (*Hint:* look at the [HAVING](http://www.w3schools.com/sql/sql_having.asp) operator.)
Tokyo Traders
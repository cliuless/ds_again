# Challenge Set 9
## Part I: W3Schools SQL Lab 

*Introductory level SQL*

--

This challenge uses the [W3Schools SQL playground](http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all). Please add solutions to this markdown file and submit.

1. Which customers are from the UK?
```
SELECT CustomerName FROM Customers WHERE Country = 'UK';
```
| CustomerName        |
|---------------------|
Around the Horn      
B's Beverages        
Consolidated Holdings
Eastern Conn
ection   
Island Trading      
North/South         
Seven Seas Imports


2. What is the name of the customer who has the most orders?
```
SELECT CustomerName
FROM Customers INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID 
GROUP BY CustomerName
ORDER BY count(TotalOrders) DESC
LIMIT 1
```
|CustomerName|
|---|
Ernst Handle

3. Which supplier has the highest average product price?
```
SELECT SupplierName
FROM Suppliers INNER JOIN Products ON Suppliers.SupplierID = Products.ProductID
GROUP BY SupplierName
ORDER BY avg(Products.Price) DESC
LIMIT 1
```

|SupplierName|
|---|
Forêts d'érables


4. How many different countries are all the customers from? (*Hint:* consider [DISTINCT](http://www.w3schools.com/sql/sql_distinct.asp).)
```
SELECT count(Country) AS DifferentCounties
FROM(
    SELECT DISTINCT Country
    FROM Customers
)
```

|DifferentCounties|
|---|
21

5. What category appears in the most orders?
```
SELECT CategoryName
FROM(
  SELECT CategoryName, Products.ProductID, OrderID
  FROM (Products INNER JOIN Categories ON Products.CategoryID = Categories.CategoryID) 
          INNER JOIN OrderDetails ON Products.ProductID = OrderDetails.ProductID
  GROUP BY CategoryName, OrderID
)
GROUP BY CategoryName
ORDER BY count(OrderID) desc
LIMIT 1
```

|CategoryName|
|---|
Beverages

6. What was the total cost for each order?
```
SELECT OrderID, sum(Quantity * Price) as OrderPrice
FROM OrderDetails INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID
GROUP BY OrderID
```

|OrderID|OrderPrice|
|---|---|
10248|566
10249|2329.25
10250|2267.25
10251|839.5
etc|...

7. Which employee made the most sales (by total price)?
```
SELECT FirstName, LastName
FROM ((
  SELECT OrderID, sum(Quantity * Price) as OrderPrice
  FROM OrderDetails INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID
  GROUP BY OrderID
 ) AS A INNER JOIN Orders on A.OrderID = Orders.OrderID
 ) INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
GROUP BY Employees.EmployeeID
Order BY sum(A.OrderPrice) DESC
LIMIT 1
```

|FirstName|LastName|
|---|---|
Margaret|Peacock

8. Which employees have BS degrees? (*Hint:* look at the [LIKE](http://www.w3schools.com/sql/sql_like.asp) operator.)
```
SELECT FirstName, LastName
FROM Employees
WHERE Notes LIKE '%BS%'
```

|FirstName|LastName|
|---|---|
Janet|Leverling
Steven|Buchanan

9. Which supplier of three or more products has the highest average product price? (*Hint:* look at the [HAVING](http://www.w3schools.com/sql/sql_having.asp) operator.)
```
SELECT SupplierName
FROM Suppliers INNER JOIN Products on Suppliers.SupplierID = Products.SupplierID
GROUP BY SupplierName
HAVING count(Products.ProductID) >=3
ORDER BY avg(Products.Price) DESC
LIMIT 1
```
|SupplierName|
|---|
Tokyo|







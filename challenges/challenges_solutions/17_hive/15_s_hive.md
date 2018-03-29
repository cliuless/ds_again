#### Set 15:  Hive Challenges Solutions  
Date:  3/21/2016  
By:  Julia  

---

**Challenge 1**

Upload the AllstarFull, Appearences, Teams and Batting tables to Hive.

- Move data  into HDFS

```bash
tail -n +2 baseballdata/AllstarFull.csv > tmp && mv tmp baseballdata/AllstarFull.csv

hdfs dfs -put baseballdata/AllstarFull.csv /user/username/baseballdata

tail -n +2 baseballdata/Appearances.csv > tmp && mv tmp baseballdata/Appearances.csv

hdfs dfs -put baseballdata/Appearances.csv /user/username/baseballdata

tail -n +2 baseballdata/Teams.csv > tmp && mv tmp baseballdata/TeamsF.csv

hdfs dfs -put baseballdata/Teams.csv /user/username/baseballdata

tail -n +2 baseballdata/Batting.csv > tmp && mv tmp baseballdata/Batting.csv

hdfs dfs -put baseballdata/Batting.csv /user/username/baseballdata

```

Add AllstarFull table into hive:


```hive
CREATE TABLE IF NOT EXISTS AllStarFull
      (playerID STRING,
      yearID INT,
      gameNum INT,
      gameID STRING,
      teamID STRING,
      lgID STRING,
      GP INT,
      startingPos INT)
      COMMENT 'Salary Table for AllStars'
      ROW FORMAT DELIMITED
      FIELDS TERMINATED BY ','
      STORED AS TEXTFILE;
```
 
```hive 
LOAD DATA INPATH '/user/username/baseballdata/AllstarFull.csv' OVERWRITE INTO TABLE AllstarFull;
``` 

Add Appearances into hive:

```hive
CREATE TABLE IF NOT EXISTS Appearances
      (yearID INT,
      teamID STRING,
      lgID STRING,
      playerID STRING,
      G_all INT,
      GS INT,
      G_batting INT,
      G_defense INT,
      G_p INT,
      G_c INT, 
      G_1b INT,
      G_2b INT,
      G_3b INT,
      G_ss INT,
      G_1f INT,
      G_cf INT,
      G_rf INT,
      G_of INT,
      G_dh INT,
      G_ph INT,
      G_pr INT)
      COMMENT 'Salary Table for Appearances'
      ROW FORMAT DELIMITED
      FIELDS TERMINATED BY ','
      STORED AS TEXTFILE;

LOAD DATA INPATH '/user/username/baseballdata/Appearances.csv' OVERWRITE INTO TABLE Appearances;
```


Add Teams table into hive:

```hive
CREATE TABLE IF NOT EXISTS Teams
      (yearID INT,
      lgID STRING,
      teamID STRING,
      franchID STRING)
      COMMENT 'Salary Table for team'
      ROW FORMAT DELIMITED
      FIELDS TERMINATED BY ','
      STORED AS TEXTFILE;
```

```hive 
LOAD DATA INPATH '/user/username/baseballdata/Teams.csv' OVERWRITE INTO TABLE Teams;
``` 

Add Batting table into hive:

```hive
CREATE TABLE IF NOT EXISTS Batting
      (playerID STRING,
      yearID INT,
      stint INT,
      teamID STRING,
      lgID STRING,
      G INT,
      G_batting INT,
      AB INT,
      R INT,
      H INT,
      H2B INT,
      H3B INT,
      HR INT,
      RBI INT,
      SB INT,
      CS INT,
      BB INT,
      SO INT,
      IBB INT,
      HBP INT,
      SH INT,
      SF INT,
      GIDP INT,
      G_old INT)
      COMMENT 'Table for Batting'
      ROW FORMAT DELIMITED
      FIELDS TERMINATED BY ','
      STORED AS TEXTFILE;

```
```hive 
LOAD DATA INPATH '/user/username/baseballdata/Batting.csv' OVERWRITE INTO TABLE Batting;
``` 

Confirm all tables have been imported:  

```hive 
show tables;
``` 

**Challenge 2**

For each year (after 1985), calculate the average salary of all players that year:
(note: as per second part of the challenge instructions, we also want to put our output into HDFS as per the 
following command)


```hive 
INSERT OVERWRITE DIRECTORY '/user/username/output1' select avg(salary),yearID from salaries where yearID > 1985 group by yearID order by yearID;  

OK
3723344.353374233	2013
3458421.216981132	2012
3318838.249106079	2011
3278746.825301205	2010
3277646.979089791	2009

```

Then for each year, calculate the average salary of all star players. Save these outputs in two files in HDFS. To record query results into a file, you can do INSERT OVERWRITE DIRECTORY '/path/to/output/dir' SELECT ........; (The ...... after SELECT is whatever your query is, and the '/path/to/output/dir' is where you want the output to go in hdfs).



```hive 

INSERT OVERWRITE DIRECTORY '/user/username/output2' select avg(salary),salaries.yearID from salaries join allstarfull on allstarfull.playerID= salaries.playerID group by salaries.yearID;


OK
790792.9628008753	1985
796762.1513671875	1986
840707.0230769231	1987
910291.6354733406	1988
1032258.8349410504	1989
1117323.654736842	1990
1719930.9078947369	1991
2132759.3596311477	1992
2410744.5110047846	1993
2618619.5848303395	1994
2911685.6774193547	1995
2868270.9873046875	1996
3302033.524878049	1997
3560149.888118812	1998
4040800.4771825396	1999
4960555.829831933	2000
5869515.220391349	2001
6322282.337704918	2002
6864536.293736501	2003
6930888.181619256	2004
7544068.468271335	2005
7364523.061403509	2006
7491047.782887701	2007
8375126.798423423	2008
8343213.118581907	2009
8970580.067620287	2010
9426656.482093664	2011
1.0668223734059097E7	2012
1.1541896877442274E7	2013
```


**Challenge 3**

For the years 2000, 2005 and 2010, calculate the average salary of New York Yankees, New York Mets, Chicago Cubs and Chicago White Sox in each of these years. Also calculate the total salary for these teams -- their salary budget.

for Yankees in 2000:
```hive
select salaries.yearid, teams.franchid, avg(salaries.salary) from salaries join teams on salaries.teamid =teams.teamid where teams.franchid in ('NYY','NYM','CHC','CHW') and salaries.yearid in ('2000','2005','2010') group by salaries.yearid, teams.franchid order by salaries.yearid, teams.franchid;

OK
2000	CHC	2017977.7666666666
2000	CHW	1073568.9655172413
2000	NYM	3180391.04
2000	NYY	3297795.0
2005	CHC	3108319.035714286
2005	CHW	2784370.3703703703
2005	NYM	3752067.4444444445
2005	NYY	8011800.653846154
2010	CHC	5429962.962962963
2010	CHW	4058846.153846154
2010	NYM	4800819.357142857
2010	NYY	8253335.56
```

**Challenge 4**

In the history of baseball, who has the record for most home runs in a single year? Who are the top 10 for this statistic?
```hive
select sum(HR) as count,playerid, yearid from batting group by yearid,playerid order by count desc limit 10;

OK
73	bondsba01	2001
70	mcgwima01	1998
66	sosasa01	1998
65	mcgwima01	1999
64	sosasa01	2001
63	sosasa01	1999
61	marisro01	1961
60	ruthba01	1927
59	ruthba01	1921
58	howarry01	2006;
```



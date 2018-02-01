
In this walkthru we will first build some more 
tables in our remote Postgres server.  We will 
then alter some configuration settings so that
we will be able to connect with our remote Postgres server locally (via python & pandas).

First, let's ssh into our cloud.. 

```bash
ssh ubuntu 
# Make sure you are home (/home/username)
pwd

```
Let's get some data to work with via the Lahman baseball data


```bash
wget http://seanlahman.com/files/database/lahman-csv_2014-02-14.zip
sudo apt-get install unzip
mkdir baseballdata
unzip lahman-csv_2014-02-14.zip -d baseballdata
```

(psql)

```sql
CREATE TABLE IF NOT EXISTS AllstarFull (
	playerID varchar(20) NOT NULL,
	yearID int NOT NULL,
	gameNum varchar(20) NOT NULL,
	gameID varchar(12) DEFAULT NULL,
	teamID text DEFAULT NULL,
	lgID text DEFAULT NULL,
	GP varchar(20) DEFAULT NULL,
	startingPos varchar(20) DEFAULT NULL,
	PRIMARY KEY (playerID,yearID,gameNum)
);


COPY AllstarFull FROM '/home/username/baseballdata/AllstarFull.csv' DELIMITER ',' CSV HEADER;


CREATE TABLE IF NOT EXISTS Salaries (
	yearID int NOT NULL,
	teamID varchar(3) NOT NULL,
	lgID varchar(2) NOT NULL,
	playerID varchar(9) NOT NULL,
	salary double precision DEFAULT NULL,
	PRIMARY KEY (yearID,teamID,lgID,playerID)
);

COPY Salaries FROM '/home/username/baseballdata/Salaries.csv' DELIMITER ',' CSV HEADER;


CREATE TABLE IF NOT EXISTS Schools (
	schoolID varchar(15) NOT NULL,
	schoolName varchar(255) DEFAULT NULL,
	schoolCity varchar(55) DEFAULT NULL,
	schoolState varchar(55) DEFAULT NULL,
	schoolNick varchar(55) DEFAULT NULL,
	PRIMARY KEY (schoolID)
);

COPY Schools FROM '/home/username/baseballdata/Schools.csv' DELIMITER ',' CSV HEADER;
```

## Connect to Postgres! 

 We want to connect Postgres with SQL Alchemy and psycopg locally.  Let's do that  


On your EC2: 

```bash
pip install psycopg2   
jupyter notebook
```

# from local (todays directory in repo) 
```bash
scp psycopg_sqlAlchemy.ipynb myaws:~
ssh myaws -NL 12345:localhost:8888 username@##.###.####
```

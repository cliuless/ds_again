# Challenge Set 9: Solutions
## Part IV: Tennis Data

*Intermediate - Advanced level SQL*

---

This challenge uses only SQL queries. Please submit answers in a markdown file.

(1) Using the same tennis data, find the number of matches played by
   each player in each tournament. (Remember that a player can be
   present as both player1 or player2).

For the men:

```sql
WITH _table AS (
  SELECT
      tb.player1 AS player,
      'USOpen' AS tourn
   FROM 
      us_men_2013 AS tb
   UNION ALL
   SELECT 
      tb.player2 AS player,
      'USOpen' AS tourn
   FROM 
      us_men_2013 AS tb   
      
   UNION ALL
   
   SELECT 
      tb.player1 AS player,
      'FrenchOpen' AS tourn
   FROM 
      french_men_2013 AS tb
   UNION ALL
   SELECT 
      tb.player2 AS player,
      'FrenchOpen' AS tourn
   FROM 
      french_men_2013 AS tb

   UNION ALL
   
   SELECT 
      tb.player1 AS player,
      'AusOpen' AS tourn
   FROM 
      aus_men_2013 AS tb
   UNION ALL
   SELECT 
      tb.player2 AS player,
      'AusOpen' AS tourn
   FROM 
      aus_men_2013 AS tb

   UNION ALL
   
   SELECT 
      tb.player1 AS player,
      'Wimbledon' AS tourn
   FROM 
      wimbledon_men_2013 AS tb
   UNION ALL
   SELECT 
      tb.player2 AS player,
      'Wimbledon' AS tourn
   FROM 
      wimbledon_men_2013 AS tb
)
SELECT
   player,
   tourn,
   COUNT(player) AS num_matches
FROM
   _table
GROUP BY player,tourn
ORDER BY player
LIMIT 6;
```

| player | tourn | num_matches |
| ------ | ----- | ----------- |
| A.Bedene | Wimbledon |   1 |
| A.Bogomolov Jr. |   Wimbledon  |  1 |
| A.Dolgopolov |   Wimbledon  |  2 |
| Adrian Mannarino |  FrenchOpen  | 1 |
| Adrian Mannarino |  AusOpen |  2 |
| Adrian Mannarino |  USOpen |   3 |

Repeat the analogous query to get the answer for women:

| player | tourn | num_matches |
| ------ | ----- | ----------- |
| A Barty |  USOpen  |  1 |
| A.Beck |   Wimbledon   | 2 |
| A.Cadantu |   Wimbledon  |  2 |
| A Cornet | USOpen   | 3 |
| A.Cornet | Wimbledon  |  3 |
| A Dulgheru | USOpen   | 2 |

(2) Who has played the most matches total in all of US Open, AUST Open, 
   French Open? Answer this both for men and women.

>Initial setup of male and female players tables.

```sql
CREATE TABLE 
   male_players 
AS SELECT 
   *
FROM 
   us_men_2013;


INSERT INTO 
   male_players
SELECT 
   *
FROM 
   aus_men_2013;


INSERT INTO 
   male_players 
SELECT 
   *
FROM 
   french_men_2013;


CREATE TABLE 
   female_players 
AS SELECT 
   *
FROM 
   us_ladies_2013;


INSERT INTO 
   female_players 
SELECT 
   *
FROM 
   aus_ladies_2013;


INSERT INTO 
   female_players 
SELECT 
   *
FROM 
   french_ladies_2013;
```

For men: 

```sql
WITH _table1 AS (
   SELECT
      tb.player1 AS player
   FROM 
      male_players AS tb
   UNION ALL
   SELECT 
      tb.player2 AS player
   FROM 
      male_players AS tb
)
SELECT 
   player, Count(player) AS num_matches
FROM 
   _table1
GROUP BY 1
ORDER BY 2 DESC
LIMIT 5;
```

| player | num_matches |
| ------ | ----------- |
| Rafael Nadal | 21 |
| Stanislas Wawrinka | 17 |
| Novak Djokovic | 17 |
| David Ferrer | 17 | 
| Roger Federer | 15 |

Repeat the analogous query to get the answer for women:

| player | num_matches |
| ------ | ----------- |
| Maria Sharapova |  11 |
| Serena Williams  | 11 |
| Victoria Azarenka | 11 |
| Agnieszka Radwanska | 11 |
| Ana Ivanovic |  9 |


(3) Who has the highest first serve percentage? (Use the maximum value
   for a single match.)

For men:

```sql
WITH _table AS (
   SELECT 
      tb.player1 AS player, 
      tb.fsp_1 AS fsp
   FROM 
      male_players AS tb
   UNION ALL
   SELECT
      tb.player2 AS player,
      tb.fsp_2 AS fsp
   FROM 
      male_players AS tb
)
SELECT
   *
FROM
   _table
ORDER BY 2 DESC
LIMIT 5;
```

| player | fsp |
| ------ | --- |
| Carlos Berlocq | 84 |
| Gael Monfils  |  84 |
| Rafael Nadal  |  84 |
| Gael Monfils  |  83 |
| Roberto Bautista Agut   | 83 |

Repeat the analogous query to get the answer for women:

| player | fsp |
| ------ | --- |
| S Errani | 93 |
| Sara Errani | 91 |
| Sara Errani | 89 |
| Victoria Azarenka | 88 |
| Sara Errani | 87 |

*Note:* some of the tables have only first initial. How might this change results?

(4) What are the unforced error percentages of the top three players
   with the most wins? (Unforced error percentage is % of points lost
   due to unforced errors. In a match, you have fields for number of
   points won by each player, and number of unforced errors for each
   field.)

For men:

```sql
WITH _table AS (
   SELECT
      tb.player1 AS player,
      tb.ufe_1 AS unforced_errors, 
      tb.tpw_2 AS total_points_lost, 
      CASE
         WHEN tb.result = 1
         THEN 1
         ELSE 0
      END AS wins
   FROM male_players as tb
   
   UNION ALL
   
   SELECT
      tb.player2 AS player,
      tb.ufe_2 AS unforced_errors, 
      tb.tpw_1 AS total_points_lost, 
      CASE
         WHEN tb.result = 0 
         THEN 1
         ELSE 0
      END AS wins
   FROM male_players as tb
)
SELECT
   player,
   SUM(wins) AS wins,
   ( SUM(unforced_errors) * 1.0 / SUM(total_points_lost) ) AS unforced_error_ratio
FROM
   _table
GROUP BY 
   player
ORDER BY 2 DESC
LIMIT 5;
```

| player | wins | unforced_error_ratio |
| ------ | ---- | -------------------- |
| Rafael Nadal |   20 | 0.21193530395984383714 |
| Stanislas Wawrinka |   15 | 0.23819408406850025947 |
| Novak Djokovic | 14 | 0.23461538461538461538 |
| David Ferrer |   14 | 0.21596534653465346535 |
| Roger Federer |  12 | 0.28905597326649958229 |


Repeat the analogous query to get the answer for women:

| player | wins | unforced_error_ratio |
| ------ | ---- | -------------------- |
| Serena Williams  |  10 | 0.43181818181818181818 |
| Agnieszka Radwanska |  9 |  0.27538461538461538462 |
| Victoria Azarenka | 9 |  0.38897396630934150077 |
| Na Li | 8 |  0.49129593810444874275 |
| Maria Sharapova  |  8 |  0.50819672131147540984 |

*Note:* These are somewhat inaccurate becuase the US databases don't have unforced error data. 
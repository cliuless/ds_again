## The challenges!

This challenge uses only SQL queries. Please submit answers in a markdown file.

1. Using the same tennis data, find the number of matches played by
   each player in each tournament. (Remember that a player can be
   present as both player1 or player2).
```
select player, sum(tot_p)
from
    (select player1 as player, count(player1) as tot_p
    from aus_men_2013 
    group by player1

    union all

    select player2 as player, count(player2) as tot_p
    from aus_men_2013 
    group by player2) as play_comb
group by player;
```

2. Who has played the most matches total in all of US Open, AUST Open, 
   French Open? Answer this both for men and women.

This a bunch of times:
```
select player, sum(tot_p) into women_aus_tot
from
    (select player1 as player, count(player1) as tot_p
    from aus_women_2013 
    group by player1

    union all

    select player1 as player, count(player1) as tot_p
    from aus_women_2013 
    group by player1) as play_comb

group by player;
```

Then this twice:
```
select player, sum(sum) as total
from
   (select * from men_aus_tot
   union all
   select * from men_wim_tot
   union all
   select * from men_us_tot
   union all
   select * from men_fr_tot) as union_tot
 group by player
 order by sum(sum) desc
 limit 1;
```

Men - Rafael Nadal: 21

Women - Agnieszka Radwanska: 15

3. Who has the highest first serve percentage? (Just the maximum value
   in a single match.)

Didn't realize we were going to combine all the files constantly - just do this for women and men:
```
select * into all_men
from
(select * from aus_men_2013
   union all
   select * from french_men_2013
   union all
   select * from us_men_2013
   union all
   select * from wim_men_2013) as union_tot;
```

Combine women and men again:
```
select * into all_matches
from(
select * from all_men
union all
select * from all_women) as ugh;
```

Now get the answer:
```
select player, max(fsp) 
from
 (select player1 as player, "fsp.1" as fsp
 from all_matches
 union all
 select player2 as player, "fsp.2" as fsp
 from all_matches
) as men_fsp
group by player
order by max(fsp) desc
limit 1;
```

 S Errani: 93

4. What are the unforced error percentages of the top three players
   with the most wins? (Unforced error percentage is % of points lost
   due to unforced errors. In a match, you have fields for number of
   points won by each player, and number of unforced errors for each
   field.)

Players with the most wins (top3):
```
select player, sum(result) as wins from
 (select player1 as player,  result
 from all_matches
 union all
 select player2 as player, 1 - result
 from all_matches
) as men_fsp
group by player
order by sum(result) desc
limit 3;
```

Going to get complicated here:
```
select ugh2.player, sum(ufe)/sum(tpl) as ufe_per
from
(
select player1 as player, sum("ufe.1") as ufe, sum("tpw.2") as tpl
from all_matches
group by player1
union all
select player2 as player, sum("ufe.2") as ufe, sum("tpw.1") as tpl
from all_matches
group by player2)
as ugh2 inner join
(select player, sum(result) as wins from
 (select player1 as player,  result
 from all_matches
 union all
 select player2 as player, 1 - result
 from all_matches
) as men_fsp
group by player
order by sum(result) desc
limit 3
) as top3
on top3.player = ugh2.player
group by ugh2.player;
```
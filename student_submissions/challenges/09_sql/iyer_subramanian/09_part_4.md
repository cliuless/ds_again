1.:

select concat(g1.player, g2.player) as player, us_men_matches, us_women_matches, aus_men_matches, aus_women_matches, fr_men_matches, fr_women_matches, wimb_men_matches, wimb_women_matches
from 
(select concat(usa.player, aus.player) as player, us_men_matches, us_women_matches, aus_men_matches, aus_women_matches
from
(select
concat(one.player, two.player) as player, us_men_matches, us_women_matches
from
(
(select a.player, sum(a.count) as us_men_matches from (select player1 as player, count(*)from us_men_2013 group by player union all 
select player2 as player, count(*) from us_men_2013 group by player) a group by a.player) one
full outer join 
(select a.player, sum(a.count) as us_women_matches from (select player1 as player, count(*)from us_women_2013 group by player union all select player2 as player, count(*) from us_women_2013 group by player) a group by a.player) two 
on one.player=two.player
)) usa
full outer join
(select
concat(one.player, two.player) as player, aus_men_matches, aus_women_matches
from
(
(select a.player, sum(a.count) as aus_men_matches from (select player1 as player, count(*)from aus_men_2013 group by player union all 
select player2 as player, count(*) from aus_men_2013 group by player) a group by a.player) one
full outer join 
(select a.player, sum(a.count) as aus_women_matches from (select player1 as player, count(*)from aus_ladies_2013 group by player union all select player2 as player, count(*) from aus_ladies_2013 group by player) a group by a.player) two 
on one.player=two.player
)) aus
on usa.player=aus.player) g1
full outer join
(select concat(france.player, wimb.player) as player, fr_men_matches, fr_women_matches, wimb_men_matches, wimb_women_matches
from
(select
concat(one.player, two.player) as player, fr_men_matches, fr_women_matches
from
(
(select a.player, sum(a.count) as fr_men_matches from (select player1 as player, count(*)from french_men_2013 group by player union all 
select player2 as player, count(*) from french_men_2013 group by player) a group by a.player) one
full outer join 
(select a.player, sum(a.count) as fr_women_matches from (select player1 as player, count(*)from french_women_2013 group by player union all select player2 as player, count(*) from french_women_2013 group by player) a group by a.player) two 
on one.player=two.player
)) france
full outer join
(select
concat(one.player, two.player) as player, wimb_men_matches, wimb_women_matches
from
(
(select a.player, sum(a.count) as wimb_men_matches from (select player1 as player, count(*)from wimbledon_men_2013 group by player union all 
select player2 as player, count(*) from wimbledon_men_2013 group by player) a group by a.player) one
full outer join 
(select a.player, sum(a.count) as wimb_women_matches from (select player1 as player, count(*)from wimbledon_women_2013 group by player union all select player2 as player, count(*) from wimbledon_women_2013 group by player) a group by a.player) two 
on one.player=two.player
)) wimb
on france.player=wimb.player) g2
on g1.player = g2.player;

2. For men: Rafael Nadal:

select player, total_men_matches from
(select player, us_men_matches as total_men_matches from
(select concat(g1.player, g2.player) as player, us_men_matches, us_women_matches, aus_men_matches, aus_women_matches, fr_men_matches, fr_women_matches, wimb_men_matches, wimb_women_matches
from 
(select concat(usa.player, aus.player) as player, us_men_matches, us_women_matches, aus_men_matches, aus_women_matches
from
(select
concat(one.player, two.player) as player, us_men_matches, us_women_matches
from
(
(select a.player, sum(a.count) as us_men_matches from (select player1 as player, count(*)from us_men_2013 group by player union all 
select player2 as player, count(*) from us_men_2013 group by player) a group by a.player) one
full outer join 
(select a.player, sum(a.count) as us_women_matches from (select player1 as player, count(*)from us_women_2013 group by player union all select player2 as player, count(*) from us_women_2013 group by player) a group by a.player) two 
on one.player=two.player
)) usa
full outer join
(select
concat(one.player, two.player) as player, aus_men_matches, aus_women_matches
from
(
(select a.player, sum(a.count) as aus_men_matches from (select player1 as player, count(*)from aus_men_2013 group by player union all 
select player2 as player, count(*) from aus_men_2013 group by player) a group by a.player) one
full outer join 
(select a.player, sum(a.count) as aus_women_matches from (select player1 as player, count(*)from aus_ladies_2013 group by player union all select player2 as player, count(*) from aus_ladies_2013 group by player) a group by a.player) two 
on one.player=two.player
)) aus
on usa.player=aus.player) g1
full outer join
(select concat(france.player, wimb.player) as player, fr_men_matches, fr_women_matches, wimb_men_matches, wimb_women_matches
from
(select
concat(one.player, two.player) as player, fr_men_matches, fr_women_matches
from
(
(select a.player, sum(a.count) as fr_men_matches from (select player1 as player, count(*)from french_men_2013 group by player union all 
select player2 as player, count(*) from french_men_2013 group by player) a group by a.player) one
full outer join 
(select a.player, sum(a.count) as fr_women_matches from (select player1 as player, count(*)from french_women_2013 group by player union all select player2 as player, count(*) from french_women_2013 group by player) a group by a.player) two 
on one.player=two.player
)) france
full outer join
(select
concat(one.player, two.player) as player, wimb_men_matches, wimb_women_matches
from
(
(select a.player, sum(a.count) as wimb_men_matches from (select player1 as player, count(*)from wimbledon_men_2013 group by player union all 
select player2 as player, count(*) from wimbledon_men_2013 group by player) a group by a.player) one
full outer join 
(select a.player, sum(a.count) as wimb_women_matches from (select player1 as player, count(*)from wimbledon_women_2013 group by player union all select player2 as player, count(*) from wimbledon_women_2013 group by player) a group by a.player) two 
on one.player=two.player
)) wimb
on france.player=wimb.player) g2
on g1.player = g2.player) monster) mash
where mash.total_men_matches is not null
order by mash.total_men_matches desc limit 5;

If you run the above code replacing the first instance of 'aus_men_matches' and then again with 'fr_men_matches', we see Rafael Nadal as the only player to have at least 7 matches for all 3 tournaments, so it must be him.

For women: 

select player, total_women_matches from
(select player, (us_women_matches) as total_women_matches from
(select concat(g1.player, g2.player) as player, us_men_matches, us_women_matches, aus_men_matches, aus_women_matches, fr_men_matches, fr_women_matches, wimb_men_matches, wimb_women_matches
from 
(select concat(usa.player, aus.player) as player, us_men_matches, us_women_matches, aus_men_matches, aus_women_matches
from
(select
concat(one.player, two.player) as player, us_men_matches, us_women_matches
from
(
(select a.player, sum(a.count) as us_men_matches from (select player1 as player, count(*)from us_men_2013 group by player union all 
select player2 as player, count(*) from us_men_2013 group by player) a group by a.player) one
full outer join 
(select a.player, sum(a.count) as us_women_matches from (select player1 as player, count(*)from us_women_2013 group by player union all select player2 as player, count(*) from us_women_2013 group by player) a group by a.player) two 
on one.player=two.player
)) usa
full outer join
(select
concat(one.player, two.player) as player, aus_men_matches, aus_women_matches
from
(
(select a.player, sum(a.count) as aus_men_matches from (select player1 as player, count(*)from aus_men_2013 group by player union all 
select player2 as player, count(*) from aus_men_2013 group by player) a group by a.player) one
full outer join 
(select a.player, sum(a.count) as aus_women_matches from (select player1 as player, count(*)from aus_ladies_2013 group by player union all select player2 as player, count(*) from aus_ladies_2013 group by player) a group by a.player) two 
on one.player=two.player
)) aus
on usa.player=aus.player) g1
full outer join
(select concat(france.player, wimb.player) as player, fr_men_matches, fr_women_matches, wimb_men_matches, wimb_women_matches
from
(select
concat(one.player, two.player) as player, fr_men_matches, fr_women_matches
from
(
(select a.player, sum(a.count) as fr_men_matches from (select player1 as player, count(*)from french_men_2013 group by player union all 
select player2 as player, count(*) from french_men_2013 group by player) a group by a.player) one
full outer join 
(select a.player, sum(a.count) as fr_women_matches from (select player1 as player, count(*)from french_women_2013 group by player union all select player2 as player, count(*) from french_women_2013 group by player) a group by a.player) two 
on one.player=two.player
)) france
full outer join
(select
concat(one.player, two.player) as player, wimb_men_matches, wimb_women_matches
from
(
(select a.player, sum(a.count) as wimb_men_matches from (select player1 as player, count(*)from wimbledon_men_2013 group by player union all 
select player2 as player, count(*) from wimbledon_men_2013 group by player) a group by a.player) one
full outer join 
(select a.player, sum(a.count) as wimb_women_matches from (select player1 as player, count(*)from wimbledon_women_2013 group by player union all select player2 as player, count(*) from wimbledon_women_2013 group by player) a group by a.player) two 
on one.player=two.player
)) wimb
on france.player=wimb.player) g2
on g1.player = g2.player) monster) mash
where mash.total_women_matches is not null
order by mash.total_women_matches desc limit 10;

If you run the above code replacing the first instance of us_women_matches with fr_women_matches and again with aus_open_matches, we can deduce with some reasoning that the answer is Victoria Azarenka.

3.select max(fsp_2) from us_women_2013;
select player2, fsp_2 from us_women_2013 where fsp_2=93;
This tells us that the highest first serve percentage belongs to S Errani. We confirm that nobody has higher by selecting max over fsp_1,fsp_2 over the other 7 tables, and seeing that all of them are less than 93.

4. For the men:

select *, 100*u/p as unfp from
(select * from
(select concat(fmum.player, amwm.player) as player, coalesce(fmum.c,0)+coalesce(amwm.c,0) as c, coalesce(fmum.u,0)+coalesce(amwm.u,0) as u, coalesce(fmum.p,0)+coalesce(amwm.p,0) as p from
(select concat(fm.player, um.player) as player, coalesce(fm.c, 0)+coalesce(um.c,0) as c, coalesce(fm.u,0)+coalesce(um.u,0) as u, coalesce(fm.p,0)+coalesce(um.p,0) as p from
(select concat(player1, player2) as player, coalesce(c1,0)+coalesce(c2,0) as c, coalesce(u1, 0)+coalesce(u2,0) as u, coalesce(p1,0)+coalesce(p2,0) as p from ((select player1, count(*) as c1, sum(ufe_1) as u1, sum(tpw_2) as p1 from french_men_2013 where result = 1 group by player1) as a full outer join (select player2, count(*) as c2, sum(ufe_2) as u2, sum(tpw_1) as p2 from french_men_2013 where result = 0 group by player2) as b on a.player1 = b.player2) as d order by c desc) as fm
full outer join
(select concat(player1, player2) as player, coalesce(c1,0)+coalesce(c2,0) as c, coalesce(u1, 0)+coalesce(u2,0) as u, coalesce(p1,0)+coalesce(p2,0) as p from ((select player1, count(*) as c1, sum(ufe_1) as u1, sum(tpw_2) as p1 from us_men_2013 where result = 1 group by player1) as a full outer join (select player2, count(*) as c2, sum(ufe_2) as u2, sum(tpw_1) as p2 from us_men_2013 where result = 0 group by player2) as b on a.player1 = b.player2) as d order by c desc) as um
on fm.player = um.player) as fmum
full outer join
(select concat(am.player, wm.player) as player, coalesce(am.c,0)+coalesce(wm.c,0) as c, coalesce(am.u,0)+coalesce(wm.u,0) as u, coalesce(am.p,0)+coalesce(wm.p,0) as p from
(select concat(player1, player2) as player, coalesce(c1,0)+coalesce(c2,0) as c, coalesce(u1, 0)+coalesce(u2,0) as u, coalesce(p1,0)+coalesce(p2,0) as p from ((select player1, count(*) as c1, sum(ufe_1) as u1, sum(tpw_2) as p1 from aus_men_2013 where result = 1 group by player1) as a full outer join (select player2, count(*) as c2, sum(ufe_2) as u2, sum(tpw_1) as p2 from aus_men_2013 where result = 0 group by player2) as b on a.player1 = b.player2) as d order by c desc) as am
full outer join
(select concat(player1, player2) as player, coalesce(c1,0)+coalesce(c2,0) as c, coalesce(u1, 0)+coalesce(u2,0) as u, coalesce(p1, 0)+coalesce(p2,0) as p from ((select player1, count(*) as c1, sum(ufe_1) as u1, sum(tpw_2) as p1 from wimbledon_men_2013 where result = 1 group by player1) as a full outer join (select player2, count(*) as c2, sum(ufe_2) as u2, sum(tpw_1) as p2 from wimbledon_men_2013 where result = 0 group by player2) as b on a.player1 = b.player2) as d order by c desc) as wm
on am.player = wm.player) as amwm
on fmum.player = amwm.player) as mommy
where mommy.p>0) as daddy
order by c desc;

This tells us that Nadal has 14%, Wawrinka has 21%, and Djokovic has 17%.

For the women:

select *, 100*u/p as unfp from
(select * from
(select concat(fmum.player, amwm.player) as player, coalesce(fmum.c,0)+coalesce(amwm.c,0) as c, coalesce(fmum.u,0)+coalesce(amwm.u,0) as u, coalesce(fmum.p,0)+coalesce(amwm.p,0) as p from
(select concat(fm.player, um.player) as player, coalesce(fm.c, 0)+coalesce(um.c,0) as c, coalesce(fm.u,0)+coalesce(um.u,0) as u, coalesce(fm.p,0)+coalesce(um.p,0) as p from
(select concat(player1, player2) as player, coalesce(c1,0)+coalesce(c2,0) as c, coalesce(u1, 0)+coalesce(u2,0) as u, coalesce(p1,0)+coalesce(p2,0) as p from ((select player1, count(*) as c1, sum(ufe_1) as u1, sum(tpw_2) as p1 from french_women_2013 where result = 1 group by player1) as a full outer join (select player2, count(*) as c2, sum(ufe_2) as u2, sum(tpw_1) as p2 from french_women_2013 where result = 0 group by player2) as b on a.player1 = b.player2) as d order by c desc) as fm
full outer join
(select concat(player1, player2) as player, coalesce(c1,0)+coalesce(c2,0) as c, coalesce(u1, 0)+coalesce(u2,0) as u, coalesce(p1,0)+coalesce(p2,0) as p from ((select player1, count(*) as c1, sum(ufe_1) as u1, sum(tpw_2) as p1 from us_women_2013 where result = 1 group by player1) as a full outer join (select player2, count(*) as c2, sum(ufe_2) as u2, sum(tpw_1) as p2 from us_women_2013 where result = 0 group by player2) as b on a.player1 = b.player2) as d order by c desc) as um
on fm.player = um.player) as fmum
full outer join
(select concat(am.player, wm.player) as player, coalesce(am.c,0)+coalesce(wm.c,0) as c, coalesce(am.u,0)+coalesce(wm.u,0) as u, coalesce(am.p,0)+coalesce(wm.p,0) as p from
(select concat(player1, player2) as player, coalesce(c1,0)+coalesce(c2,0) as c, coalesce(u1, 0)+coalesce(u2,0) as u, coalesce(p1,0)+coalesce(p2,0) as p from ((select player1, count(*) as c1, sum(ufe_1) as u1, sum(tpw_2) as p1 from aus_ladies_2013 where result = 1 group by player1) as a full outer join (select player2, count(*) as c2, sum(ufe_2) as u2, sum(tpw_1) as p2 from aus_ladies_2013 where result = 0 group by player2) as b on a.player1 = b.player2) as d order by c desc) as am
full outer join
(select concat(player1, player2) as player, coalesce(c1,0)+coalesce(c2,0) as c, coalesce(u1, 0)+coalesce(u2,0) as u, coalesce(p1, 0)+coalesce(p2,0) as p from ((select player1, count(*) as c1, sum(ufe_1) as u1, sum(tpw_2) as p1 from wimbledon_women_2013 where result = 1 group by player1) as a full outer join (select player2, count(*) as c2, sum(ufe_2) as u2, sum(tpw_1) as p2 from wimbledon_women_2013 where result = 0 group by player2) as b on a.player1 = b.player2) as d order by c desc) as wm
on am.player = wm.player) as amwm
on fmum.player = amwm.player) as mommy
where mommy.p>0) as daddy
order by c desc;

This tells us that Williams has 45%.  So, the answer to the question, the unforced error percentages for the 3 highest ranked players (as defined by win number) are 14% for Nadal, 21% for Wawrinka, 17% for Djokovic, and 45% for Williams. (Djokovic and Williams both have 10 wins).
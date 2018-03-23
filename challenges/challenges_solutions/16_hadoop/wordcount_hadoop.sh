#!/bin/sh
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -file /home/hduser/mapper.py -mapper /home/hduser/mapper.py -file /home/hduser/count_reducer.py -reducer /home/hduser/count_reducer.py -input /user/username/gutenberg/pg4300.txt -output /user/username/book-output 




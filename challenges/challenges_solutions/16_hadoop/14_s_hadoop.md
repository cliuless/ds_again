#### Set 14:  Hadoop Challenges Solutions  
Date:  3/11/2016  
By:  Julia  

---

#### 1) The "hello world" of map reduce:  
(Just like we did in class.)  

Please note that the following exercise was completed 
via hadoop on AWS EC2.


a)  Get data  

Let’s make a directory for these  

```bash  
mkdir /home/hduser/textdata  
```

Get your Gutenberg ebooks (plain text `utf-8` encoding) you can
`wget`:  


 * [Ulyses by James Joyce](http://www.gutenberg.org/cache/epub/4300/pg4300.txt)  
 * [Notebooks of Leonardo Da Vinci](http://www.gutenberg.org/cache/epub/5000/pg5000.txt)  
 * [The Outline of Science by J Arthur Thomson](http://www.gutenberg.org/cache/epub/20417/pg20417.txt)  

For example:  

```bash
cd /home/hduser/textdata  
wget http://www.gutenberg.org/cache/epub/4300/pg4300.txt  
wget http://www.gutenberg.org/cache/epub/5000/pg5000.txt  
wget http://www.gutenberg.org/cache/epub/20417/pg20417.txt  
```


#### Put data in hdfs  

make some directories **in the hadoop distributed file system! **  

```bash  
hdfs dfs -mkdir /user/   
hdfs dfs -mkdir /user/username/  
hdfs dfs -mkdir /user/username/gutenberg  
```



```bash  
hdfs dfs -put /home/hduser/textdata/* /user/username/gutenberg  
```

Check and make sure it is in the hdfs  

```bash
hdfs dfs -ls /user/username  
```

Yay!  


#### Our mapper and reducer (use nano to create your your files)  
### Note: Make sure you are in '/home/hduser'  

Our mapper `mapper.py` includes the following code:  

```python  
#!/usr/bin/env python  

import sys  
from textblob import TextBlob  

for line in sys.stdin:  
    line = line.decode('utf-8')  
    words = TextBlob(line).words  
    for word in words:  
        word = word.encode('utf-8')  
        print "{}\t{}".format(word, 1)  
```

And our reducer `count_reducer.py` looks like this:  

```python  
#!/usr/bin/env python  

import sys  

current_word = None  
current_count = 0  
word = None  

for line in sys.stdin:  
    word, count = line.split('\t')  
    count = int(count)  
    if word == current_word:  
        current_count += count  
    else:  
        if current_word:  
            print '{}\t{}'.format(current_word, current_count)  
        current_word = word  
        current_count = count  

if current_word == word:  
    print '%s\t%i' % (current_word, current_count)  
```


#### Run it!  

First we have to change permissions for both of our files:  

chmod +x /home/hduser/mapper.py  
chmod +x /home/hduser/count_reducer.py  

Before we run it using hadoop, let's test it first without 
using hadoop:  

```bash  
cat textdata/pg20417.txt | ./mapper.py | sort | ./count_reducer.py > output  
```

Inspect your output:  
```bash  
cat output  
```

Now using Hadoop streaming API:  


```bash
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -file /home/hduser/mapper.py -mapper /home/hduser/mapper.py -file /home/hduser/count_reducer.py -reducer /home/hduser/count_reducer.py -input /user/username/gutenberg/pg4300.txt -output /user/username/book-output  
```  

Note that we can also run the above command using .sh.
Create a wordcount_hadoop.sh file:

```sh
#!/bin/sh
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -file /home/hduser/mapper.py -mapper /home/hduser/mapper.py -file /home/hduser/count_reducer.py -reducer /home/hduser/count_reducer.py -input /user/username/gutenberg/pg4300.txt -output /user/username/book-output 
```

Remember to change permissions on your wordcount_hadoop.sh file:  chmod +x 
Then run:

```bash
.\wordcount
```

* See book-output for sample output.  

To do a word count on multiple files, just add multiple input files (as follows)  

```bash
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -file /home/hduser/mapper.py -mapper /home/hduser/mapper.py -file /home/hduser/count_reducer.py -reducer /home/hduser/count_reducer.py -input /user/username/gutenberg/pg4300.txt -input /user/username/gutenberg/pg20417.txt-output /user/username/book-output  
```

#### 2) Write a mapper and reducer in Python to produce an outer join of the data in data.txt by name.  


Our mapper file:  

```python  
#!/usr/bin/env python  
import sys  

for line in sys.stdin:  
    try:  
        name=eval(line)['name']  
        type=eval(line)['type']  
        if 'age' in line:  
                third=eval(line)['age']  
        else:  
                third=eval(line)['product']  
        test=len(eval(line))  
        print "{}\t{}\t{}".format(name, type,third)  
    except:  
        pass  
```


Our reducer file: 

```python  
#!/usr/bin/env python  
import sys  

current_key=None  

for line in sys.stdin:  
        lines=line.split('\t')  
        lines=[x.replace('\n','') for x in lines]  
        if current_key is None:  
            current_key = lines[0]  
            values=lines[1:]  
            continue  
        if lines[0] == current_key:  
            values+=lines[1:]  
        else:  
            print current_key,values  
            current_key=lines[0]  
            values=lines[1:]  
print current_key, values  
```

Remember to add permissions:  

```bash
chmod +x map.py  
chmod +x reduce.py  


hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -file /home/hduser/map.py -mapper /home/hduser/map.py -file /home/hduser/reducer.py -reducer /home/hduser/reducer.py -input /user/username/data.txt -output /user/username/book-output2 

hdfs dfs -cat /user/username/book-output2/part-00000

Ann 2
Beth 3
Charlie 1
Dana 3
Eugene 3
Fred 4
Greg 1
```

done!  

---

**Extra, Extra!**

```
# run shell script at terminal
$  ./wordcount_hadoop.sh
```



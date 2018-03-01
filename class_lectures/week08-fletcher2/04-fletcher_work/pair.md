### Pair Problem

I know you all are focused on wrapping up the project. So we'll keep it simple today. Solve this HackerRank challenge.

#### Cut the sticks

You are given  sticks, where the length of each stick is a positive integer. A cut operation is performed on the sticks such that all of them are reduced by the length of the smallest stick.

Suppose we have six sticks of the following lengths:

    5 4 4 2 2 8
    
Then, in one cut operation we make a cut of length 2 from each of the six sticks. For the next cut operation four sticks are left (of non-zero length), whose lengths are the following: 

     3 2 2 6
     
The above step is repeated until no sticks are left.

Write a function that, given the length of sticks, prints the number of sticks that are left before each subsequent cut operations.

Sample Input #1

    [5 4 4 2 2 8]

Sample Output #1

    6
    4
    2
    1

Sample Input #2

    1 2 3 4 3 3 2 1

Sample Output #2

    8
    6
    4
    1

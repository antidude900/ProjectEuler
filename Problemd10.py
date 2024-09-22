"""
When doing this question, I got to a big problem. There were 7 test cases in total. Out of 7, 5 of them were solved but 2 of them exceeded time limit. 
I tried optmizing the code as much as I can but still 6 and 7 never solved. Then seeing the discussion section, I found out the mistake.

The problem was that for every test case I was making a sieve array from start. The efficient way was to find the maximum N among all the test cases
and make a sieve array of that maximum. In this way, ewe can use the same sieve array for all test cases saving time.

[To understand how the test cases are read, see the ReadMe of this repository]
"""

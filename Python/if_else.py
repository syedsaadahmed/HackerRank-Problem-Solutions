#!/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
if (N % 2 == 0 and N > 20):
    print "Not Weird"
elif (N % 2 == 0 and 2 <= N <= 5):
    print "Not Weird"
elif (N % 2 == 0 and 6 <= N <= 20):
        print "Weird"
else:
    print "Weird"

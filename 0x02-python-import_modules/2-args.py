#!/usr/bin/python3
import sys
count = len(sys.argv)
print("{} arguments:".format(count - 1))
for i in range(1, count):
    print("{}: {}".format(i,sys.argv[i]))

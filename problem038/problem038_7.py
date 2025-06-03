import sys

num = map(int,raw_input().split())

if num[0] < num[1]:
    print "a < b"
elif num[0] == num[1]:
    print "a == b"
elif num[0] > num[1]:
    print "a > b"
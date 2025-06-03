# coding: UTF-8
n = input()
for n in range(n):
    inputs = map(int,raw_input().split())
    if inputs[0]**2 == inputs[1]**2 + inputs[2]**2 or\
       inputs[1]**2 == inputs[0]**2 + inputs[2]**2 or\
       inputs[2]**2 == inputs[0]**2 + inputs[1]**2:
        print "YES"
    else:
        print "NO"
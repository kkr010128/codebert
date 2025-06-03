#!/usr/bin/python

s=raw_input()
p=raw_input()
s+=s
print "Yes" if p in s else "No"
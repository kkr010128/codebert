#!/usr/bin/python
# coding: utf-8

def maze(string, h):
    return string[h:] + string[:h]

while True:
    string = raw_input()
    if string == "-":
        break

    m = int(raw_input())
    for i in range(m):
        h = int(raw_input())
        string = maze(string, h)
        #print "h: {}, string: {}".format(h, string)
    print string
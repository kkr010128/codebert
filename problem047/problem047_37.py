#-------------------------------------------------------------------------------
# coding: utf-8
# Created:     16/12/2015
import sys

io = sys.stdin

op = { "+" : lambda x, y:  x + y,
        "-": lambda x,y: x - y,
        "/": lambda x,y: x/y,
        "*": lambda x,y: x*y }


while True:
    a, op_, b = io.readline().split()
    if op_ == "?" : break
    a1, b1 = int(a), int(b)

    print op[op_](a1, b1)
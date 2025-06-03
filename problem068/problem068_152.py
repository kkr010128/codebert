#coding: utf-8

s = input()
q = int(input())
for i in range(q):
    order = input().split(" ")
    if   order[0] == "print":
        print(s[int(order[1]) : int(order[2])+1])
    elif order[0] == "reverse":
        r = s[int(order[1]) : int(order[2])+1]
        r = r[::-1]
        s = s[:int(order[1])] + r + s[int(order[2])+1:]
    elif order[0] == "replace":
        s = s[:int(order[1])] + order[3] + s[int(order[2])+1:]


# coding: utf-8
# Here your code !
N=int(input())
dict={}
for i in range(N):
    a,b=input().split()
    if a=="insert":
        dict[b]=i
    else:
        if b in dict:
            print("yes")
        else:
            print("no")
# coding: utf-8
# Your code here!
A,V = map(int,input().split())
B,W = map(int,input().split())
T = int(input())

dis=abs(A-B)
dis1=(V-W)*T

if dis<=dis1:
    print("YES")
else:
    print("NO")

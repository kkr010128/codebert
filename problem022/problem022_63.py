# coding: utf-8
input()
s = list(map(int,input().split()))
input()
t = list(map(int,input().split()))
cnt = 0
for i in t:
    if i in s:
        cnt += 1
print(cnt)
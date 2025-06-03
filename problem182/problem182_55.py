from sys import stdin, stdout
import math
import bisect
import re

n, k, c = map(int, stdin.readline().strip().split())
s = stdin.readline().strip()

arr1 = [-1] * 200005
arr2 = [-1] * 200005

cnt = 1
day = 0
while day<len(s):
    if s[day] == 'o':
        arr1[day] = cnt
        cnt += 1
        day+=c
    if cnt > k:
        break
    day+=1

cnt = k
day = len(s) - 1
while day>=0:
    if s[day] == 'o':
        arr2[day]=cnt
        cnt-=1
        day-=c
    if cnt <= 0:
        break
    day-=1

for i in range(len(s)):
    if arr1[i]==arr2[i] and arr1[i]!=-1:
        stdout.writelines('%d\n' % (i+1))
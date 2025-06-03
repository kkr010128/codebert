#import sys
#input = sys.stdin.readline
M = 10**9+7
n = int(input())
l = list(map(int,input().split()))
o = [0]*61
z = [0]*61
for i in l:
    a = bin(i)[2:]
    j = 0
    while(j < len(a)):
        if a[j] == "1":
            o[len(a)-j-1] += 1

        j += 1

cnt = 0
b = 1
for j in range(len(o)):
    cnt = (cnt+(o[j]*(n-o[j])*b)%M)%M
    b *= 2

print(cnt)

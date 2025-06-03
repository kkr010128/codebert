import sys
input = sys.stdin.readline

n = int(input())
s, t = list(map(list, input().split()))

a = ""

for i in range(n):
    a += s[i]
    a += t[i]

print(a)


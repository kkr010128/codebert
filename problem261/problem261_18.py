import sys
input = sys.stdin.readline

s = list(input())

a = 0

#print(len(s))

for i in range((len(s) - 1) // 2):
    #print(s[i], s[-2-i])
    if s[i] != s[-2-i]:
        a += 1

print(a)
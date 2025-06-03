n = int(input())
s, t = input().split()
ret = ''
for i, j in zip(s, t):
    ret += i
    ret += j
print(ret)
n = int(input())
s = list(map(int, input().split()))
q = int(input())
t = list(map(int, input().split()))
c = 0
for num in t:
    if num in s:
        c += 1

print(c)

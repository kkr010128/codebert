n = int(input())
a = [int(x) for x in input().split()]
s = 0
for i in a:
    s ^= i
print(*[x ^ s for x in a])
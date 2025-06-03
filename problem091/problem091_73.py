from itertools import*
n=input()
l = map(int,input().split())
ans = 0
for a, b, c in combinations(l, 3):
    if a != b != c != a and a + b > c and b + c > a and c + a > b:
        ans += 1
print(ans)
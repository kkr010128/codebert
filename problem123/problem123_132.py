N = int(input())
A = list(map(int, input().split()))
total = 0
for a in A:
    total ^= a

ans = ""

for a in A:
    ans += str(total^a) + " "

print(ans)
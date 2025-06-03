n = int(input())
a = [int(x) for x in input().split()]

ans = 0
maxa = 0
for aa in a:
    maxa = max(maxa, aa)
    ans += maxa - aa
print(ans)
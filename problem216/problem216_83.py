a, b, c = map(int, input().split())
ans = "No"

if a == b and b != c:
    ans = "Yes"
elif b == c and c != a:
    ans = "Yes"
elif a == c and c != b:
    ans = "Yes"

print(ans)

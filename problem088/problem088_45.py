N = int(input())
As = list(map(int, input().split()))

now = 0
cost = 0
for A in As:
    if A > now:
        now = A
    else:
        cost += now-A
print(cost)
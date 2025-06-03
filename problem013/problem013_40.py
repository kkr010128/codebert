n = int(input())
R = [int(input()) for i in range(n)]
profit= R[1] - R[0]
mn = R[0]
R.pop(0)
for i in R:
    if profit < i - mn:
        profit = i - mn
        if 0 > i - mn:
            mn = i
    elif mn > i:
        mn = i

print(profit)
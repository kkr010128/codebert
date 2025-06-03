N = int(input())
m = N//100
M = N//105
if 100*m <= N <= 105*m or 100*M <= N <= 105*M:
    print(1)
else:
    print(0)
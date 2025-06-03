S = int(input())
if S % 1000 == 0:
    W = 0
else:
    W = 1000-(S % 1000)
print(W)
190
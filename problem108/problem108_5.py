N = int(input())
if N % 1000 == 0:
    print(0)
else:
    payment = N // 1000 + 1
    change = payment*1000 - N
    print(change)

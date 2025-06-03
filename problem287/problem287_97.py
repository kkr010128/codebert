N = int(input())

ans = False

for i in range(1,10):
    if N % i == 0 and N / i <= 9:
        ans = True

if ans:
    print("Yes")
else:
    print("No")
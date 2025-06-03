n = int(input())

ans = 0
ama = 0

for i in range(1, 10):
    ans = n / i
    ama = n % i

    if i == 9 and ama != 0:
        print("No")
    if i <= 9 and ans <= 9 and ama == 0:
        print("Yes")
        exit()
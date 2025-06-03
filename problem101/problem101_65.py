A, B, C = map(int, input().split())
K = int(input())

for i in range((K + 1)):
    for j in range((K + 1) - i):
        for k in range((K + 1) - i - j):
            if A * (2 ** i) < B * (2 ** j) < C * (2 ** k):
                print("Yes")
                exit()

print("No")

N = int(input())
S = 0

for i in range(1, N + 1):
    if i % 15 == 0:
        S += 0
    elif i % 3 == 0:
        S += 0
    elif i % 5 == 0:
        S += 0
    else:
        S += i
print(S)

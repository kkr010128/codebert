S = input()
T = input()

min = 10000000

for i in range(len(S)- len(T) + 1):
    x = 0
    for j in range(len(T)):
        if S[i+j] != T[j]:
            x += 1
    if x < min:
        min = x
print(min)
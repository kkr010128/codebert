S = input()
T = input()

S = list(S)
T = list(T)

result = len(T)
x = 0

for i in range(len(S)-len(T)+1):
    for j in range(len(T)):
        if S[i+j] != T[j]:
            x += 1
    if result > x:
        result = x
    x = 0

print(result)

S = input()
T = input()
a = len(T)
for i in range(len(S)-len(T)+1):
    c = 0
    for j, t in enumerate(T):
        if S[i+j] != t:
            c += 1
    a = min(a, c)
print(a)
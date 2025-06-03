
S = input()
T = input()

count = 0
max_count = 0

for i in range(len(S) - len(T) +1):
    for j in range(len(T)):
        if S[i+j] == T[j]:
            count += 1
            if max_count <= count:
                max_count = count
        if j == (len(T) -1):
            count = 0

print(len(T) - max_count)

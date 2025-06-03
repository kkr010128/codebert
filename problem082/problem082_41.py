S = input()
T = input()

max_count = 0
for i in range(max(1, len(S) - len(T))):
    count = 0
    for j in range(len(T)):
        if S[i+j] == T[j]:
            count += 1
    max_count = max(max_count, count)
    
print(len(T) - max_count)

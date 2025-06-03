S = input()
T = input()
count = []
for k in range(0,len(S)-len(T)+1):
    sum = 0
    for i in range(k,k+len(T)):
        if (S[i] != T[i-k]):
            sum += 1
    count.append(sum)

print(min(count))
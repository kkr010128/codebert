S = input()
T = input()
largest = 0
for i in range(len(S) - len(T)+1):
    count = 0
    for j in range(len(T)):
        if S[i+j] == T[j]:
            count += 1
    if largest < count:
        largest = count
print(len(T) - largest)

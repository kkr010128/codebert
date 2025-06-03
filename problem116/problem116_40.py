S = input()
list_S = list(S)
T = input()
list_T = list(T)
count = 0
for i in range(len(list_S)):
    if S[i] != T[i]:
        count +=1
print(count)
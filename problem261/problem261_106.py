S = input()
Count = 0
for T in range(0,len(S)//2):
    if S[T]!=S[-T-1]:
        Count += 1
print(Count)
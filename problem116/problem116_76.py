s = input()
S1 = list(s)
T = list(input())

cnt =0
for i in range(len(s)):
    if S1[i] != T[i]:
        cnt+=1
print(cnt)
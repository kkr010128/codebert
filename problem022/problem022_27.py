n = int(input())
S =input().split(" ")
l =int(input())
T = input().split(" ")
ans =0
for t in T:
    S.append(t)
    j =0
    while S[j] !=t:
        j+=1
    if j !=n:
        ans +=1
    S=S[:-1]
print(ans)

n = list(input())
for i in range(len(n)) :
    n[i] = int(n[i])
if sum(n)%9==0 :
    print("Yes")
else :
    print("No")
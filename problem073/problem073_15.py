n = int(input())
ans = 0
t = 0
J = 0
for i in range(1,n):
    for j in range(i,n):
        if i*j >= n:break
        if i == j : t+=1
        ans +=1
        J = j


print(2*ans -t)

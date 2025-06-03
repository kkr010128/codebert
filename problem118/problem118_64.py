N = int(input())
ans = 0
l = N//2
for i in range(1, l+1): #約数についてのループ
    n = N//i
    ans += i*n*(n+1)//2
    
# 約数がl+1より大きい時は、それを約数に持つ数は1個しかない(それ自身)
ans += (l+1+N)*(N-l)//2

print(ans)
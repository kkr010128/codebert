N = int(input())
sum_ = lambda n:(n*(n+1))//2
ret = sum(d*sum_(N//d) for d in range(1,N+1))
# print([d*sum_(N//d) for d in range(1,N+1)])
print(ret)
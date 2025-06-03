x = int(input())
mod =10**9 + 7
ans = pow(10,x,mod)
ans -= 2 * pow(9,x,mod)
ans += pow(8,x,mod)
ans %=mod
print(ans)
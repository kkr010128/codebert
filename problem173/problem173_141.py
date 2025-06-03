n=int(input())
ans = 0
ans += n*(n+1)//2
ans += 15*(n//15)*(n//15+1)//2
ans -= 3*(n//3)*(n//3+1)//2
ans -= 5*(n//5)*(n//5+1)//2
print(ans)

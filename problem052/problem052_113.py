n=int(input())
print(*['']+[i for i in range(3,n+1)if i%3==0 or '3' in str(i)])
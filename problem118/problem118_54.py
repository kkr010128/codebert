n = int(input())
print(int(sum([k*(n//k+1)*(n//k)/2 for k in range(1,n+1)])))
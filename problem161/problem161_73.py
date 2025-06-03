A,B,N = map(int, input().split())

if N >= B:
    ans = (A//B)*(B-1) + (A%B)*(B-1)//B
else:
    ans = (A//B)*N + (A%B)*N//B

print(ans)
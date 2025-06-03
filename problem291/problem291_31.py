A,B = map(int,input().split())
ans=int(A-B*2)
print(ans if ans >= 0 else 0)
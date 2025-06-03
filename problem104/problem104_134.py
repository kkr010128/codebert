L,R,d = (int(X) for X in input().split())
print(sum([True for T in range(L,R+1) if T%d==0]))
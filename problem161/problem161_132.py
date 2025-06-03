A, B, N = map(int, input().split())


if N//B == 0:
    ans_i = N
else :
    ans_i = B*(N//B)-1

print((A*ans_i)//B - A*(ans_i//B))

N, M=map(int, input().split())
s_row = [0 for x in range(M+1)]
for n in range(N):
 arr = list(map(int, input().split()))
 arr.append(sum(arr))
 s_row = [x+y for x,y in zip(s_row, arr)]
 print(" ".join([str(x) for x in arr]))
print(" ".join([str(x) for x in s_row]))
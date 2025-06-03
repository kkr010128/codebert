n = int(input())
A = list(enumerate(list(map(int, input().split()))))
A.sort(key=lambda x:x[1])
ans = []
for i in A: ans.append(str(i[0]+1))
print(" ".join(ans))
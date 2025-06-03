
N = int(input())
L = len(str(N))
if L == 1:
    print(N)
    quit()
    
pair = [[(10**(L-2)-1)//9]*9 for _ in range(9)]
for i in range(9):
    pair[i][i] += 1

for i in range(10**(L-1), N+1):
    pair[int(str(i)[0])-1][int(str(i)[L-1])-1] += 1 if i%10 else 0
ans = 0
for i in range(9):
    for j in range(9):
        ans += pair[i][j] * pair[j][i]
print(ans)
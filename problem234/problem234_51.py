import numpy as np

n = int(input())
table,ans = np.zeros((9,9)),0

for k in range(n):
    num = str(k+1)
    if int(num[0])!=0 and int(num[-1])!=0:
        table[int(num[0])-1][int(num[-1])-1]+=1

for i in range(9):
    for j in range(9):
        ans += table[i][j]*table[j][i]
print(int(ans))
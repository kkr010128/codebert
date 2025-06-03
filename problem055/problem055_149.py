import sys
n = int(input())

A=[[[0 for _ in range(10)] for _ in range(3)] for _ in range(4)]
#0??§?????????
#[[[0 0 0 0 0 0 0 0 0 0],
#  [0 0 0 0 0 0 0 0 0 0],
#  [0 0 0 0 0 0 0 0 0 0]],
# [[0 0 0 0 0 0 0 0 0 0],
#  [0 0 0 0 0 0 0 0 0 0],
#  [0 0 0 0 0 0 0 0 0 0]],
# [[0 0 0 0 0 0 0 0 0 0],  
#  [0 0 0 0 0 0 0 0 0 0],
#  [0 0 0 0 0 0 0 0 0 0]],
# [[0 0 0 0 0 0 0 0 0 0],
#  [0 0 0 0 0 0 0 0 0 0],
#  [0 0 0 0 0 0 0 0 0 0]]]

#?£?    Building = b
#???    Floor    = f
#???    Room     = r
#??°    Number   = num
for i in range(n):
	b,f,r,num = input().strip().split()
	A[int(b)-1][int(f)-1][int(r)-1]+=int(num)

for i in range(4):
	for j in range(3):
		print('',' '.join(map(str,A[i][j])))
	if i!=3:
		print('#'*20)
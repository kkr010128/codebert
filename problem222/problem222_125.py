N = int(input())
A = list(map(int, input().split()))
N_MAX = 200000
A_MAX = 10 ** 9

temp = dict()

for i in A:
  if i in temp:
    print("NO")
    exit()
  else:
    temp[i] = 0
print("YES")
N = int(input())
i = list(map(int, input().split())) #i_1 i_2を取得し、iに値を入れる

s = 0

for j in range(0,N,2):
  if i[j] % 2 == 1 :
    s += 1
print(s)
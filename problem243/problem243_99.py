n = int(input())
dic = {}
time = []
for i in range(n):
  s, t = map(str, input().split())
  dic[s] = i + 1
  time.append(int(t))
ans = 0
song = input()
ans = sum(time[dic[song]:])
print(ans)
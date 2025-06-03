n = int(input())
a = list(map(int,input().split()))
hidariwa = sum(a)
migiwa = 0
answer = hidariwa
for i in range(n):
  hidariwa -= a[i]
  migiwa +=a[i]
  answer = min(abs(hidariwa-migiwa),answer)
print(answer)
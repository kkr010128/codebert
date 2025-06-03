A,B = map(int,input().split())
num = min(A,B)
num1 = max(A,B)
count=0
for i in range(num1):
  count += num*(10**i)
print(count)
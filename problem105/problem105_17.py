n = int(input())
a = list(map(int,input().split()))
number = len(a)
count = 0

for i in range(0,number,2):
  if a[i]%2 == 1:
    count += 1
print(count)
    


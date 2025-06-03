a = int(input())
AA = map(int,input().split())
AAA = list(AA)
count = 0
for i in range(a):
  if i%2 ==0 and AAA[i]%2 ==1:
    count +=1
print(count)
n = int(input())
a = list(map(int, input().split()))
lists = [0] * n
 
for i in range(n):
    lists[a[i] - 1] = i + 1
    
for i in lists:
  print(i , end =' ')
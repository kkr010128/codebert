n,k = map(int,input().split())

li = []
for i in range(k) :
  gomi = input()
  [li.append(int(j)) for j in input().split()]
st = set(li)
  
print(n - len(st))
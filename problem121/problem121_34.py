N = int(input())
eList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
n = N
mod = N
numList = []
 
while n > 0:
  n, mod = divmod(n,26)
  if mod != 0:
    numList.insert(0, mod - 1)
  else:
    numList.insert(0, 25)
    n -= 1
ans =''
for num in numList:
  ans += eList[num]
print(ans)
N = int(input())
ans = []
while N > 0:
  N -= 1
  a = N%26
  ans.append(chr(97+a))
  N = N//26
#print(ans)
ret = ""
for i in range(len(ans)):
  ret += ans[-1-i]
  #print(ret)
print(ret)
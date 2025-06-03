N = int(input())
s = input()
a = [chr(i) for i in range(65, 65+26)]
ls = []
for x in a:
  ls.append(x)
for x in a:
  ls.append(x)
ans = []
for x in s:
  ans.append(ls[ls.index(x)+N])
print(''.join(ans))
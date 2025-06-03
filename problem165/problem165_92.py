n=int(input())
ls=[]
for i in range(n):
  s=input()
  ls.append(s)

setl=set(ls)
print(len(setl))
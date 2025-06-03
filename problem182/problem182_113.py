"""
入力例 1 
11 3 2
ooxxxoxxxoo
->6
入力例 2 
5 2 3
ooxoo
->1
->5

入力例 3 
5 1 0
ooooo
->
入力例 4 
16 4 3
ooxxoxoxxxoxoxxo
->11
->16
"""
n,k,c = map(int,input().split())
s = input()
r=[0]*n
l=[0]*n
ki=0
ci=100000
for i in range(n):
    ci += 1
    if s[i]=='x':
        continue
    if ci > c:
        ci = 0
        ki+=1
        l[i]=ki
    if ki == k:
        break

ki=k
ci=100000
for i in range(n):
    ci += 1
    if s[n-1-i]=='x':
        continue
    if ci > c:
        ci = 0
        r[n-1-i]=ki
        ki-=1
    if ki == 0:
        break
ret=[]
for i in range(n):
    if r[i]==l[i] and r[i]!=0:
        ret.append(i+1)
# print(l)
# print(r)
for i in range(len(ret)):
  print(ret[i])
  


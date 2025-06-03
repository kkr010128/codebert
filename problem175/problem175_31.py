from collections import Counter
n=int(input())
stri=list(input())
cc=Counter(stri)

count=cc['R']*cc['G']*cc['B']


for i in range(n-2):
  for j in range(i+1,n-1):
    if stri[j]==stri[i]:continue
      
    lib=['R','G','B']
    lib.remove(stri[i])
    lib.remove(stri[j])
    t=lib.pop()
    
    skip_k=2*j-i
    #print(i,j,skip_k)
    if skip_k>n-1:continue
    if stri[skip_k]==t:
      count-=1
print(count)
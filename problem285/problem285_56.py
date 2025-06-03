import sys
sys.setrecursionlimit(1000000)
s=input()
#print(s)
l=[-1 for _ in range(len(s)+1)]
def aa(ix,v): #ixはlベース
# print(ix,v,l)
  if (ix>= len(s) and v==1) or (ix==0 and v==0-1):
    return
  if v==1 and s[ix]=="<" and l[ix+1]<=l[ix]:
    l[ix+1]=l[ix]+1
    aa(ix+1,1)
  elif v==-1 and s[ix-1]==">" and l[ix-1]<=l[ix]:
    l[ix-1]=l[ix]+1
    aa(ix-1,-1)
  return

for i in range(0,len(s)):
  if i ==0 and s[0]=="<":    
    l[0]=0
    aa(i,1)
  elif i==len(s)-1 and s[-1]==">":
    l[-1]=0
    aa(i+1,-1)
  elif s[i]==">" and s[i+1]=="<":
    l[i+1]=0
    aa(i+1,1)
    aa(i+1,-1)

print(sum(l))


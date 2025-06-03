d=int(input())
c=list(map(int,input().split()))
s=[list(map(int,input().split()))for _ in range(d)]
class Score:
  def __init__(self,t):
    self.x=[d*[0]for _ in range(26)]
    self.scor=0
    self.ans=[]
    for i in range(d):
      v=t[i]
      self.scor+=s[i][v]
      for j in range(26):
        if j!=v:
          self.x[j][i]+=1
          if i!=0:self.x[j][i]+=self.x[j][i-1]
        self.scor-=c[j]*self.x[j][i]
      self.ans.append(self.scor)
  def solve(self):
    return [self.scor,self.ans]
t=[int(input())-1 for _ in range(d)]
x=Score(t)
_,ans=x.solve()
for i in ans:print(i)
class UnionFindTree():
    def __init__(self, n):
        self.parents = [-1] * n
 
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
 
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
 
        if x == y:
            return
        
        # 常にxの要素数＞yの要素数とする
        if self.parents[x] > self.parents[y]:
            x, y = y, x
            
        # self.parents[x] に　yの要素数を追加してから併合
        self.parents[x] += self.parents[y]
        self.parents[y] = x

def main():
  N, M = map(int, input().split())
  uft = UnionFindTree(N)
  
  for m in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    uft.union(a, b)
    
  print(-min(uft.parents))
  
  
  
if __name__ == "__main__":
  main()
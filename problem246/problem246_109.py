import itertools

def dictnum(l):
  seq=list(itertools.permutations(l))
  seq.sort()

  return seq.index(tuple(l))

n=int(input())
p=list(map(int,input().split()))
q=list(map(int,input().split()))

print(abs(dictnum(p)-dictnum(q)))
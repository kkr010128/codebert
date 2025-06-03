def row():
  c=0
  for y in range(HEIGHT):
    for x in range(WIDTH):
      if A[y][x]!=-1:
        break
    else:
      c+=1
  return c


def col():
  c=0
  for x in range(WIDTH):
    for y in range(HEIGHT):
      if A[y][x]!=-1:
        break
    else:
      c+=1
  return c


def obl():
  c=0
  for z in range(HEIGHT):
    if A[z][z]!=-1:
      break
  else:
    c+=1
  
  y=0
  for x in range(WIDTH-1,-1,-1):
    if A[y][x]!=-1:
      break
    y+=1
  else:
    c+=1
  return c  
    

def main():
  for b in B:
    for y in range(HEIGHT):
      for x in range(WIDTH):
        if A[y][x]==b:
          A[y][x]=-1
  cnt=row()+col()+obl()
  print('Yes' if cnt else 'No')

  
if __name__=='__main__':
  HEIGHT=3
  WIDTH=3
  A=[[int(a) for a in input().split()] for y in range(HEIGHT)]
  N=int(input())
  B=[int(input()) for n in range(N)]
  main()
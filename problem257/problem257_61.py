
from sys import exit

def main():
  N = int(input())
  a = list(map(int,input().split()))
  index = -1
  num = 1
  
  for i in range(index+1, N):
    if a[i] != num:
      continue
    elif a[i] == num:
      index = i
      num += 1
      
  if index != -1:
    print(N-(num-1))
    exit()
      
  #indexに更新がなければ-1のまま
  print(index)
  
  
  
  
main()
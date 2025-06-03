def main():
  a, b = input().split()
  ansA = ''
  ansB = ''
  
  for _ in range(int(b)):
    ansA += a
  for _ in range(int(a)):
    ansB += b
    
  if ansA > ansB:
    print(ansB)
  elif ansA <= ansB:
    print(ansA)
  
  
  
  
main()
def main():
  N = int(input())
  S = input()
  
  cnt = 0
  
  for i in range(N-2):
    if S[i] == 'A':
      if S[i+1] == 'B':
        if S[i+2] == 'C':
          cnt += 1
  print(cnt)
  
  
main()
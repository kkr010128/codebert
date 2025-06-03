from sys import exit
def main():
  N = int(input())
  S = input()
  middle = int(N / 2)
  
  if middle == 0 or N % 2 != 0:
    print('No')
    exit()
  
  for i in range(middle):
    if S[i] != S[i + middle]:
      print('No')
      exit()
  
  print('Yes')
  
main()
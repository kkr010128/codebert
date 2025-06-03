import sys

N = int(input())
S = input()

if N%2!=0 :
  print("No")
  sys.exit(0)
else:
  for i in range(int(N/2)):
      if S[i]!=S[i+int(N/2)]:
        print("No")
        sys.exit(0)
print("Yes")
import sys
S = input()
N = int(input())
for i in range(N):
  a = sys.stdin.readline().split()
  if a[0] == "replace":
    S = S[:int(a[1])] + a[3] + S[int(a[2])+1:]
  elif a[0] == "reverse":
    X =  S[int(a[1]):int(a[2])+1]
    X = X[::-1]
    S = S[:int(a[1])] + X +S[int(a[2])+1:]
  elif a[0] == "print":
    print(S[int(a[1]):int(a[2])+1])

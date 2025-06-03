N = input()
A = list(map(int, input().split()))
C = sorted(A)
l = len(A)
i = 0
S = 1

while i < l:
   S = S * C[i]
   i = i + 1
   if S > 1000000000000000000:
        print(-1)
        break
   elif i == l:
        print(S)
        break
H = int(input())
W = int(input())
N = int(input())

def f(a):
   if N % a == 0:
      result = int(N / a)
   else:
      result = int(N / a) + 1
   print(result)

if H <= W:
   f(W)
else:
   f(H)
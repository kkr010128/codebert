X, N = map(int, input().split())
p_list = list(map(int, input().split()))

if N == 0: 
   print(X)
else:
   for i in range(0,100):
       if not X-i in p_list:
           print(X-i)
           break
       elif not X+i in p_list:
           print(X+i)
           break
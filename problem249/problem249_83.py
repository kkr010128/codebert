a,b,k=map(int,input().split())
if k>a+b:print(0,0)
elif a<=k and k<=a+b:
    print(0,b-(k-a))
elif a>k :
      print(a-k,b)

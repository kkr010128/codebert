while 1:
    s=input()
    
    if len(s)==1:break
      
    for _ in range(int(input())):
        a=int(input())
        s=s[a:]+s[:a]
    
    print(s)

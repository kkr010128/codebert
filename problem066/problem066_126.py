while True:
    n=input()
    if n=='-':
        break
    else:
        m=int(input())
        for i in range(m):
            h=int(input())
            n=n[h:len(n)]+n[:h]
        print(n)
    

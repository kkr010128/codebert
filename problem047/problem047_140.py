while True:
    a,op,b = input().split()
    a = int(a)
    b = int(b)
    if op =='?':
        break
    elif op =='+':
        print('%d'%(a+b))
    elif op =='-':
        print('%d'%(a-b))
    elif op =='*':
        print('%d'%(a*b))
    elif op =='/':
        print('%d'%(a/b))


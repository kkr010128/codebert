while True:
    n=input()
    if n=="-":
        break
    for i in range(int(input())):
        h=int(input())
        n=n[h:]+n[:h]
    print(n)
    

while 1:
    n=input()
    if len(n)==1:break
    for i in range(int(input())):
        a=int(input())
        n=n[a:]+n[:a]
    print(n)

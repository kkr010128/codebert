while True:
    n=input()
    if n=='-':break
    x=int(input())
    for _ in range(x):
        h=int(input())
        n=n[h:]+n[:h]
    print(n)

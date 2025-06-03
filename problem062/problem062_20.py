while True:
    s=input()
    if s=="0":
        break
        
    n=list(map(int, list(s)))
    print(sum(n))
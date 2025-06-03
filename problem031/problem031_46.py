while True:
    n = int(raw_input())
    if n == 0: break
 
    x = map(int, raw_input().split())
    ave = sum(x) / float(n)
    std = (sum([(e-ave)**2 for e in x])/n)**0.5
    print std

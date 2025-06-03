#ITP1_10-C Standard Deviation
while True:
    n= int(input())
    if n==0:
        break
    s = input().split(" ")
    mean = 0.0
    for i in range(n):
        mean += float(s[i])
    mean /= n
    cov = 0.0
    
    for i in range(n):
        cov+=((float(s[i])-mean)**2)/n
    print(cov**0.5)
n,m=map(int, input().split())
if m%2==1:
    for i in range(m//2):
        print(i+1,m-i)
    for i in range(m//2+1):
        print(m+i+1,2*m+1-i)
else:
    for i in range(m//2):
        print(i+1,m+1-i)
    for i in range(m//2):
        print(m+i+2,2*m+1-i)
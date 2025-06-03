
while True:
    m,f,r=list(map(int,input().split()))
    if m==f==r==-1: break
    s=m+f
    print('F' if m*f<0 or s<30 else 'D' if 30<=s<50 and r<50 else 'C' if 50<=s<65 or 30<=s<50 and 50<=r else 'B' if 65<=s<80 else 'A')
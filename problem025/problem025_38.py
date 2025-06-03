def resolve():
    n=int(input())
    a=list(map(int,input().split()))
    q=int(input())
    m=list(map(int,input().split()))
    sa=[0]*100000
    for i in range(2**n):
        s=0
        for j in range(n):
            if i>>j&1:
                s+=a[j]
        sa[s]=1
    for i in m:
        if sa[i]==0:
            print('no')
        else:
            print('yes')

if __name__ == '__main__':
    resolve()

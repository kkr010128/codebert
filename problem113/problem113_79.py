import random

def solve(d,c,s):
    A=[]
    cnt=0
    while cnt<=1000:
        last=[0]*27
        srate=[]
        ans=[]
        for i in range(1,d+1):
            a=0
            for j in range(1,27):
                a-=c[j-1]*(i-last[j])
            t=random.randint(1,26)
            a+=s[i-1][t-1]+c[t-1]*(i-last[t])
            last[t]=i           
            ans.append(t)
            srate.append(a)
        A.append([srate[-1]]+ans)
        cnt+=1
    A.sort(reverse=True)
    return A[0]

def main():
    d=int(input())
    c=list(map(int,input().split()))
    s=[list(map(int,input().split())) for _ in range(d)]
    ans=solve(d,c,s)
    #print(ans[0])
    for i in ans[1:]:
        print(i)

if __name__ == '__main__':
    main()
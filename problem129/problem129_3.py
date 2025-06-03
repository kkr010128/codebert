import collections
N=int(input())
A=list(map(int,input().split()))
A=sorted(A)
c=collections.Counter(A)
if __name__=="__main__":
    if 1 in A:
        if c[1]==1:
            print(1)
        else:
            print(0)
    else:
        A=[]
        dp=[True for _ in range(10**6+10)]
        for key,value in c.items():
            if value==1:
                A.append(key)
            else:
                if dp[key]:
                    i=2
                    while i*key<=10**6:
                        dp[i*key]=False
                        i+=1 
        if len(A)==0:
            print(0)
        else:
            for a in A:
                if dp[a]:
                    i=2
                    while i*a<=10**6:
                        dp[i*a]=False
                        i+=1 
            ans=0
            for a in A:
                if dp[a]:
                    ans+=1
            print(ans)


n,k,s = map(int,input().split())

u = []
if n == k:
    for i in range(n):
        u.append(s)
else:
    if s%2==0:
        for i in range(k+1):
            u.append(int(s/2))
        for i in range(n-k-1):
            u.append(10**9-1)
    else:
        if s==1:
            for i in range(k):
                u.append(1)
            for i in range(n-k):
                u.append(10**9)
        else:
            if k%2==0:
                u.append(int((s-1)/2))
                for i in range(int(k/2)):
                    u.append(int((s+1)/2))
                    u.append(int((s-1)/2))    
                for i in range(n-k-1):
                    u.append(10**9)
            else:
                for i in range(int((k+1)/2)):
                    u.append(int((s+1)/2))
                    u.append(int((s-1)/2))  
                for i in range(n-k-1):
                    u.append(10**9)
print(' '.join(map(str,u)))
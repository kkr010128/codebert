a,b,c,d,e,f=map(int,input().split())
d2={1:a,2:b,3:c,4:d,5:e,6:f}
d1={a:1,b:2,c:3,d:4,e:5,f:6}
a,b,c,d,e,f=1,2,3,4,5,6
ans=[[b,c,e,d,b],[a,d,f,c,a],[a,b,f,e,a],[a,e,f,b,a],[a,c,f,d,a],[b,d,e,c,b]]
for _ in range(int(input())):
    top,front=map(int,input().split())
    top,front=d1[top],d1[front]
    top-=1
    for i in range(len(ans[top])):
        if front==ans[top][i]:
            print(d2[ans[top][i+1]])
            break
    

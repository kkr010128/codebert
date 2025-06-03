s,t=list(input().split())
a,b=list(map(int,input().split()))
u=input()
ball={s:a,t:b}  
ball[u] =max(0,ball[u]-1)

print(ball[s],ball[t])
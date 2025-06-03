x_low,x_up,y_low,y_up=map(int,input().split())

a1=x_low*y_low
a2=x_low*y_up
a3=x_up*y_low
a4=x_up*y_up

ans=max(a1,a2,a3,a4)
print(ans)
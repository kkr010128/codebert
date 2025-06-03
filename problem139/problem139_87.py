from datetime import datetime,timedelta

a=input().split()
a=[int(_) for _ in a]

t1=datetime(2000,1,1,a[0],a[1],0)
t2=datetime(2000,1,1,a[2],a[3],0)

delta=t2-t1
total_seconds=delta.seconds

ans=(total_seconds-a[4]*60)/60
print(int(ans))

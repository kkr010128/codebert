n,k=map(int,input().split())
a=list(map(int,input().split()))
town=[0]*n
info=[1]
now=1
while town[now-1]==0:
    town[now-1]+=1
    now=a[now-1]
    info.append(now)
loop_list=list(info[info.index(now):-1])
loop_len=len(loop_list)
before_loop_list=list(info[:info.index(now)])
#print(town)
#print(info)
if k<len(before_loop_list):
    print(before_loop_list[k])
else:
    print(loop_list[((k-len(before_loop_list))%loop_len)])
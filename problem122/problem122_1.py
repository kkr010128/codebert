n = int(input())
a = [int(x) for x in input().split()]
q = int(input())
bc=[]
for i in range(q):
    bc.append([int(x) for x in input().split()])

a_cnt=[0]*(10**5+1)

for i in range(len(a)):
	a_cnt[a[i]]+=1

a_goukei=sum(a)

for gyou in range(q):
	a_goukei+=(bc[gyou][1]-bc[gyou][0])*a_cnt[bc[gyou][0]]
	print(a_goukei)
	a_cnt[bc[gyou][1]]+=a_cnt[bc[gyou][0]]
	a_cnt[bc[gyou][0]]=0
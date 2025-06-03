S=[]
T=[]

S_num=int(input())
S=input().split()

T_num=int(input())
T=input().split()

cnt=0
for i in range(T_num):
	for j in range(S_num):
		if(S[j]==T[i]):
			cnt+=1
			break

print(cnt)

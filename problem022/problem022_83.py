S=[]
T=[]
n=int(input())
s=input().split()
for i in range(n):
	S.append(s[i])
q=int(input())
t=input().split()
for j in range(q):
	T.append(t[j])
cnt=0
for i in range(q):
	for j in range(n):
		if T[i]==S[j]:
			cnt+=1
			break
print(cnt)

N = int(input())
T = []
try:
	while True:
		t = input()
		t=int(t)
		T_temp=[]
		for t_ in range(t) :
			temp = list(map(int,input().split()))
			T_temp.append(temp)
		T.append(T_temp)
except EOFError:
	pass
    
def check_Contradiction(true_list):
    S = {}
    for n in range(N):
        if n in true_list:
            S[n]=set([1])
        else:
            S[n]=set([0])

    for t in true_list:
        for T_ in T[t]:
            S[T_[0]-1].add(T_[1])
    ok=True
    for s in S.keys():
        if len(S[s])!=1:
            ok='False'
            break

    return ok

ok_max = -1
for i in range(2**N):
#     print('=====',i)
    true_list=[]
    for j in range(N):
        if i>>j&1 ==True:
            true_list.append(j)
#     print(true_list)
#     print(check_Contradiction(true_list))
            
    if check_Contradiction(true_list)==True:
        if ok_max < len(true_list):
            ok_max=len(true_list)
            
print(ok_max)
n=int(input())
lst=["1","2","3","4","5","6","7","8","9","10","11","12","13"]
#S_list=lst
#H_list=lst
#C_list=lst
#D_list=lst
S_list=["1","2","3","4","5","6","7","8","9","10","11","12","13"]
H_list=["1","2","3","4","5","6","7","8","9","10","11","12","13"]
C_list=["1","2","3","4","5","6","7","8","9","10","11","12","13"]
D_list=["1","2","3","4","5","6","7","8","9","10","11","12","13"]
for i in range(n):
	Del=map(str,raw_input().split())
	if Del[0]=="S":
		S_list.remove(Del[1])
        elif Del[0]=="H": 
                H_list.remove(Del[1]) 
        elif Del[0]=="C": 
                C_list.remove(Del[1]) 
        elif Del[0]=="D": 
                D_list.remove(Del[1]) 
S=map(int,S_list)
H=map(int,H_list)
C=map(int,C_list)
D=map(int,D_list)
#
for i in range(len(S)):
	print "S "+str(S[i])
for i in range(len(H)):
        print "H "+str(H[i])
for i in range(len(C)):
        print "C "+str(C[i])
for i in range(len(D)):
        print "D "+str(D[i])
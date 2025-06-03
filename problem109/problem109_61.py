N=int(input())
A=0
W=0
T=0
R=0
for i in range(N):
    st=input()
    if st=="AC":
        A+=1
    elif st=="WA":
        W+=1
    elif st=="TLE":
        T+=1
    else:
        R+=1
print("AC x "+str(A))
print("WA x "+str(W))
print("TLE x "+str(T))
print("RE x "+str(R))
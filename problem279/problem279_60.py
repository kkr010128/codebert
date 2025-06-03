N=int(input())
S=list(input())
if N%2!=0:
    print("No")
else:
    s_1=S[:int(N/2)]
    s_2=S[int(N/2):N]
    if s_1==s_2:
        print("Yes")
    else:
        print("No")
  
  
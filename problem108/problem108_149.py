#A
N=input()
if len(N) >= 4:
    N_3=N[-3:]
    ans=1000-int(N_3) if int(N_3) !=0 else 0
else:
    ans=1000-int(N)
print(ans)
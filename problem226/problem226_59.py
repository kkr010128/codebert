r=input().split()
H=int(r[0])
N=int(r[1])
data_pre=input().split()
data=[int(s) for s in data_pre]
if sum(data)>=H:
    print("Yes")
else:
    print("No")
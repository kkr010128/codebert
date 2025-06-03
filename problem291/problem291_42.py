a1=input()
a2=[i for i in a1.split()]
a3,a4=[a2[i] for i in (0,1)]
A,B=int(a3),int(a4)
print(max(0,A-2*B))
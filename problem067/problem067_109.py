n=int(input())
T,H=0,0
for i in range(n):
    t_card,h_card=input().split()
    if t_card>h_card:
        T+=3
    elif t_card<h_card:
        H+=3
    else:
        T+=1
        H+=1
print(str(T)+" "+str(H))
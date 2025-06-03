n=input()
t_p=0
h_p=0
for i in range(int(n)):
    t,h=input().split()
    a=sorted([t,h])
    if t == h:
        t_p+=1
        h_p+=1
    elif t  == a[1]:
        t_p+=3
    else:
        h_p+=3
print(t_p, h_p)
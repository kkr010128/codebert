a_1= [[0 for i in range(10)] for j in range(3)]
a_2= [[0 for i in range(10)] for j in range(3)]
a_3= [[0 for i in range(10)] for j in range(3)]
a_4= [[0 for i in range(10)] for j in range(3)]

def print_ninzu(a):
    print("",end=" ")
    print(" ".join(map(str,a[0])))
    print("",end=" ")
    print(" ".join(map(str,a[1])))
    print("",end=" ")
    print(" ".join(map(str,a[2])))

n = int(input())
for i in range(n):
    com = list(map(int,input().split()))
    if com[0] == 1:
        a_1[com[1]-1][com[2]-1] += com[3]
    if com[0] == 2:
        a_2[com[1]-1][com[2]-1] += com[3]
    if com[0] == 3:
        a_3[com[1]-1][com[2]-1] += com[3]
    if com[0] == 4:
        a_4[com[1]-1][com[2]-1] += com[3]    
        
print_ninzu(a_1)
print("####################")
print_ninzu(a_2)
print("####################")
print_ninzu(a_3)
print("####################")
print_ninzu(a_4)
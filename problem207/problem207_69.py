
A1=input()

A2=input()

A3=input()

#N=int(N)

list1 = A1.split()

list1 = [int(i) for i in list1]


list2 = A2.split()

list2 = [int(i) for i in list2]


list3 = A3.split()

list3 = [int(i) for i in list3]


N = input()

N=int(N)

num=[]

for i in range(N):
    num.append(int(input()))


T1 = all([(i in num ) for i in list1])

T2 = all([(i in num ) for i in list2])

T3 = all([(i in num ) for i in list3])

T4 = all([(list1[0] in num),(list2[0] in num),(list3[0] in num)])

T5 = all([(list1[1] in num),(list2[1] in num),(list3[1] in num)])

T6 = all([(list1[2] in num),(list2[2] in num),(list3[2] in num)])

T7 = all([(list1[0] in num),(list2[1] in num),(list3[2] in num)])

T8 = all([(list1[2] in num),(list2[1] in num),(list3[0] in num)])

if (any([T1,T2,T3,T4,T5,T6,T7,T8])) == True:
    print("Yes")
else:
    print("No")
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 20:50:35 2020

@author: akros
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 16:51:42 2020

@author: akros
"""

A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A3 = list(map(int, input().split()))

N = int(input())
a = []

for i in range(N):
    a.append(int(input()))
   
    if A1[0] == a[i]:
        A1[0] = True
    elif a[i] == A1[1]:
        A1[1] = True
    elif a[i] == A1[2]:
        A1[2] = True
    elif a[i] == A2[0]:
        A2[0] = True
    elif a[i] == A2[1]:
        A2[1] = True
    elif a[i] == A2[2]:
        A2[2] = True
    elif a[i] == A3[0]:
        A3[0] = True
    elif a[i] == A3[1]:
        A3[1] = True
    elif a[i] == A3[2]:
        A3[2] = True


if A1[0] == True and A1[1] == True and A1[2] == True:
    print("Yes")
elif A1[0] == True and A2[0] == True and A3[0] == True:
    print("Yes")
elif A1[0] == True and A2[1] == True and A3[2] == True:
    print("Yes")
elif A1[1] == True and A2[1] == True and A3[1] == True:
    print("Yes")
elif A1[2] == True and A2[2] == True and A3[2] == True:
    print("Yes")
elif A2[0] == True and A2[1] == True and A2[2] == True:
    print("Yes")
elif A3[0] == True and A3[1] == True and A3[2] == True:
    print("Yes")
elif A1[2] == True and A2[1] == True and A3[0] == True:
    print("Yes")
    
else:             
    print("No")

    
    
    

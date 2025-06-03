a,b,c = map(int, input().split())

a_b = a==b
b_c = b==c
a_c = a==c

if a_b and b_c and a_c:    
    print("No")

elif a_b or b_c or a_c:
    print("Yes") 

else:
    print("No")
a,b,c,d=map(int,input().split())
temp_q=(c+b-1)//b
temp_g=(a+d-1)//d
if temp_q>temp_g:
    print("No")
else:
    print("Yes")
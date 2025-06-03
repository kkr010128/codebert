A,B,C=map(int,input().split())
if 4*A*B<(C-A-B)*(C-A-B) and C>A+B:
    print("Yes")
else:
    print("No")

h,n=map(int, input().split())
a_list=[int(i) for i in input().split()]

if sum(a_list)>=h:
    print("Yes")
else:
    print("No")
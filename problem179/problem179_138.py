n,m=map(int, input().split())
a_list=[int(i) for i in input().split()]

a_list.sort(reverse=True)
#print(a_list)

standard=sum(a_list)/(4*m)

#print(a_list[m-1])
#print(standard)
if a_list[m-1]<standard:
    print("No")
    
else:
    print("Yes")

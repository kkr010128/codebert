N=int(input())

max_x=int(N**0.5)
ans_list=[0]*N

for x in range(1,max_x):
    for y in range(1,max_x):
        for z in range(1,max_x):
            s=x**2+y**2+z**2+x*y+y*z+z*x
            if s<=N:
                ans_list[s-1]+=1
                
for i in range(N):
    print(ans_list[i])
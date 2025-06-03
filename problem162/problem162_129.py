n,m=map(int,input().split())
left=m//2
right=(m+1)//2

for i in range(left):
    print(i+1,2*left+1-i)


for i in range(right):
    print(2*left+1+i+1,2*left+1+2*right-i)


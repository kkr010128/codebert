a,b,c = map(int,input().split(" "))
list_divisor=[i for i in range(1,c+1) if c % i == 0]
cnt = [j for j in range(a,b+1) if j in list_divisor]
print(len(cnt))


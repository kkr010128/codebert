moto = input()
num = int(input())

for i in range(num):
    order = input().split()
    if order[0] == "print":
        m,n=int(order[1]),int(order[2])
        print(moto[m:n+1])
    elif order[0] == "reverse":
        m,n=int(order[1]),int(order[2])
        moto = moto[:m]+moto[m:n+1][::-1]+moto[n+1:]
    elif order[0] == "replace":
        m,n,l=int(order[1]),int(order[2]),order[3]
        moto = moto[:m]+order[3]+moto[n+1:]
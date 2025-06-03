temp = input()
n = int(input())
for _ in range(n):
    order,a,b,*value = input().split()
    a = int(a)
    b = int(b)

    if order == "print":
        print(temp[a:b+1])
    elif order == "reverse":
        rev = temp[a:b+1]
        temp = temp[:a] + rev[::-1] + temp[b+1:]
    else:#replace
        temp = temp[:a] + value[0] + temp[b+1:]

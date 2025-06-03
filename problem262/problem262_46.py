def my_eval(ar,str):
    res = True
    n = len(str)
    # print(n)
    # print("start")
    for i in range(n):
        # print(i)

        if(ar[str[i][0]] == 1):
            # print(str[i][0])
            # print(str[i][1])
            # print(str[i][2])
            # print(ar[str[i][1]-1])
            # print(ar[str[i][1]-1] == str[i][2])
            # print(ar)
            # print()
            if(ar[str[i][1]] != str[i][2]):
                res = False
    # print("end")
    # print()
    return res

if __name__ == "__main__":

    # 全探索
    n = int(input())
    str = []
    for i in range(n):
        a = int(input())

        for j in range(a):
            x = list(map(int,input().split()))
            x.insert(0,i+1)
            str.append(x)
    ar = [0] * (n+1)
    res = 0
    # print(str)
    count = 0
    for i in range(2**n):
        count = 0
        for j  in range(n):
            if(i >> j & 1 == 1):
                ar[j+1] = 1
                count += 1
            else:
                ar[j+1] = 0
        # print(ar)
        if(my_eval(ar,str)):
            res = max(res,count)
    print(res)


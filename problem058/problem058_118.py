while True:
    n, x = map(int,input().split())
    count=0
    if n == x == 0:
        break
    else:
        ls = []
        for i in range(1,n+1):
            ls.append(i)

        for s in ls:
            num1 = s

            for j in ls:
                if num1 == j:
                    break
                else:
                    num2 = j
                    if x < num1+num2:
                        break

                for k in ls:
                    if num1 == k:
                        break
                    elif num2 == k:
                        break
                    elif num1+num2+k == x:
                        count+=1
                    else:
                        pass
    print(count)
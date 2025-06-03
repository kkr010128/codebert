
n = int(input())

ans = 0
count = 0

a, b, c = 1, 1, 1

while a <= n:

    # print("A : {0}".format(a))
    # print("追加パターン : {0}".format( (n // a) ))

    if a == 1 :
        ans =  ans + ( (n // a) - 1)
    else :

        if n // a == 1 :
            ans = ans + 1
        else :

            if n % a == 0 :
                ans = ans + ( (n // a) - 1)
            else :
                ans = ans + ( (n // a) )

            



    # if n % a == 0 :
    #     ans = ans + ( (n / a) - 1 )
    # else :
    #     ans = ans + ( (n // a) - 1 )

    # ans = ans + (n / a) - 1

    # print("A : {0}".format(a))

    # while a * b < n:

    #     print("B : {0}".format(b))

    #     ans += 1

    #     b += 1
    #     c = 1

    a += 1
    b, c = 1, 1

# print("計算実行回数 : {0}".format(count))
print(ans - 1)
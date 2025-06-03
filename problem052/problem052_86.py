def call(n):
    s = ""
    for i in range(1,n+1):
        if i%3 == 0:
            s += " {0}".format(i)
        else:
            x = i
            while x > 0:
               if x%10 == 3:
                   s += " {0}".format(i)
                   break
               x = x // 10
    print(s)

m = int(input())
call(m)
n, m = map(int, input().split())

if n % 2 == 0:
    i = 1
    while i <= m:
        a_i = str(i)
        
        if i <= (n - 2) // 4:
            b_i = str(n - i)
        else:
            b_i = str(n - i - 1)
        
        print(a_i + " " + b_i)
        i += 1
        
elif n % 2 == 1:
    for i in range(1, m + 1):
        a_i = str(i)
        b_i = str(n - i)
        
        print(a_i + " " + b_i)

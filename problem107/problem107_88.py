
n = int(input())
x = input()

def popcount(ni):
    n_b = str(bin(ni))
    return n_b.count("1")

def ans(n,x):
    x_i = int(x, 2)
    x_orig = popcount(x_i)
    x_i_t = x_i % (x_orig+1)
    if x_orig != 1:
        x_i_b = x_i % (x_orig-1)
    else:
        x_i_b = x_i
    solve = 0
    for i in range(n):
        x_count = x_orig
        if x[i] == "0":
            x_count += 1
            solve = x_i_t + pow(2,n-1-i,x_count)
        else:
            x_count -= 1
            if x_count != 0:
                solve = x_i_b - pow(2,n-1-i,x_count)
            else:
                print(0)
                continue
        count = 0

        if x_count != 0 :
            solve = solve % x_count
            count+=1

        while solve > 0:
            solve = solve % popcount(solve)
            count+=1

        print(count)

    
ans(n,x)

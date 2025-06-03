#ABC 174 C
k = int(input())

sevens = [0] * k

sevens[0] = 7 % k

if k == 7 or k == 1:
    print(1)
    
else:
    for i in range(1, k):
        new = (sevens[i - 1] * 10 + 7) % k
        sevens[i] = new

        if new == 0:
            print(i + 1)
            break
    else:
        print(-1)
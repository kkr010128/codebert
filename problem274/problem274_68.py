n, m = map(int, input().split())
s = input()
 
x = n
roulette = []
while x > m:
    for i in range(m, 0, -1):
        if s[x-i] == '0':
            x -= i
            roulette.append(i)
            break
    else:
        print(-1)
        exit()
roulette.append(x)
roulette.reverse()
print(' '.join(map(str, roulette)))
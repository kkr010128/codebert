x,k,d = map(int, input().split())

if x == 0:
    if k % 2 == 1:
        x = d

elif x > 0:
    if x >= k*d:
        x -= k*d
    else:
        n = x//d
        x -= n*d
        k -= n

        if k%2 ==1:
            x -= d
else:
    if x <= -(k*d):
        x += k*d

    else:
        n = abs(x)//d
        x += n*d
        k -= n
        if k%2 ==1:
            x += d

print(abs(x))
def cnt_car(w, p):
    car = 1
    wi = 0
    for i in w:
        if (wi + i) <= p:
            wi += i
        else:
            car += 1
            wi = i
    return car

n, k = map(int, input().split())
w = [int(input()) for i in range(n)]
p = max(max(w), sum(w) // k)
while True:
    if cnt_car(w, p) <= k:
        print(p)
        break
    else:
        #print("failed: ", p, cnt_car(w, p))
        if cnt_car(w, p + 100) > k:
            p += 100
        else:
            p += 1

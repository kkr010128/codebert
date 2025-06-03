n,k = map(int,input().split())
w = []
for _ in range(n):
    w.append(int(input()))

def enough(p,k,w):
    count = 0
    in_truck = 0
    for x in w:
        if x > p:
            return False
        else:
            if in_truck + x > p:
                count += 1
                in_truck = x
            else:
                in_truck += x
    if in_truck > 0:
        count += 1
    return k >= count

maximum = sum(w)
minimum = 1

while True:
    if minimum == maximum:
        break
    else:
        tmpp = (maximum + minimum) // 2
        if enough(tmpp,k,w):
            maximum = tmpp
        else:
            minimum = tmpp + 1

print(minimum)

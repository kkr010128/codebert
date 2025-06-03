num = int(input())
xs  = [int(n) for n in input().split()]
ys  = [int(n) for n in input().split()]

def calc_distance(xs, ys, p):
    sums = sum([abs(x-y) ** p for x,y in zip(xs, ys)])
    return sums ** (1.0 / p)

for index in range(1,4):
    print(calc_distance(xs, ys, index))

print(max(abs(x-y) for x,y in zip(xs,ys)))

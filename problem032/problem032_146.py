# Distance II

dimension = int(input())
vectors = [[float(i) for i in input().rstrip().split()] for j in range(2)]
x = vectors[0]
y = vectors[1]

absoluteValues = [abs(x[k] - y[k]) for k in range(dimension)]
# print(absoluteValues)

# xとyのミンコフスキー距離を求める関数(a: 有限)
def mink(a):
    totalValue = 0
    for i in range(dimension):
        totalValue += absoluteValues[i] ** a
    distance = totalValue ** (1 / a)
    return distance

# xとyのChebyshev距離を求める関数
def chev():
    maxValue = 0
    for i in range(dimension):
        # print(absoluteValues[i])
        if absoluteValues[i] > maxValue:
            maxValue = absoluteValues[i]
    print(maxValue)


for i in range(1, 3 + 1):
    dist = mink(i)
    print(dist)
chev()


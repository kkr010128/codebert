import math

def average(l):
    return sum(l) / len(l)

def var(l):
    a = average(l)
    return sum(map(lambda x: (x-a)**2, l)) / len(l)

def std(l):
    return math.sqrt(var(l))

if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        l = [int(i) for i in input().split()]
        print("{0:.5f}".format(std(l)))
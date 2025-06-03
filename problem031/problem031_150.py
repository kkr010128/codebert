from math import sqrt
from statistics import mean

def standard_deviate(numbers):
    m = mean(numbers)
    b = sum([(n - m)**2 for n in numbers])
    return sqrt(b/len(numbers))

if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        students = list(map(int, input().split()))[0:n]
        print(standard_deviate(students))


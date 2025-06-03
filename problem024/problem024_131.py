def allocation():
    n, cars = map(int, input().split())
    weight = [int(input()) for i in range(n)]

    left = max(weight)
    right = sum(weight)

    while left < right:
        mid = (left + right) // 2

        if check(weight, cars, mid):
            right = mid
        else:
            left = mid + 1

    print(left)

def check(weight, cars, capacity):
    t = 0
    c = 1
    for w in weight:
        t += w
        if t > capacity:
            t = w
            c += 1

    if c <= cars:
        return True
    else:
        return False

if __name__ == '__main__':
    allocation()
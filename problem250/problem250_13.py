# 素数ならTrue、素数でなければFalseを返す
def is_prime(x):
    sqrt = int(x ** 0.5)
    for i in range(2, sqrt + 1):
        if x % i == 0:
            return False
    return True

x = int(input())

while(not is_prime(x)):
    x += 1

print(x)

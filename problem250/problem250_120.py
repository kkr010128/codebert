def is_prime(num: int) -> bool:
    # 6k +- 1 <= √n
    if num <= 1:
        return False

    if num <= 3:
        return True

    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i+2) == 0:
            return False
        i += 6

    return True


x = int(input())
for i in range(x,1000000):
    if is_prime(i):
        print(i)
        break

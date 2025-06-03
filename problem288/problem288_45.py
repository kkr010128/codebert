# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def make_divisors(n: int):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors, upper_divisors[::-1]



def resolve():
    import sys
    input = sys.stdin.readline

    n = int(input().rstrip())
    lower_divisors, _ = make_divisors(n)
    print(min(lower_divisor + (n // lower_divisor) - 2 for lower_divisor in lower_divisors))





if __name__ == "__main__":
    resolve()

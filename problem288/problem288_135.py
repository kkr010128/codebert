def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        tmp = []
        if n % i == 0:
            tmp.append(i)
            tmp.append(n//i)
        if(len(tmp)>0):
            divisors.append(sum(tmp))
    return divisors
def main5():
    n = int(input())
    k = make_divisors(n)
    print(min(k)-2)


if __name__ == '__main__':
    main5()

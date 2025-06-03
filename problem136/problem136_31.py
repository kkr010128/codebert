import sys
import collections


#https://python.ms/factorize/
def factorize(n):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    return fct

def main():
    input = sys.stdin.readline
    change_to_count_list = []
    for i in range(62):
        if i == 0:
            change_to_count_list.append(1)
        else:
            change_to_count_list.append(change_to_count_list[i-1]+i+1)
    N = int(input())
    yakusu_list = factorize(N)
    c = collections.Counter(yakusu_list)
    result = 0
    for count in c.values():
        for i in range(62):
            if change_to_count_list[i] == count:
                if i == 0:
                    result += 1
                    break
                else:
                    result += i + 1
                    break

            elif change_to_count_list[i-1] < count and change_to_count_list[i] > count:
                result += i
                break
    print(result)


if __name__ == '__main__':
    main()
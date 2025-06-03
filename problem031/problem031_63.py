from math import sqrt

def sd(nums):
    n   = len(nums)
    ave = sum(nums)/n

    return abs(sqrt(sum([(s - ave)**2 for s in nums])/n))

def main():
    while True:
        n = input()

        if n == '0':
            break

        nums = [int(x) for x in input().split()]
        print("{:f}".format(sd(nums)))

if __name__ == '__main__':
    main()

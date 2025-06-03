import math
def int_ceil(src, range):
    return int(math.ceil(src/float(range)) * range)

def main():
    week = int(input())
    debt = 100000
    for _ in range(week):
        risi = debt * 0.05
        debt = int_ceil(debt + risi, 1000)
    print(debt)

if __name__ == "__main__":
    main()

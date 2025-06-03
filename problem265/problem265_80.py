import math
def main2():
    n = int(input())
    x = int(math.ceil(n / 1.08))
    
    if int(x*1.08) == n:
        print(x)
    else:
        print(":(")

if __name__ == "__main__":
    main2()
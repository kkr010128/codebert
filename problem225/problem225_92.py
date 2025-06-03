import math
def main():
    h, a = list(map(int, input().split()))
    print(math.ceil(h/a))
    
if __name__ == '__main__':
    main()
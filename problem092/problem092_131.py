def main():
    x, k, d = map(int,input().split())
    abs_x = abs(x)
    times = abs_x // d
    if(times > k):
        print(abs_x - k * d)
    else:
        if((k - times) % 2 == 0):
            print(abs_x - times * d)
        else:
            print(abs(abs_x - (times + 1) * d))
if __name__ == '__main__':
    main()
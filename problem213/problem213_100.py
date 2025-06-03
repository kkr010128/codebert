def main():
    n = int(input())
    X = [int(x) for x in input().split()]
    ave_x = int(sum(X) / len(X))
    error_1 = 0
    error_2 = 0
    for x in X:
        error_1 += (x-ave_x) ** 2
        error_2 += (x-(ave_x+1)) ** 2
        min_e = min(error_1, error_2)
    print(min_e)
    
if __name__ == '__main__':
    main()
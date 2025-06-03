def Main(K):
    l = (1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51)
    return l[K-1]
                

def main():
    K = int(input())
    print(Main(K))

if __name__ == '__main__':
    main()
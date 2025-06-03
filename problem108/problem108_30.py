def main():

    N = int(input())
    if N % 1000 == 0: return 0
    else: return 1000 - N % 1000 

if __name__ == '__main__':
    print(main())

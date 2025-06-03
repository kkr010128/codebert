# -*-coding:utf-8

def main():

    while True:
        n, x = map(int, input().split())
        if ((n == 0) and (x == 0)):
            break

        count = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                for k in range(1, n+1):
                    if((i<j) and (j<k) and i+j+k == x):
                        count += 1

        print(count)

if __name__ == '__main__':
    main()
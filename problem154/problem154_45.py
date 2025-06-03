# coding=utf-8

if __name__ == '__main__':
    N, K = map(int, input().split())

    sunuke = [0] * N
    #print(sunuke)

    for i in range(K):
        D = int(input())
        li = list(map(int, input().split()))

        for j in range(D):
            sunuke[li[j] - 1] += 1
            #print(sunuke)

    print(sunuke.count(0))

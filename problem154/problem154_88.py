#import time

def main():
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for i in range(2*K)]
    sunuke = [0]*(N+1)
    for i in range(K):
        for j in matrix[2*i+1]:
            sunuke[j] += 1
    ans = sunuke.count(0) -1

    return ans

if __name__ == '__main__':
    #start = time.time()
    print(main())
    #elapsed_time = time.time() - start
    #print("経過時間:{}".format(elapsed_time * 1000) + "[msec]")
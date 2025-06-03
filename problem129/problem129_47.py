#import time

def main():
    N = int(input())
    As = list(map(int, input().split()))

    As.sort()
    amax = max(As) + 1
    lis = [True] * amax
    ans = 0

    for i in range(N-1):
        if lis[As[i]]:
            for j in range(As[i], amax, As[i]):
                lis[j] = False
            if As[i] < As[i+1]:
                ans += 1
    if lis[-1]:
        ans += 1

    return ans

if __name__ == '__main__':
    #start = time.time()
    print(main())
    #elapsed_time = time.time() - start
    #print("経過時間:{}".format(elapsed_time * 1000) + "[msec]")
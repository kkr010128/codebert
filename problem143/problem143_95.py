#import time

def main():
    K = int(input())
    S = input()
    if len(S) <= K:
        return S
    else:
        return S[:K] + "..."

if __name__ == '__main__':
    #start = time.time()
    print(main())
    #elapsed_time = time.time() - start
    #print("経過時間:{}".format(elapsed_time * 1000) + "[msec]")
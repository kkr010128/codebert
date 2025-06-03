#import time

def main():
    N, K = map(int, input().split())
    As = list(map(int, input().split()))
    As = [0]+As
    ikisaki = As[1]
    aru = {1}
    itta = [1]
    imaitta = 1
  
    while not ikisaki in aru:
        imaitta = ikisaki
        ikisaki = As[ikisaki]
        itta.append(imaitta)
        aru.add(imaitta)
    ind = itta.index(ikisaki)
    kurikaesi = itta[ind:]
    itidokiri = itta[:ind]
    ans = itidokiri[K] if len(itidokiri) > K else kurikaesi[(K-len(itidokiri))%len(kurikaesi)]


    return ans

if __name__ == '__main__':
    #start = time.time()
    print(main())
    #elapsed_time = time.time() - start
    #print("経過時間:{}".format(elapsed_time * 1000) + "[msec]")
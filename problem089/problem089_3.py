def main():
    H,W,M = map(int,input().split())
    dict_ichi = {}
    dict_H = {key:0 for key in range(1,H+1,1)}
    dict_W = {key:0 for key in range(1,W+1,1)}
    for i in range(M):
        h,w = map(int,input().split())
        dict_H[h] += 1
        dict_W[w] += 1
        dict_ichi[(h,w)] = 1
    #print(list)
    maxH = max(dict_H.values())
    maxW = max(dict_W.values())
    wi = [i for i in range(1,W+1,1) if dict_W[i] == maxW]
    #print(retuH,gyoW,wi)
    for h in [i for i in range(1,H+1,1) if dict_H[i] == maxH]:
        for w in wi:
            if (h,w) not in dict_ichi:
                return maxH + maxW
    return maxH + maxW -1

print(main())

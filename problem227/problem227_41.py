if __name__ == '__main__':
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H = sorted(H)[::-1]
    cnt = 0
    for h in H:
        if K>0:
            K -= 1
        else:
            cnt += h
    
    print(cnt)
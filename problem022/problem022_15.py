def main():
    n = int(input())
    s = list(map(int, input().split())) 
    q = int(input())
    t = list(map(int, input().split()))
    
    # 集合的なら
    # res = len(set(s) & set(p))
    # print(res)
    # 線形探索なら
    cnt = 0
    for i in t:
        if i in s:
            cnt += 1
    print(cnt)
    
if __name__ == '__main__':
    main()

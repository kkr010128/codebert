def main():
    n = int(input())
    a = list(map(int,input().split()))
    dic = {}
    for i in range(n):
        if not a[i] in dic.keys():
            dic[a[i]] = 1
        else:
            dic[a[i]] += 1
    s = 0
    for k in dic.keys():
        s += dic[k] * k
    q = int(input())
    for i in range(q):
        b,c = map(int,input().split())
        if b in dic.keys():
            cnt = dic[b]
        else:
            cnt = 0
        dic[b] = 0
        if c in dic.keys():
            dic[c] += cnt
        else:
            dic[c] = cnt
        s = s + cnt * (c-b)
        print(s)

if __name__ == "__main__":
    main()

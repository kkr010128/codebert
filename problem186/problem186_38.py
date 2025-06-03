# 改善1：sys入力
# 改善2：ifで分岐させるより、あとから個別対応した方が分岐を毎回やらないですむ？


import sys
input=sys.stdin.readline

def main():
    k,n = map(int, input().split())
    s = list(map(int, input().split()))
    l = []
    for i in range(1,n):
        a = s[i] - s[i-1]
        l.append(a)
    l.append(k - (s[-1] - s[0]))
    print(k - max(l))

if __name__ == '__main__':
    main()

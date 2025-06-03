# 解説を見た。
# https://at274.hatenablog.com/entry/2020/01/24/060000

def main():
    num = int(input())
    counter = [[0] * 10 for _ in range(10)]
    for x in range(1, num + 1):
        x = str(x)
        head = int(x[0])
        tail = int(x[-1])
        counter[head][tail] += 1
    gen = (counter[head][tail] * counter[tail][head]
           for head in range(1, 10)
           for tail in range(1, 10))
    print(sum(gen))


if __name__ == '__main__':
    main()

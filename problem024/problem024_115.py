import sys
input = sys.stdin.readline


def main():
    n, k = map(int, input().split())

    products = [int(input()) for _ in range(n)]

    left = 1
    right = 10000 * 100000  # 最大重量 × 最大貨物数

    while left < right:
        mid = (left + right) // 2
        # print("left:{}".format(left))
        # print("right:{}".format(right))
        # print("mid:{}".format(mid))

        v = allocate(mid, k, products)
        # print("count:{}".format(v))

        if n <= v:
            right = mid
        else:
            left = mid + 1

    print(right)


def allocate(capacity, truckNum, products):
    # print("===== start allocation capacity:{}======".format(capacity))
    v = 0
    tmp = 0
    truckNum -= 1
    while len(products) > v:
        product = products[v]

        # print("tmp weight:{}".format(tmp))
        # print("product weight:{}".format(product))

        if product > capacity:
            # print("capacity over")
            # そもそも１個も乗らない時避け
            return 0

        if tmp + product <= capacity:
            # 同じトラックに積み続ける
            tmp += product
        else:
            # 新しいトラックがまだあればつむ
            if truckNum > 0:
                # print("new truck")
                truckNum -= 1
                tmp = product
            else:
                return v

        v += 1

    return v


if __name__ == '__main__':
    main()


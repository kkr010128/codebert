# D - Road to Millionaire


def million(n, a):
    wallet = 1000
    i = 0
    while i < n - 1:
        highest_price = a[i]
        cheapest_price = a[i]
        # 直近の最高値と最安値を取得する
        for j in range(i + 1, n):
            if highest_price > a[j]:
                break
            if highest_price < a[j]:
                highest_price = a[j]
            if cheapest_price > a[j]:
                cheapest_price = a[j]
        if highest_price > cheapest_price:
            # 取引する
            stock = wallet // cheapest_price
            wallet = wallet - stock * cheapest_price
            wallet = wallet + stock * highest_price
            i = j
        else:
            i += 1
    return wallet


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(million(n, a))

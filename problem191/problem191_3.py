def maximum_volume():
    """
    立方体に近いほど体積が大きくなる
    """
    # 入力
    L = int(input())
    # 処理
    one_side = L / 3
    # 体積
    return one_side ** 3

result = maximum_volume()
print(result)
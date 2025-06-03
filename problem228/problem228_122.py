import math

def caracal_vs_monster():
    """
    2**0 個                       5
           　                 /       \
    2**1 個               2.5         2.5
           　             /     \      /    \
    2**2 個           1.25   1.25  1.25   1.25
          　          /    \   /   \  /  \   /   \
    2**3 個       0.625  0.625 ...
    """
    # 入力
    H = int(input())
    # H / 2 の何回目で1になるか
    count = int(math.log2(H))
    # 攻撃回数
    attack_count = 0
    for i in range(count+1):
        attack_count += 2 ** i
    return attack_count

result = caracal_vs_monster()
print(result)
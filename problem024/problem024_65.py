import sys

n, k = tuple(map(int, input().split()))

lower_p = 0
w_list = []
for _ in range(n):
    w = int(sys.stdin.readline())
    lower_p = w if w > lower_p else lower_p
    w_list.append(w)
    
def get_possible_n(p):
    """最大積載重量を p としたときに、所与のトラック台数 k で処理可能な荷物の数

    所与の荷物数 n のうち、いくつ処理可能かを返す。荷物の重量と順序に依存し、
    （弱い）単調増加関数である。これが返す最大値は n である。
    """
    pos_n = 0
    for _ in range(k):
        acc_w = 0
        while pos_n < n:
            if acc_w + w_list[pos_n] <= p:
                acc_w += w_list[pos_n]
                pos_n += 1
            else:
                break
        else:
            break
    return pos_n

# upper_p は、get_possible_n(upper_p) が確実に n を返すことが保証される値。
upper_p = lower_p * n // k + lower_p

def b_search(lower_p, upper_p):
    while lower_p < upper_p:
        mid_p = (lower_p + upper_p) // 2
        if get_possible_n(mid_p) < n:
            lower_p = mid_p + 1
        else:
            upper_p = mid_p
    return lower_p

print(b_search(lower_p, upper_p))


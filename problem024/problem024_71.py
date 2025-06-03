from typing import List


def is_able_to_load(tmp_P: int, weights: List[int], track_num_max: int) -> bool:
    track_num = 1
    tmp_sum = 0
    for w in weights:
        if tmp_sum + w <= tmp_P:
            tmp_sum += w
        else:
            track_num += 1
            tmp_sum = w
            if track_num > track_num_max:
                return False
    return True


if __name__ == "__main__":
    n, k = map(lambda x: int(x), input().split())
    weights = list(map(lambda x: int(input()), range(n)))

    left_weight = max(weights)
    right_weight = 10000 * 100000
    mid_weight = (left_weight + right_weight) // 2
    optimal_P = right_weight

    while left_weight <= right_weight:
        if is_able_to_load(mid_weight, weights, k):
            optimal_P = mid_weight
            right_weight = mid_weight - 1
        else:
            left_weight = mid_weight + 1

        mid_weight = (left_weight + right_weight) // 2

    print(f"{optimal_P}")


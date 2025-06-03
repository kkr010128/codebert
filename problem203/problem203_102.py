# coding: utf-8
import math

def main():
    a, b = map(int, input().split())
    tmp_a_min = math.ceil(a / 0.08)
    tmp_a_max = math.ceil((a+1) / 0.08)
    tmp_b_min = math.ceil(b / 0.1)
    tmp_b_max = math.ceil((b+1) / 0.1)
    tmp_a = list(range(tmp_a_min, tmp_a_max))
    tmp_b = list(range(tmp_b_min, tmp_b_max))
    tmp = set(tmp_a) & set(tmp_b)
    if len(tmp) != 0:
        print(min(tmp))
    else:
        print(-1)
main()
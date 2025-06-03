import sys

def get_maximum_profit():
    element_number = int(input())
    v0 = int(input())
    v1 = int(input())

    min_v = min(v0, v1)
    max_profit = v1-v0

    for v in map(int, sys.stdin.readlines()):
        max_profit = max(max_profit, v-min_v)
        min_v = min(min_v, v)

    print(max_profit)

if __name__ == '__main__':
    get_maximum_profit()
from sys import stdin
from math import ceil

def is_stackable(k,p,w):
    if max(w) > p:
        return False
    s = w[0]
    count = len(w)
    for i in range(1, len(w)):
        if s + w[i] <= p:
            s += w[i]
            count -= 1
        else:
            s = w[i]
    return k >= count

def main():
    n,k = map(int, stdin.readline().split())
    w = [int(line) for line in stdin.readlines()]
    
    left = max(max(w), ceil(sum(w)/k))
    right = (max(w) * ceil(n/k)) + 1
    while True:
        mid = int((left + right) / 2)
        if is_stackable(k, mid, w):
            if not is_stackable(k, mid - 1, w):
                print(mid)
                break
            right = mid
        else:
            if is_stackable(k, mid + 1, w):
                print(mid + 1)
                break
            left = mid + 1

main()

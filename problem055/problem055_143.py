if __name__ == '__main__':
    nums = [[[0 for r in range(10)] for f in range(3)] for b in range(4)]
    n = int(input())
    for i in range(n):
        b, f, r, v = [int(i) for i in input().split()]
        nums[b-1][f-1][r-1] += v
    for b in range(4):
        for f in range(3):
            print(' ' + ' '.join([str(i) for i in nums[b][f]]))
        if b == 3: break
        print('#'*20)
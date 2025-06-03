# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_A
import sys

nums_len = int(sys.stdin.readline())
nums_str = sys.stdin.readline().split(' ')
nums = map(int, nums_str)

print ' '.join(map(str, nums))
for i in range(1, nums_len):
    for j in reversed(range(1, i + 1)):
        if nums[j] < nums[j - 1]:
            v = nums[j]
            nums[j] = nums[j - 1]
            nums[j - 1] = v
    print ' '.join(map(str, nums))
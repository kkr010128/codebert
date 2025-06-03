# coding=utf-8

inputs = raw_input().rstrip().split()
nums = [int(x) for x in inputs]
print ' '.join([str(x) for x in sorted(nums)])
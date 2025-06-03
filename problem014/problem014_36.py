def bubbleSort(list_, n):
    count = 0
    for i in xrange(n):
        for j in xrange(n-1, i, -1):
            if list_[j] < list_[j - 1]:
                list_[j], list_[j - 1] = list_[j - 1], list_[j]
                count += 1

    return count

n = input()
nums = map(int, raw_input().split())
count = bubbleSort(nums, n)
print ' '.join(map(str, nums))
print count
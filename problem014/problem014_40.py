def bubbleSort(list_, n):
    list_ = list_[:]
    count = 0
    for i in xrange(n):
        for j in xrange(n-1, i, -1):
            if list_[j] < list_[j - 1]:
                list_[j], list_[j - 1] = list_[j - 1], list_[j]
                count += 1

    return list_, count

n = input()
nums = map(int, raw_input().split())
sorted_, count = bubbleSort(nums, n)
print ' '.join(map(str, sorted_))
print count
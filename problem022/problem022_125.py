n1 = int(input())
nums1 = list(map(int, input().split()))
n2 = int(input())
nums2 = list(map(int, input().split()))

def linear_search(nums1, n1, key):
    nums1[n1] = key
    index = 0
    while nums1[index] != key:
        index += 1
    return index != n1

output = 0
nums1.append(None)
for key in nums2:
    if linear_search(nums1, n1, key):
        output += 1

print(output)

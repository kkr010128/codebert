import math
import collections
n, k = map(int, input().split())
W = collections.deque()
for i in range(n):
    W.append(int(input()))
left = max(math.ceil(sum(W) / k), max(W))
right = sum(W)
center = (left + right) // 2
# print('------')
while left < right:
    i = 1
    track = 0
    # print(center)
    for w in W:
        # if center == 26:
        #     print('track: ' + str(track))
        track += w
        if track > center:
            track = w
            i += 1
            if i > k:
                left = center + 1
                break
    else:
        right = center
    center = (left + right) // 2
print(center)

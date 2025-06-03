N = int(input())
height = [int(i) for i in input().split()]
box = [0]

for x in range(1 ,N):
    if(height[x] >= height[x-1] + box[x-1]):
        box.append(0)
    if(height[x] < height[x-1] + box[x-1]):
        box.append(- height[x] + height[x-1] + box[x-1])

sum = 0
for t in box:
    sum += t
print(sum)
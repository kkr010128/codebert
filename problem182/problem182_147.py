# input
N, K, C = map(int, input().split())
S = input()

# process
l = [i+1 for i in range(N) if S[i] == 'o']
left = [l[0]]
right = [l[-1]]
for i in range(1, len(l)):
    if l[i] > left[-1]+C:
        left.append(l[i])
    if l[-i-1] < right[-1]-C:
        right.append(l[-i-1])

# output
# print(l)
# print(left)
# print(right)
if len(left) == K:
    for i in range(len(left)):
        if left[i] == right[-i-1]:
            print(left[i])

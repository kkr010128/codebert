n = int(input())
num_list = list(map(int, input().split()))

sets = set(num_list)

if len(num_list) == len(sets):
    ans = 'YES'
else:
    ans = 'NO'

print(ans)
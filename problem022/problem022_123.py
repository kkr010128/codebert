def linear_search(num_list,target):
    for num in num_list:
        if num == target:
            return 1
    return 0

n = input()
num_list = list(map(int,input().split()))
q = input()
target_list = list(map(int,input().split()))
ans = 0

for target in target_list:
    ans += linear_search(num_list,target)
print(ans)

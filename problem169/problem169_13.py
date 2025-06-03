n = int(input())
bosses = list(map(int, input().split()))

ans_list = [0]*n
for boss in bosses:
    ans_list[boss-1] += 1

for ans in ans_list:
    print(ans)
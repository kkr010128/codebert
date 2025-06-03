n = int(input())
num_list = list(map(int, input().split()))

ans_list = [0]*n
for i, j in enumerate(num_list):
    ans_list[j-1] = str(i+1)

ans = ' '.join(ans_list)
print(ans)
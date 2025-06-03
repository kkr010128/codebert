S = list(input())
L = len(S)
count = 0
count_minus = [0] * L
for i in range(L):
    if S[i] == ">":
        count = 0
    else:
        count += 1
    count_minus[i] = count

count = 0
count_plus = [0] * L
for i in reversed(range(L)):
    if S[i] == "<":
        count = 0
    else:
        count += 1
    count_plus[i] = count

result_list = [0] * (L-1)
for i in range(len(result_list)):
    result_list[i] = max(count_minus[i], count_plus[i+1])

result = sum(result_list) + count_minus[L-1] + count_plus[0] 
print(result)
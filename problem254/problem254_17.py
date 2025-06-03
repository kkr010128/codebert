not_ans = []
not_ans.append(int(input()))
not_ans.append(int(input()))
for i in range(1, 4):
    if i not in not_ans:
        print(i)
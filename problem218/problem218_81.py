n = int(input())

# 入力データ受取り時に、辞書に追加していくやり方
s_dict = {}
for i in range(n):
    s = input()    
    if s not in s_dict:
        s_dict[s] = 1
    s_dict[s] += 1

max_value = max(s_dict.values())
ans = []
for key, value in s_dict.items():
    if value == max_value:
        ans.append(key)

ans.sort()
for i in ans:
    print(i)
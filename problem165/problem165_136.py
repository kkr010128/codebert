a= int(input())
ans_list = []
for i in range(a):
    ans_list.append(input())
print(len(list(set(ans_list))))
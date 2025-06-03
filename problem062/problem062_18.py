num = []
ans = []
while True:
    num = map(int,raw_input())
    if num == list([0]):
        break
    ans.append(sum(num))

for i in range(len(ans)):
    print ans[i]
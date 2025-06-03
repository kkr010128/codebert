s = input()
q = int(input())
flag = True
head = '' # 最終的に先頭に追加されている文字
end = '' # 最終的に末尾に追加されている文字

for i in range(q):
    que = [i for i in input().split()]
    if que[0] == '1':
        flag ^= True # Trueなら通常，Falseは反転状態
    elif que[0] == '2' and flag is True:
        if que[1] == '1':
            head = que[2] + head
        elif que[1] == '2':
            end = end + que[2]
    elif que[0] == '2' and flag is False:
        if que[1] == '1':
            end = end + que[2]
        elif que[1] == '2':
            head = que[2] + head
s = head+s+end
if flag is False:
    s = s[::-1]
print(s)
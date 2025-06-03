dic = {}
l = []
n = int(input())
for i in range(n):
    s = input()

#sが新規キーか否かで操作を変える
    if s in dic:
        dic[s] += 1
#新規ではないならvalueを1増やす
    else:
        dic[s] = 1
          
m = max(dic.values())

for i in dic:
    if dic[i] == m:
        l += [i]

print(*sorted(l))
import sys
s = input()
k = int(input())
n = len(s)
all_same = True
for i in range(n-1):
    if s[i] != s[i+1]:
        all_same = False
if all_same:
    print((n*k)//2)
    sys.exit()
head_same = 1
for i in range(n-1):
    if s[i] == s[i+1]:
        head_same += 1
    else:
        break
tail_same = 1
for i in range(n-1,0,-1):
    if s[i] == s[i-1]:
        tail_same += 1
    else:
        break
head_tail_same = 0
if s[0] == s[-1]:
    head_tail_same = head_same + tail_same
def return_internal_same(ls):
    i = 0
    same_count = 1
    return_value = 0
    while i < len(ls)-1:
        if ls[i] != ls[i+1]:
            i += 1
            return_value += same_count // 2
            same_count = 1
            continue
        else:
            same_count += 1
            i += 1
    return_value += same_count // 2
    return return_value
# head_tial_sameがあるかどうかで場合わけ
if head_tail_same > 0:
    ans = head_same//2 + tail_same//2
    ans += (k-1) * (head_tail_same//2)
    ans += k*(return_internal_same(s[head_same:n-tail_same]))
else:
    ans = k*(head_same//2 + tail_same//2)
    ans += (k-1) * (head_tail_same//2)
    ans += k*(return_internal_same(s[head_same:n-tail_same]))
print(ans)
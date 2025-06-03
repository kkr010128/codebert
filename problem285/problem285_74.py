# AGC040
# A
# ><
import itertools

s_list = input()

n = len(s_list) + 1
a_list = [0]*n
tmp_list = [0]*n

gr = itertools.groupby(s_list)

idx = 0
_tmp = 0
for key, group in gr:
    _num = sum(1 for _ in group)
    if key == "<":
        a_list[idx:idx+_num+1] = list(range(_num+1))
    else:
        a_list[idx] = max(_tmp,_num)
        a_list[idx+1:idx+_num] = list(range(_num-1,0,-1))
        tmp_list[idx] = _num
    idx += _num
    _tmp = _num

# print(a_list)
# print(tmp_list)
print(sum(a_list))    
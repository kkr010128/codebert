#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_B&lang=jp
def merge(target_list, left_index, right_index):
    global count
    mid_index = (left_index + right_index) // 2
    l = target_list[left_index:mid_index] + [pow(10,9) + 1]
    r = target_list[mid_index:right_index] + [pow(10,9) + 1]
    l_target = 0
    r_target = 0
    #print(left_index, right_index, mid_index, l,r)
    for k in range(left_index, right_index):
        count += 1
        if l[l_target] < r[r_target]:
            target_list[k] = l[l_target]
            l_target += 1
        else:
            target_list[k] = r[r_target]
            r_target += 1
    #print(target_list)
def merge_sort(target_list, left_index, right_index):
    if left_index + 1 < right_index:
        mid_index = (left_index + right_index) // 2

        merge_sort(target_list, left_index, mid_index)
        merge_sort(target_list, mid_index, right_index)
        merge(target_list, left_index, right_index)
    
if __name__ == "__main__":
    l = input()
    target_list = [int(a) for a in input().split()]
    global count
    count = 0
    merge_sort(target_list, 0, len(target_list))
    print(" ".join([str(n) for n in target_list]))
    print(count)
# -*- coding: utf-8 -*-

N = int(input().strip())
S_list = [input().strip() for _ in range(N)]
#-----

def count_brackets(brackets):
    L = R = 0
    L_rev = R_rev = 0
    max_R = -float("inf")
    max_L = -float("inf")
    
    
    for i in range(len(brackets)):
        if brackets[i] == "(":
            L += 1
        else:  # brackets[i] == ")"
            R += 1
            max_R = max(max_R, R - L)
        
        if brackets[len(brackets)-1-i] == "(":
            L_rev += 1
            max_L = max(max_L, L_rev - R_rev)
        else:  # brackets[len(brackets)-1-i] == ")"
            R_rev += 1
    
    if max_L < 0: max_L = 0
    if max_R < 0: max_R = 0
    
    return max_L, max_R


tmp_cnt1 = []  #  the number of "("  >=  the number of ")"
tmp_cnt2 = []  #  the number of "("  <   the number of ")"

for S in S_list:
    cnt_L,cnt_R = count_brackets(S)

    if cnt_L == cnt_R == 0:
        continue
    
    if cnt_L >= cnt_R:
        tmp_cnt1.append( (cnt_L,cnt_R) )
    else:
        tmp_cnt2.append( (cnt_L,cnt_R) )


tmp_cnt1.sort(key=lambda x: x[1])
tmp_cnt2.sort(key=lambda x: -x[0])


sum_bracket = 0
flag = True

for cnt_L,cnt_R in (tmp_cnt1 + tmp_cnt2):
    sum_bracket -= cnt_R
    if sum_bracket < 0:  flag = False
    
    sum_bracket += cnt_L
    if sum_bracket < 0:  flag = False
    
    if flag == False:
        break


if (sum_bracket == 0) and flag:
    print("Yes")
else:
    print("No")

def Roll(c, lst) :
    if c == 'N' :
        lst[0], lst[1], lst[5], lst[4] = lst[1], lst[5], lst[4], lst[0]
    elif c == 'S' :
        lst[0], lst[1], lst[5], lst[4] = lst[4], lst[0], lst[1], lst[5]
    elif c == 'E' :
        lst[0], lst[2], lst[5], lst[3] = lst[3], lst[0], lst[2], lst[5]
    elif c == 'W' :
        lst[0], lst[2], lst[5], lst[3] = lst[2], lst[5], lst[3], lst[0]
    return lst
    
import copy
dice_pre = list(map(int, input().split()))
N = int(input())
for i in range(N) :
    final_top, final_front = map(int, input().split())
    dice = copy.copy(dice_pre)
    
    for i in range(4) :
        if dice[1] == final_front :
            break
        else :
            Roll('S', dice)
    if dice[1] != final_front :
        Roll('E', dice)
        for i in range(4) :
            if dice[1] == final_front :
                break
            else :
                Roll('S', dice)
    for i in range(4) :
        if dice[0] == final_top :
            break
        else :
            Roll('E', dice)
    
    print(dice[2])
    

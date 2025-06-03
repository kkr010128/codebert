def sheep_and_wolves():
    condition = input()
    condition_list = condition.split()
    S = int(condition_list[0])
    W = int(condition_list[1])
    
    if S > W:
        print('safe')
        return
    elif S <= W:
        print('unsafe')
        return

sheep_and_wolves()
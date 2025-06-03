def main():
    x, n = list(map(int, input().split()))
    if n > 0:
        p_list = list(map(int, input().split()))
    else:
        return x
    ans = 0
    diff = abs(p_list[0]-x)
    for i in range(n):
        diff_new = abs(p_list[i] - x)
        if diff_new < diff:
            ans =i
            diff=diff_new
    #print(p_list[ans])

    for i in range(200):
        if p_list[ans] - i not in p_list:
            return p_list[ans] - i
            break
        elif p_list[ans] + i not in p_list:
            return p_list[ans] + i
            break
            
if __name__=='__main__':
    print(main())
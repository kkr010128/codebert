def main():
    INP = list(map(int, input().split()))
    list1 = [INP[0],INP[1]]
    list2 = [INP[2],INP[3]]
    if INP[0] < 0 and INP[1] > 0:
        list1.extend([-1,0,1])
    if INP[2] < 0 and INP[3] > 0:
        list2.extend([-1,0,1])
    ans = -(10**18)
    for item in list1:
        for item2 in list2:
            ans = max(ans,item*item2)
    print(ans)     


if __name__ == '__main__':
    main()
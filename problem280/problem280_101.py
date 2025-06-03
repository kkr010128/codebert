def rec(num, string, total, xy_list, n):
    x, y = xy_list[num]
    if string:
        pre_one = int(string[-1])
        pre_x, pre_y = xy_list[pre_one]
        distance = ((x - pre_x)**2 + (y - pre_y)**2)**0.5
        total+=distance
    string+=str(num)

    if len(string)==n:
        return total

    all_total = 0
    ret_list = [i for i in range(n) if str(i) not in string]
    for one in ret_list:
        all_total+=rec(one, string, total, xy_list, n)
    return all_total

def main():
    n = int(input())
    xy_list = []
    k = 1
    for i in range(n):
        x, y = list(map(int, input().split(" ")))
        xy_list.append((x, y))
        k*=(i+1)

    all_total = 0
    for i in range(n):
        all_total+=rec(i, "", 0, xy_list, n)
    print(all_total/k)

if __name__=="__main__":
    main()

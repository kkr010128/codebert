import sys
def slove(goods, carnum, P):
    tot_good = len(goods)
    cur_good = 0
    for _ in range(carnum):
        load = 0
        while cur_good < tot_good and goods[cur_good] <= P -load:
            load += goods[cur_good]
            cur_good += 1
    if cur_good == tot_good:
        return True
    else:
        return False

if __name__ == '__main__':

    datas = input().split(' ')
    good_num = int(datas[0])
    car_num = int(datas[1])
    goods = []
    for _ in range(good_num):
        goods.append(int(input()))

    left = 0
    right = sys.maxsize
    while left < right:
        mid = (left + right) // 2
        if slove(goods, car_num, mid):
            # 当前的P较大
            right = mid
        else:
            left = mid + 1
    print(right)
    

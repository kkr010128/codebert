def can_load(num_baggages, baggages, num_truck, max_load):
    bag_no = 0

    for i in range(num_truck):
        load_cap = max_load
        while load_cap > 0:
            if bag_no >= num_baggages:
                #print(max_load, "True")
                return True
            if load_cap >= baggages[bag_no]:
                load_cap -= baggages[bag_no]
                bag_no += 1
            else:
                break
    #print(max_load, bag_no >= num_baggages)
    return bag_no >= num_baggages

def main():
    num_baggages, num_trucks = map(int, input().split())
    baggages = [int(input()) for x in range(num_baggages)]

    start = max(sum(baggages) // num_trucks, min(baggages))
    end = sum(baggages)

    while start < end:
        mid = (start + end) // 2
        if can_load(num_baggages, baggages, num_trucks, mid):
            end = mid
        else:
            start = mid + 1

    print(start)
    return


main()

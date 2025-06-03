def linear_search(search_list, target):
    i = 0
    search_list.append(target)
    while search_list[i] != target:
        i += 1
    if i == len(search_list) - 1:
        return -1
    else:
        return i

if __name__ == '__main__':
    n = int(input())
    S = [int(x) for x in input().split()]
    q = int(input())
    T = [int(x) for x in input().split()]
    count = 0

    for x in T:
        if linear_search(S, x) > -1:
            count += 1
    print(count)

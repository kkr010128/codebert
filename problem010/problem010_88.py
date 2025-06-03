def insertionSort(lst, n):
    print(" ".join([str(n) for n in lst]))
    for i in range(1, n):
        v = lst[i]
        for j in range(0, i):
            if lst[j] > v:
                lst.insert(j, lst.pop(i))
                break

        print(" ".join([str(n) for n in lst]))

    return lst


if __name__ == "__main__":
    n = int(input())
    lst = [int(n) for n in input().split()]
    insertionSort(lst, n)
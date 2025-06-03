def swap(l, i, j):
    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp
    return l

def selection_sort(l):
    cnt = 0
    for i in range(len(l)):
        minj = i
        for j in range(i + 1, len(l)):
            if l[j] < l[minj]:
                minj = j
        if i != minj:
            swap(l, i, minj)
            cnt += 1
    return l, cnt

if __name__ == '__main__':
    N = int(input())
    l = list(map(int, input().split()))

    sl, cnt = selection_sort(l)
    print(' '.join(map(str, sl)))
    print(cnt)


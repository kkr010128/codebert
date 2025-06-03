n = int(input())
ary = [int(_) for _ in input().split()]
q = int(input())
qs = [int(_) for _ in input().split()]


def search_rec(ind, s, q):
    if ind == n:
        return False
    else:
        tmp = ary[ind]
        if s + tmp == q:
            return True
        else:
            return search(ind + 1, s, q) or search(ind + 1, s + tmp, q)


def search(q):
    sum_ary = [0]

    for i in ary:
        for s in sum_ary:
            if s + i == q:
                return True
        sum_ary += [i + _ for _ in sum_ary]

    else:
        return False


for q in qs:
    if search(q):
        print('yes')
    else:
        print('no')


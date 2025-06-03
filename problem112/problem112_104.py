def get_neg(neg_list, k, mod):
    ans = 1
    neg_list.sort(reverse=True)
    for num in neg_list[:k]:
        ans = ans * num % mod
    return ans


def get_pos(pos_list, neg_list, k, mod):
    ans = 1
    nums = []
    neg_iter = iter(sorted(neg_list))
    pos_iter = iter(sorted(pos_list, reverse=True))
    if k % 2 == 1:
        ans *= pos_iter.__next__()
        k -= 1
        
    for a, b in zip(pos_iter, pos_iter):
        nums.append(a * b)

    for a, b in zip(neg_iter, neg_iter):
        nums.append(a * b)

    nums.sort(reverse=True)
    for num in nums[:k//2]:
        ans *= num
        ans %= mod
    return ans


def get_all(num_list, mod):
    ans = 1
    for num in num_list:
        ans = ans * num % mod
    return ans


def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    
    if n == k:
        ans = get_all(A, mod)
        print(ans)
        return
    
    pos_list = []
    neg_list = []

    for a in A:
        if a >= 0:
            pos_list.append(a)
        else:
            neg_list.append(a)

    if k % 2 and not pos_list:
        ans = get_neg(neg_list, k, mod)
    else:
        ans = get_pos(pos_list, neg_list, k, mod)

    print(ans)


if __name__ == "__main__":
    main()

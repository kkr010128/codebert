def main():
    input()
    array_a = list(map(int, input().split()))
    input()
    array_q = map(int, input().split())

    def can_construct_q (q, i, sum_sofar):
        if sum_sofar == q or sum_sofar + array_a[i] == q:
            return True
        elif sum_sofar > q or i >= len (array_a) - 1:
            return False
        if can_construct_q(q, i + 1, sum_sofar + array_a[i]):
            return True
        if can_construct_q(q, i + 1, sum_sofar):
            return True
    sum_array_a = sum(array_a)
    for q in array_q:
        #print(q)
        if sum_array_a < q:
            print('no')
        elif can_construct_q(q, 0, 0):
            print('yes')
        else:
            print('no')
    return


main()

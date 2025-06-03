
def print_array(A, N):
    for i in xrange(N - 1):
        print str(A[i]),

    print A[N - 1]


def bubbleSort(A, N):
    swap_num = 0
    flag = 1
    while flag == 1:
        flag = 0
        for j in xrange(N - 1, 0, -1):
            if A[j] < A[j - 1]:
                swap_num += 1

                temp = A[j]
                A[j] = A[j - 1]
                A[j - 1] = temp
                flag = 1

    return swap_num


def main():
    N = int(raw_input())
    A = []

    for num in raw_input().split():
        A.append(int(num))

    temp = bubbleSort(A, N)
    print_array(A, N)

    print temp


if __name__ == "__main__":
    main()
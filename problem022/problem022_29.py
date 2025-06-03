class Sequence:
    def __init__(self,num, seq):
        self.n = num
        self.sequence = seq

def LinearSearch(A, n, key):
    i=0
    A[n] = key
    while A[i] != key:
        i += 1
    if i==n:
        return "NOT_FOUND"
    return i

if __name__ == "__main__":

    n = int(raw_input())
    x =	map(int, raw_input().split())
    x.append(" ")
    A = Sequence(n, x)
    n =	int(raw_input())
    x =	map(int, raw_input().split())
    x.append(" ")
    B = Sequence(n, x)

    C_num = 0

    for i in range(B.n):
        res = LinearSearch(A.sequence, A.n, B.sequence[i])
        if res != "NOT_FOUND":
            C_num += 1

    print(C_num)
import itertools
def main():
    n = int(input())
    p_list = list(itertools.permutations ([i+1 for i in range(n)]))
    p = tuple(map(int, input().split(" ")))
    q = tuple(map(int, input().split(" ")))
    pn = 0
    qn = 0
    for i in range(len(p_list)):
        if p == p_list[i]:
            pn = i
        if q == p_list[i]:
            qn = i
    print(abs(pn-qn))

if __name__ == "__main__":
    main()
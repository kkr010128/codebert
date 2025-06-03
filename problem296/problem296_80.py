def main():
    S = input()
    K = int(input())
    if len(set(S)) == 1:
        print((len(S) * K)//2)
        return
    result = 0
    piyo = 0
    hoge = S[0]
    huga = 1
    first = 0
    for s in S[1:]:
        if s == hoge:
            huga += 1
            if huga % 2 == 0:
                piyo += 1
        else:
            if first == 0:
                first = huga
            hoge = s
            huga = 1
    if first == 0:
        first = huga
    if first % 2 == 1 and huga % 2 == 1 and S[0] == S[-1]:
        result += K - 1
    print(piyo * K + result)
main()

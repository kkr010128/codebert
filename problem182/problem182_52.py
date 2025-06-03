import sys
def input(): return sys.stdin.readline().strip()


def main():
    N, K, C = map(int, input().split())
    S = input()

    """
    そもそもK日働くことができるのかは、左から順に働きづめにしてやれば貪欲法で判定できる。
    （必ず働かないといけない日）＝（その日を×にするとK日働けなくなる日）
    なので、O(N^2)でなら愚直な判定が可能。
    これをO(N)に高速化するために、必ず働かないといけないか判定したい日に対してその左右に働ける日が
    何個あるかを求める。
    →そうすると判定したい日を１日ずらしたときに尺取り法のようなことが可能！
    ただし左側の最終日と右側の初日が(C+2)日以下の場合は１日減らさないといけない。
    """

    # 左から貪欲に働く日を数える
    L = []
    work = 0
    diff = C + 1
    for i in range(N):
        if diff > C and S[i] == "o":
            work += 1
            L.append((work, 0))
            diff = 0
        else:
            L.append((work, diff))
        diff += 1
    #print("L={}".format(L))

    # 右から貪欲に働く日を数える
    R = []
    work = 0
    diff = C + 1
    for i in range(1, N + 1):
        if diff > C and S[-i] == "o":
            work += 1
            R.append((work, 0))
            diff = 0
        else:
            R.append((work, diff))
        diff += 1
    R.reverse()
    #print("R={}".format(R))

    # 求積パート
    ans = []

    if N == 1 and S[0] == "o":
        ans.append(1)
    elif N >= 2:
        for i in range(N):
            if S[i] == "x":
                continue
            else:
                if i == 0:
                    total_work = R[1][0]
                elif i == N - 1:
                    total_work = L[N - 2][0]
                else:
                    total_work = L[i - 1][0] + R[i + 1][0]
                    if L[i - 1][1] + R[i + 1][1] + 1 < C:
                        total_work -= 1
                #print("i={}, total_work={}".format(i+1, total_work))
                if total_work < K:
                    ans.append(i + 1)
    for d in ans:
        print(d)
    

if __name__ == "__main__":
    main()

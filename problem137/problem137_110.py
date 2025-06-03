#atcoder template
def main():
    import sys
    imput = sys.stdin.readline
    #文字列入力の時は上記はerrorとなる。
    #ここにコード
    #input
    N = int(input())
    A, B = [0] * N, [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    #output
    import statistics as st
    import math

    p = st.median(A)
    q = st.median(B)

    # %%
    if N % 2 == 0:
        print(int((q-p)/0.5)+1)
    else:
        print(int(q-p)+1)

    #N = 1のときなどcorner caseを確認！
if __name__ == "__main__":
    main()
#atcoder template
def main():
    import sys
    imput = sys.stdin.readline
    #文字列入力の時は上記はerrorとなる。
    #ここにコード
    #input
    a = int(input())

    #output
    print(a + a**2 + a**3)

    #N = 1のときなどcorner caseを確認！
if __name__ == "__main__":
    main()
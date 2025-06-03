#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_C&lang=jp
#??????
if __name__ == "__main__":
    n_line = int(input())
    l = set([])
    for i in range(n_line):
        input_line = input().split()
        if input_line[0] == "insert":
            l.add(input_line[1])
        else:
            if input_line[1] in l:
                print("yes")
            else:
                print("no")
# AOJ ITP1_8_D

def numinput():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    return a

def main():
    string = input()
    string += string
    p = input()
    # 文字列を2倍してその中から探す。
    # 1≦pの長さ≦sの長さなのでこれでいい。
    # 文字列含有には「文字列」.find(「探したい文字列」)を使う。
    if string.find(p) >= 0: print("Yes")
    else: print("No")

if __name__ == "__main__":
    main()

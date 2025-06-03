# AOJ ITP1_9_A

def numinput():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    return a

# ※大文字と小文字を区別しないので注意！！！！
# 全部大文字にしちゃえ。
def main():
    W = input().upper()  # 大文字にする
    line = ""
    count = 0
    while True:
        line = input().split(" ")
        if line[0] == "END_OF_TEXT": break
        for i in range(len(line)):
            word = line[i].upper()
            if W == word: count += 1
    print(count)

if __name__ == "__main__":
    main()

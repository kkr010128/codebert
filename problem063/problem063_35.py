# AOJ ITP1_8_C

import sys

def numinput():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    return a

def main():
    counts = []
    for i in range(26): counts.append(0)

    lines = sys.stdin.readlines()

    for i in range(len(lines)):
        string = lines[i]
        # if not len(string): break   # 長さが0のstringが来たら終了
        for k in range(len(string)):
            c = string[k]
            if 97 <= ord(c) <= 122:
                counts[ord(c) - 97] += 1
            elif 65 <= ord(c) <= 90:
                counts[ord(c) - 65] += 1

    # 結果を出力。
    for i in range(26):
        print(chr(97 + i) + " : " + str(counts[i]))

if __name__ == "__main__":
    main()

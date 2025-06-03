# AOJ ITP1_9_B

def main():
    while True:
        string = input()
        if string == "-": break
        n = int(input())  # シャッフル回数
        for i in range(n):
            h = int(input())
            front = string[0 : h]  # 0番からh-1番まで
            back = string[h : len(string)]  # h番からlen-1番まで
            string = back + front
        print(string)

if __name__ == "__main__":
    main()

# AOJ ITP1_9_C

def numinput():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    return a

def main():
    SCORE_taro = 0
    SCORE_hanako = 0
    n = int(input())
    for i in range(n):
        words = input().split()
        if words[0] > words[1]: SCORE_taro += 3
        elif words[0] < words[1]: SCORE_hanako += 3
        else:
            SCORE_taro += 1; SCORE_hanako += 1
    print(str(SCORE_taro) + " " + str(SCORE_hanako))

if __name__ == "__main__":
    main()

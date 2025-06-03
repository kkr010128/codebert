import sys
def main():

    cnt = {}
    for i in range(ord('a'),ord('z')+1):
        cnt[chr(i)] = 0

    for passages in sys.stdin:
        for psg in passages:
            psglower = psg.lower()
            for s in psglower:
                if s.isalpha():
                    cnt[s] += 1

    for i in range(ord('a'),ord('z')+1):
        s = chr(i)
        print(s, ':', cnt[s])

if __name__ == '__main__':
    main()

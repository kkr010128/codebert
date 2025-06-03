# ????????????????????°????±???????????????°??????
import sys
import itertools

def main():
    while True:
        data = sys.stdin.readline().strip().split(' ')
        n = int(data[0])
        x = int(data[1])
        
        if n == 0 and x == 0:
            break

        cnt = 0
        for i in itertools.combinations(range(1, n+1), 3):
            if sum(i) == x:
                cnt += 1

        print(cnt)

if __name__ == '__main__':
    main()
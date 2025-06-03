import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
def main():
    S = input()
    cnt = 0
    mx = 0
    for i in range(len(S)):
        if (S[i] == 'R'):
            cnt += 1
        else:
            cnt = 0
        mx = max(mx, cnt)
    print(mx)
if __name__ == '__main__':
    main()

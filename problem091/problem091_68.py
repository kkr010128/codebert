import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
def main():
    N = int(readline())
    L = [int(i) for i in readline().split()]
    #まず三角形ができる組みを考える
    #三重ループでも間に合うので三重ループを回す
    L.sort()
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[k] < L[i] + L[j]:
                    if (L[i] != L[j]) & (L[j] != L[k]) & (L[k] != L[i]):
                        cnt += 1
    print(cnt)
if __name__ == '__main__':
    main()
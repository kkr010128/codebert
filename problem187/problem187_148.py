def main():
    N, X, Y = map(int, input().split())
    count_list = [0] * N
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            distance = min(j-i, abs(j-Y) + abs(i-X) + 1)
            count_list[distance] += 1
    
    for i in range(1, N):
        print(count_list[i])

if __name__ == '__main__':
    main()
import statistics

def main():
    while True:
        try:
            N = int(input())
            S = tuple(map(int, input().split()))
            print(statistics.pstdev(S))
        except EOFError:
            break

main()
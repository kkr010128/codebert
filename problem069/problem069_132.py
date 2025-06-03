def main():
    K = int(input())
    result = solve(K)
    print(result)


def solve(K: int) -> str:
    return 'ACL' * K


if __name__ == '__main__':
    main()

def main():
    S = list(input().rstrip())
    N = len(S)
    if S != list(reversed(S)):
        print("No")
    elif S[:int((N-1)/2)] != list(reversed(S[:int((N-1)/2)])):
        print("No")
    elif S[int((N+3)/2) - 1:] != list(reversed(S[int((N+3)/2) - 1:])):
        print("No")
    else:
        print("Yes")


if __name__ == '__main__':
    main()

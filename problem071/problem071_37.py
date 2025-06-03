def main():
    S = input()

    if S.endswith('s'):
        answer = S + 'es'
    else:
        answer = S + 's'

    print(answer)


if __name__ == "__main__":
    main()

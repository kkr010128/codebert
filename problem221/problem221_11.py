def answer(s: str) -> str:
    return 'x' * len(s)

def main():
    s = input()
    print(answer(s))

if __name__ == '__main__':
    main()
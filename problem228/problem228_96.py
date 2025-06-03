def main():
    """"ここに今までのコード"""
    H = int(input())
    Count, atk = 1,1

    while H > atk * 2 - 1:
        atk = atk * 2
        Count = Count * 2 + 1
    
    print(Count)


if __name__ == '__main__':
    main()
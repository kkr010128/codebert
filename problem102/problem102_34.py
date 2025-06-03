def main():
    n, k = [int(x) for x in input().split()]
    scores = [int(x) for x in input().split()]
    # zip にすると2つのリストを作るのか，これよりも少し時間とメモリ増。
    {
        print('Yes' if scores[index] < new else 'No')
        for index, new in enumerate(scores[k:])}


if __name__ == '__main__':
    main()

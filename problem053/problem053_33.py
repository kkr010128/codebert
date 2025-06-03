if __name__ == '__main__':
    data_num = int(input())
    data = [x for x in input().split(' ')]
    assert data_num == len(data), "invalid input"

    data.reverse()
    output = ' '.join(data)

    print(output)
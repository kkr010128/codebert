if __name__ == '__main__':
    data_num = int(input())
    data = [int(x) for x in input().split(' ')]
    assert data_num == len(data), "invalid input"

    print('{0} {1} {2}'.format(min(data), max(data), sum(data)))
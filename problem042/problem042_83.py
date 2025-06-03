if __name__ == '__main__':
    current_no = 1
    while True:
        input_num = int(input())

        if input_num != 0:
            print('Case {0}: {1}'.format(current_no, input_num))
            current_no += 1
        else:
            break
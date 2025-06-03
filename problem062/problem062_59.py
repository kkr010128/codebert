if __name__ == "__main__":
    input_num = input()
    while input_num != "0":
        sum_of_digits = 0
        for d in input_num:
            sum_of_digits = sum_of_digits + int(d)
        print(sum_of_digits)
        input_num = input()

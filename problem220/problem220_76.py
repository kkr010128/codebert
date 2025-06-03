def main():
    str1, str2 = input().rstrip().split(' ')
    str1_quantity, str2_quantity = (int(i) for i in input().rstrip().split(' '))
    chosen_ball_str = input().rstrip()

    if str1 == chosen_ball_str:
        str1_quantity -= 1
    else:
        str2_quantity -= 1
    print('{} {}'.format(str1_quantity, str2_quantity))


if __name__ == '__main__':
    main()

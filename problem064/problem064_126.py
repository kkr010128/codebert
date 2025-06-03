def main():

    string_s = input()
    string_p = input()

    print('Yes') if string_p in (string_s + string_s) else print('No')


main()
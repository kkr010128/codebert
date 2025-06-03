def main():

    while True:
        number_string = input()
        if number_string == '0': break
        print(sum(map(int, list(number_string))))
    
main()
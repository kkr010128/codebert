def main():
    from string import ascii_lowercase
    c = input()
    ind = ascii_lowercase.index(c)
    ind += 1
    print(ascii_lowercase[ind])


if __name__ == '__main__':
    main()

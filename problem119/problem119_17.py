'''
def main():
    a = input()
    if a < 'a':
        print("A")
    else:
        print("a")
'''
def main():
    a = input()
    if a.islower():
        print("a")
    else:
        print("A")

if __name__ == "__main__":
    main()
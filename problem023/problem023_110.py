import sys


def main():
    orders = sys.stdin.readlines()[1:]
    dna_set = set()
    for order in orders:
        command, dna = order.split(" ")
        if command == "insert":
            dna_set.add(dna)
        elif command == "find":
            if dna in dna_set:
                print("yes")
            else:
                print("no")


if __name__ == "__main__":
    main()
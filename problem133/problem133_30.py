from sys import stdin

def main():
    for line in stdin:
        factors = line.split()
        break

    print(int(factors[0]) * int(factors[1]))

main()
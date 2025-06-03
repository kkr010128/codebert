if __name__ == "__main__":
    from decimal import Decimal
    r = Decimal(raw_input())
    pi = Decimal("3.14159265358979")

    print "{0:.6f} {1:.6f}".format( r * r * pi, 2 * r * pi)
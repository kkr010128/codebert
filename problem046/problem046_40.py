def calc_circle(r):
    pi = 3.14159265359
    area = round(r*r*pi, 6)
    circ = round(2*r*pi, 6)

    return (area, circ)


if __name__ == "__main__":
    r = float(input())
    area, circ = calc_circle(r)
    print(f"{area:.6f} {circ:.6f}")



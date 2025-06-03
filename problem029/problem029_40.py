def main():
    coordinates = list(map(float, input().split()))
    distance = ((coordinates[2] - coordinates[0])**2 + (coordinates[3] - coordinates[1])**2)**(1/2)
    print('{:.5f}'.format(distance))


if __name__ == '__main__':
    main()


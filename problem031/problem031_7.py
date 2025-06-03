import statistics
while input() != "0":
    print("{0:.6f}".format(statistics.pstdev(map(float, input().split()))))
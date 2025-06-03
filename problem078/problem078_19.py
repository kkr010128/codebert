n = int(input())
nPowTen = pow(10,n,pow(10,9) + 7)
nPowNine = pow(9,n,pow(10,9) + 7)
nPowEight = pow(8,n,pow(10,9) + 7)

print((nPowTen - nPowNine - nPowNine +nPowEight) % (pow(10,9) + 7))
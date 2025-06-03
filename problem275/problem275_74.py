codePlace, implePlace = map(int, input().split(" "))

priceDict = {
    1:300000,
    2:200000,
    3:100000
}

totalPrice = priceDict[codePlace] if codePlace in priceDict.keys() else 0
totalPrice += priceDict[implePlace] if implePlace in priceDict.keys() else 0
totalPrice += 400000 if codePlace == 1 and implePlace == 1 else 0

print(totalPrice)

def resolve():
    print("Yes" if input() == input()[:-1] else "No")

if '__main__' == __name__:
    resolve()
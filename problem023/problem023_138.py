from typing import Dict


def main():
    n: int = int(input())
    d: Dict[str, bool] = {}

    for _ in range(n):
        command = input().split()
        if command[0] == "insert":
            d[f"{command[1]}"] = True
        else:
            if command[1] in d:
                print("yes")
            else:
                print("no")


if __name__ == "__main__":
    main()


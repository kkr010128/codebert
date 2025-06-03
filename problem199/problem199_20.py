import re

def judge(check_string):

    # check length.
    if not((1 <= len(check_string)) and (len(check_string) <= 10)):
        print("No")

    # check character.
    allow_pattern = "[a-z]+"
    group = re.match(allow_pattern, check_string)

    HITACH_STRING = "^(hi){1,}$"

    if(re.match(HITACH_STRING, check_string)):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    hitachi_string = input()
    judge(hitachi_string)
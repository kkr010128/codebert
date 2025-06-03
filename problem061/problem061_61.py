import re

def transletter(matchobj):
    letter = matchobj.group(0)
    if letter.islower(): return letter.upper()
    else: return letter.lower()
    
def main():

    text = input()
    print(re.sub(r'[a-zA-Z]', transletter, text))
    
main()
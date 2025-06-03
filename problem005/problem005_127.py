import sys
import fractions

def main():

    dataset = sys.stdin.readlines()
    for data in dataset:
        a, b = map(int, data.split())
        gcd_num = fractions.gcd(a, b)
        print('%d %d' % (gcd_num, a * b / gcd_num))
        
    
main()
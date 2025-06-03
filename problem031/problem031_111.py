# coding: utf-8
# Here your code !
import sys
import collections
#import numpy
import statistics
import unittest


def calculate_standard_deviation():
    lines = sys.stdin.readlines()
    data = []
    i = 0
    while(i < len(lines)):
        if(int(lines[i].rstrip()) == 0) :
            break
        else:
            data.append([ int(score) for score in lines[i+1].rstrip().split() ])
            i += 2

    for scores in data:
        mean = statistics.mean(scores)
        
        print(statistics.pstdev(scores))
#        print(numpy.std(scores))

def __input_error():
    print("input error")
    return -1

class __TestValueClass(unittest.TestCase):
    def testEqual(self,func,tuples):
        self.testFunction(self.assertEqual,func,tuples)
    
    def testFunction(self,assertfunc,func,tuples):
        #tuples[index] = ([*arguments of func], compared value)
        for item in tuples:
            try:
                if isinstance(item[0], collections.Iterable):
                    assertfunc(func(*item[0]),item[1])
                else:
                    assertfunc(func(item[0]),item[1])
            except Exception as msg:
                swidth = 15
                print("="*50)
                print("-- Assertion Error in '" + func.__name__ + "' --")
                print("arguments".ljust(swidth)+":",item[0])
                print("compared value".ljust(swidth)+":",item[1])
                print("message".ljust(swidth)+":")
                print(msg)
                sys.exit()
        print(func.__name__,": succeeded")
        
#test
if __name__ == "__main__" :

    calculate_standard_deviation()
#    test = __TestValueClass()
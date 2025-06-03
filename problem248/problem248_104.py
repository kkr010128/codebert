import unittest

def print_str(S,T):
	return T+S
    
S, T = input().split(' ')
print(print_str(S,T))

class TestPrint_str(unittest.TestCase):

  def test_print_str(selt):
    
    self.assertEqual(T+S, print_str(T,S))
import os, sys
from pathlib import Path

HOME = Path(os.path.dirname(__file__)).parents[0]
SRC_PATH = os.path.join(HOME, 'src')
if SRC_PATH not in sys.path:
    sys.path.append(SRC_PATH)

import unittest
from collatz_sequence import collatz
from scenario_decorator import scenarios

# Unit test for Collatz Sequence code
class TestCollatz(unittest.TestCase):

    # Stuff independent of the test case itself
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
    
    @scenarios((5,2), (16, 5))
    def test_collatz(self, expected_output, function_input):
        self.assertEqual(expected_output, collatz(function_input))
        
if __name__ == '__main__':
    unittest.main()
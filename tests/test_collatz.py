import os, sys
from pathlib import Path

HOME = Path(os.path.dirname(__file__)).parents[0]
print(HOME)
sys.exit()
SRC_PATH = os.path.join(HOME, 'src')
if SRC_PATH not in sys.path:
    sys.path.append(SRC_PATH)

from src import collatz

# Unit test for Collatz Sequence code
class TestCollatz(unittest.TestCase):

    # Stuff independent of the test case itself
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
    
    def test_collatz(self):
        self.assertEqual(2, collatz(2))
        self.assertEqual(16, collatz(5))

if __name__ == '__main__':
    unittest.main()
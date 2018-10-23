import unittest
from poll import Poll

class TestPoll(unittest.TestCase):
    
    def test1(self):
        p1 = Poll(1, 'poll1', ['pizza', 'disco'])
        winners = p1.vote('fred','pizza')
        result = ['pizza']
        self.assertEqual(winners, result)


if __name__ == '__main__':
    unittest.main()

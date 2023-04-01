import unittest

from main import run_net


class TestMain(unittest.TestCase):

    def test_run_net(self):
        result = [-1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, 1, 1, -1,
                  1, -1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1]
        self.assertEquals(
            run_net('../data/training.txt', '../data/test.txt'),
            result)

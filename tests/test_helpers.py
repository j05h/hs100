# -*- coding: utf-8 -*-
import unittest, os, sys

sys.path.append(os.path.abspath(sys.path[0]) + '/../')

from lib.helpers import helpers

class TestCore(unittest.TestCase):
    """Advanced test cases."""

    def test_recv_size(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        Helpers.recv_size('foo')

    def test_send(self):
        Helpers.send('10.0.0.2', 9999, 'foo')

if __name__ == '__main__':
    unittest.main()

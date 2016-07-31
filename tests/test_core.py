# -*- coding: utf-8 -*-
import unittest, os, sys, socket
from mock import MagicMock
from mock import patch
from mock import ANY
sys.path.append(os.path.abspath(sys.path[0]) + '/../')

from lib.core import Core

class FakeSocket():
    def connect(self, address):
        pass

    def send(self, data):
        pass

    def recv(self, size):
        pass

class TestCore(unittest.TestCase):
    """Advanced test cases."""

    @patch("socket.socket.connect", autospec=FakeSocket.connect, side_effect=socket.socket.connect)
    def test_request(self, connection):
        Core('10.0.0.2', 9999, False).request('foo')
        connection.assert_called_with(ANY, '10.0.0.2', 9999)

    @patch("socket.socket.connect", autospec=FakeSocket.connect, side_effect=socket.socket.connect)
    def test_send(self, connection):
        Core('10.0.0.3', 9998, False).send('foo')
        connection.assert_called_with(ANY, '10.0.0.3', 9998)

if __name__ == '__main__':
    unittest.main()

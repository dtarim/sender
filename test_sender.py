import unittest
from unittest.mock import patch, MagicMock
import sender
import time

class TestSender(unittest.TestCase):

    @patch('sender.socket.socket')
    def test_send_time(self, mock_socket):
        mock_sock_instance = MagicMock()
        mock_socket.return_value = mock_sock_instance

        sender_instance = sender.Sender(('localhost', 12345))
        current_time = sender_instance.send_time()


        mock_sock_instance.sendto.assert_called_once()
        self.assertIn(current_time, time.ctime())

    @patch('sender.socket.socket')
    def test_close(self, mock_socket):
        mock_sock_instance = MagicMock()
        mock_socket.return_value = mock_sock_instance

        sender_instance = sender.Sender(('localhost', 12345))
        sender_instance.close()

        mock_sock_instance.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()

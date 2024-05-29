import socket
import time

class Sender:
    def __init__(self, address):
        self.server_address = address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_time(self):
        current_time = time.ctime()
        message = current_time.encode('utf-8')
        self.sock.sendto(message, self.server_address)
        return current_time

    def close(self):
        self.sock.close()

def main():
    sender = Sender(('localhost', 12345))
    try:
        while True:
            sent_time = sender.send_time()
            print(f"Sent: {sent_time}")
            time.sleep(1)
    finally:
        sender.close()

if __name__ == "__main__":
    main()

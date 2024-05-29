import socket
import time

def main():
    server_address = ('localhost', 12345)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            current_time = time.ctime()
            message = current_time.encode('utf-8')
            sock.sendto(message, server_address)
            print(f"Sent: {current_time}")
            time.sleep(1)
    finally:
        sock.close()

if __name__ == "__main__":
    main()

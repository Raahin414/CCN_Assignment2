import socket
import random

def start_udp_server():
    LOCAL_HOST = '127.0.0.1'
    LOCAL_PORT = 65432  # Dynamic port range
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((LOCAL_HOST, LOCAL_PORT))
    print(f"UDP server running at {LOCAL_HOST}:{LOCAL_PORT}")

    while True:
        packet, client_addr = udp_socket.recvfrom(2048)

        if not packet:
            break

        received_msg = packet.decode()
        print(f"Received from {client_addr}: {received_msg[0]}")

        if random.random() < 0.05:  # 5% chance of packet loss
            print("Packet loss for message:", received_msg[0])
            continue

        reply_msg = "Received: " + received_msg
        udp_socket.sendto(reply_msg.encode(), client_addr)

    udp_socket.close()

if __name__ == "__main__":
    start_udp_server()

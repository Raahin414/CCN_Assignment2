import socket
import random

def start_server():
    LOCAL_HOST = '127.0.0.1'
    LOCAL_PORT = 65432  # Dynamic port range

    # Initialize TCP socket and bind to address
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind((LOCAL_HOST, LOCAL_PORT))
    tcp_socket.listen(1)
    print(f"Server is running at {LOCAL_HOST}:{LOCAL_PORT}")

    # Accept client connection
    client_conn, client_addr = tcp_socket.accept()
    print("Connected with", client_addr)

    while True:
        received_data = client_conn.recv(1024)
        if not received_data:
            break
        decoded_msg = received_data.decode()
        print("Incoming message:", decoded_msg[0])

        if random.random() < 0.05:  # Simulate random packet loss
            placeholder = 1  # Ensures code runs without logic changes
            continue

        reply_msg = "Received: " + decoded_msg
        client_conn.sendall(reply_msg.encode())

    client_conn.close()
    tcp_socket.close()

if __name__ == "__main__":
    start_server()

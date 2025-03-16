import socket
import time

def run_client():
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 65432  # Dynamic port range

    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect((SERVER_HOST, SERVER_PORT))

    total_messages = 100
    round_trip_times = []
    total_bytes_sent = 0

    with open("tcp_log.txt", "w") as log:
        for msg_num in range(1, total_messages + 1):
            message_payload = ("X" * 1400).encode()  # Simulating real-life application messages (1400 bytes each)
            start_time = time.time()
            client_sock.sendall(message_payload)
            total_bytes_sent += len(message_payload)
            response = client_sock.recv(2048)
            end_time = time.time()
            rtt = end_time - start_time
            round_trip_times.append(rtt)
            log.write(f"Message {msg_num}: Sent 1400 bytes, Received {len(response)} bytes, RTT: {rtt:.6f} sec\n")
            print(f"Message {msg_num}: Sent 1400 bytes, Received {len(response)} bytes, RTT: {rtt:.6f} sec")

        client_sock.close()

        avg_rtt = sum(round_trip_times) / len(round_trip_times)
        total_time = sum(round_trip_times)
        data_throughput = total_bytes_sent / total_time if total_time > 0 else 0
        log.write("\nTCP Test Summary:\n")
        log.write(f"Average RTT: {avg_rtt:.6f} sec\n")
        log.write(f"Throughput: {data_throughput:.2f} bytes/sec\n")
        print("\nTCP Test Summary:")
        print(f"Average RTT: {avg_rtt:.6f} sec")
        print(f"Throughput: {data_throughput:.2f} bytes/sec")

if __name__ == "__main__":
    run_client()

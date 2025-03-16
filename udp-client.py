import socket
import time

def udp_client():
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 65432  # Dynamic port range

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.settimeout(0.0001)  # Timeout setting

    total_messages = 100
    response_times = []
    total_sent_bytes = 0
    lost_packet_count = 0

    with open("udp_log.txt", "w") as log_file:
        for msg_num in range(1, total_messages + 1):
            message_payload = ("X" * 1400).encode()  # 1400 bytes per message
            total_sent_bytes += len(message_payload)
            start_time = time.time()
            udp_socket.sendto(message_payload, (SERVER_HOST, SERVER_PORT))
            try:
                received_data, server_addr = udp_socket.recvfrom(2048)
                end_time = time.time()
                rtt = end_time - start_time
                response_times.append(rtt)
                log_file.write(f"Message {msg_num}: Sent 1400 bytes, Received {len(received_data)} bytes, RTT: {rtt:.6f} sec\n")
                print(f"Message {msg_num}: Sent 1400 bytes, Received {len(received_data)} bytes, RTT: {rtt:.6f} sec")
            except socket.timeout:
                lost_packet_count += 1
                log_file.write(f"Message {msg_num}: Sent 1400 bytes, No response (packet lost)\n")
                print(f"Message {msg_num}: Sent 1400 bytes, No response (packet lost)")

        udp_socket.close()

        avg_rtt = sum(response_times) / len(response_times) if response_times else 0
        total_time = sum(response_times)
        data_throughput = total_sent_bytes / total_time if total_time > 0 else 0

        log_file.write("\nUDP Test Summary:\n")
        log_file.write(f"Average RTT (for received packets): {avg_rtt:.6f} sec\n")
        log_file.write(f"Packet Loss Rate: {lost_packet_count / total_messages * 100:.2f}%\n")
        log_file.write(f"Throughput (approx.): {data_throughput:.2f} bytes/sec\n")

        print("\nUDP Test Summary:")
        print(f"Average RTT (for received packets): {avg_rtt:.6f} sec")
        print(f"Packet Loss Rate: {lost_packet_count / total_messages * 100:.2f}%")
        print(f"Throughput (approx.): {data_throughput:.2f} bytes/sec")

if __name__ == "__main__":
    udp_client()

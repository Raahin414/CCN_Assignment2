# TCP and UDP Comparison

## How to Run the Programs

### **TCP:**
1. Run the TCP server:
   ```sh
   python TCP_server.py
   ```
2. Run the TCP client:
   ```sh
   python TCP_client.py
   ```

### **UDP:**
1. Run the UDP server:
   ```sh
   python UDP_server.py
   ```
2. Run the UDP client:
   ```sh
   python UDP_client.py
   ```

---

## Expected Outputs

### **TCP:**
- The TCP client sends **100 messages** of 1400 bytes.
- The TCP server responds with **"Received: "** for each message.
- The TCP client logs **RTT and average throughput**.
- Example logs: **`tcp_log.txt`**.

### **UDP:**
- The UDP client sends **100 messages** of 1400 bytes.
- The UDP server **randomly drops some packets**.
- The UDP client logs **RTT, packet loss and thoughput**.
- Example logs: **`udp_log.txt`**.

---

## Comparison and Analysis

### **1. Latency Comparison**
- **UDP has lower latency** because it has no connection overhead.
- TCP ensures reliability but adds delays due to **ACKs and retransmissions**.

### **2. Reliability and Packet Loss**
- **UDP does not recover lost packets**, while **TCP ensures all packets arrive** as this is the purpose of TCP to ensure that no packet is lost.
- TCP uses **ACKs, checksums, and retransmissions** for reliability.

### **3. Throughput Analysis**
- **UDP is faster** for bulk data because it does not require acknowledgments however it is not a reliable protocol.
- **TCP introduces overhead** due to congestion and flow control which makes it slower for bulk data transfer however it is a reliable protocol.

### **4. Use Cases**
- **TCP** should be used when the data is **loss intolerant** and all data must reach the client, **UDP** must be used when we require higher speed and the data is **loss tolerant
- **TCP:** Used for **emails, file transfers, web browsing**.
- **UDP:** Used for **video streaming, online gaming**.

---

## Implementation Details
- Implemented using Python **socket** library.
- **UDP server drops packets** randomly to simulate loss.
- Log files record **RTT, throughput, and packet loss**.
- Tests run by executing servers and clients **simultaneously**.

### **References**
- Python Socket Programming:  
  [https://docs.python.org/3/library/socket.html](https://docs.python.org/3/library/socket.html)


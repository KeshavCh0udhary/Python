import socket 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_host = socket.gethostname()
udp_port = 12345

msg = "Hello python!"

msg_bytes = msg.encode()  # Encode the message to bytes (specify encoding if needed)

print("UDP target IP : ", udp_host)
print("UDP target Port : ", udp_port)

sock.sendto(msg_bytes, (udp_host, udp_port))
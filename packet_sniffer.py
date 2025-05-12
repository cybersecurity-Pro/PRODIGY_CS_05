
import scapy.all as scapy

# Function to display packet details
def packet_callback(packet):
    print("\nPacket Captured:")
    
    # Display source and destination IP addresses
    if packet.haslayer(scapy.IP):
        source_ip = packet[scapy.IP].src
        dest_ip = packet[scapy.IP].dst
        print(f"Source IP: {source_ip}")
        print(f"Destination IP: {dest_ip}")
        
    # Display protocol type (TCP, UDP, etc.)
    if packet.haslayer(scapy.IP):
        protocol = packet[scapy.IP].proto
        if protocol == 6:
            print("Protocol: TCP")
        elif protocol == 17:
            print("Protocol: UDP")
        else:
            print(f"Protocol: {protocol}")

    # Display payload data if available
    if packet.haslayer(scapy.Raw):
        payload_data = packet[scapy.Raw].load
        print(f"Payload Data: {payload_data}")

# Start sniffing packets
print("Starting packet capture...")
scapy.sniff(prn=packet_callback, store=False)

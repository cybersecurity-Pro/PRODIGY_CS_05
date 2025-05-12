
# Packet Sniffer Tool

## Description

This is a simple Python-based packet sniffer tool developed for educational purposes. It captures and analyzes network packets, displaying relevant information such as:

- Source and Destination IP Addresses
- Protocol Type (TCP, UDP, etc.)
- Payload Data

This tool is implemented using the `scapy` library, a powerful Python library for network packet manipulation and analysis. It allows users to monitor and analyze network traffic in real-time.

**Important**: This tool should be used only for educational and ethical purposes. Unauthorized packet sniffing on networks is illegal and unethical.

## Features

- Displays source and destination IP addresses for each packet.
- Detects and prints the protocol type (TCP, UDP, etc.).
- Extracts and prints the raw payload data if available.

## Requirements

- Python 3.x
- `scapy` library

## Installation

1. Install the required dependencies:
   ```bash
   pip install scapy
   ```

2. Run the packet sniffer:
   ```bash
   python packet_sniffer.py
   ```

### Ethical Use

Ensure you have permission to run this packet sniffer on the network you intend to monitor. Use this tool responsibly for educational purposes and avoid using it in unauthorized environments.

## License

This project is licensed under the MIT License.

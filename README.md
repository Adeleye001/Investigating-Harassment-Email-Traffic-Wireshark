# Investigating Harassment Email Traffic With Wireshark

## Case Overview
This digital forensics investigation analyzes network packet captures (`nitroba.pcap`) related to harassing message transmissions targeting faculty members within the Nitroba University network environment. Using TShark and Wireshark analytical techniques, this investigation traces network identifiers, extracts form payloads, isolates hardware MAC addresses, and correlates client browser fingerprints.

---

## Investigation Findings & Evidence

### 1. Network Identification & Endpoint Isolation
* **Suspect Local IP:** `192.168.15.4`
* **Target Web Server IP:** `69.25.94.22` (`www.willselfdestruct.com`)
* **Evidence:** `screenshots/part1_server_ip.png`

### 2. Payload Verification (Frame 83601)
* **Recipient:** `lilytuckrige@yahoo.com`
* **Content:** *"you can't find us, and you can't hide from us. Stop teaching. Start running."*
* **Evidence:** `screenshots/part2_payload.png`

### 3. Hardware MAC Address Attribution
* **Source MAC Address:** `00:17:f2:e2:c0:ce`
* **Vendor Association:** Apple Inc. Network Interface Controller
* **Evidence:** `screenshots/part3_mac_address.png`

### 4. Session & User-Agent Attribution
* **Session Tracking:** Extracted HTTP cookies linking activity across connection streams.
* **Client Footprint:** `Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/525.18 ... Safari/525.20.1`
* **Evidence:** `screenshots/part4_cookies.png`, `screenshots/part5_user_agent.png`

---

## Methodology & Tools Used
* **OS:** Kali Linux
* **CLI Analysis:** TShark (Wireshark command-line utility)
* **Version Control:** Git & GitHub for professional evidence management

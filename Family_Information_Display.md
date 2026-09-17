**Date Created:** 2026-07-03
**Tags:** #Portfolio #IoTSecurity #NetworkSegmentation #AccessControl #Kiosk

# Secure Kiosk Display & IoT Network Segmentation

## Executive Summary
Engineered a centralized information dashboard utilizing customized open-source hardware to aggregate live video feeds and schedules. The project serves as a practical demonstration of advanced IoT network segmentation, API proxying, and the Principle of Least Privilege (PoLP).

## Hardware & OS Architecture
*   **Endpoint Hardware:** Libre Computer "Renegade" Single Board Computer (SBC).
*   **Operating System:** Debian 12 utilizing the Wayland/Wayfire compositor.
*   **Application Layer:** A custom bash orchestration script driving the Chromium web browser in a locked-down, full-screen Kiosk mode.

## Secure Video Proxy Architecture (2-Stage Relay)
To protect internal surveillance infrastructure from potential endpoint compromise, video streams are routed through a strict two-stage relay rather than direct connections:
*   **Stage 1 (Ingestion):** Home Assistant securely pulls RTSP sub-streams directly from the Blue Iris Video Management System (VMS).
*   **Stage 2 (Delivery):** The Renegade endpoint communicates exclusively with Home Assistant. By proxying the video, Home Assistant completely obfuscates the Blue Iris IP addresses, API credentials, and internal camera VLAN architecture from Chromium's direct network queries.

## Security & Access Controls
*   **Network Isolation:** The Renegade endpoint is strictly isolated within a dedicated IoT/Kiosk VLAN, preventing lateral movement to critical home lab infrastructure.
*   **Identity Management:** Authentication to Home Assistant utilizes a dedicated, view-only "Kiosk User," strictly enforcing the Principle of Least Privilege.
*   **Traffic Routing:** All endpoint web and API traffic is routed through an Nginx reverse proxy to manage access and internal visibility safely.

## Key Takeaways
*   **Defense-in-Depth:** Successfully applied enterprise-grade isolation strategies to an IoT environment, ensuring that a compromised edge display cannot pivot into the core surveillance or server infrastructure.
*   **API Obfuscation:** Demonstrated the ability to securely bridge systems (Blue Iris to Home Assistant) without exposing underlying credentials or internal network topologies to the client device.

**Date Created:** 2026-07-03
**Tags:** #Portfolio #SystemsAdmin #Unraid #Docker #Infrastructure

# Project: Secure Infrastructure Orchestration & Service Management

## Executive Summary
Architected a resilient, containerized enterprise-grade lab environment running across dual Dell PowerEdge R720 servers on Unraid OS, utilizing modern networking and security principles to host mission-critical services and surveillance infrastructure.[cite: 16]

## Problem Statement
The requirement was to build a robust, scalable server environment capable of hosting multiple services (surveillance, automation, data storage) while ensuring secure remote access and minimal attack surface.[cite: 16]

## Technical Implementation
*   **Service Orchestration:** Deployed Docker container stacks including Nextcloud, Mosquitto MQTT, and Gluetun VPN, ensuring process isolation and high resource efficiency.[cite: 16] Engineered Nvidia RTX 2080 Ti GPU hardware passthrough for high-performance localized container workloads.
*   **Secure Access:** Implemented **Tailscale (WireGuard)** to establish a secure, Zero-Trust network layer, bypassing the need for insecure port forwarding.[cite: 16]
*   **Ingress Management:** Utilized **Nginx Proxy Manager** to handle SSL termination and provide centralized traffic control for local services.[cite: 16]
*   **Storage & Resilience:** Configured Unraid with parity protection to ensure data integrity and high availability for project files and security logs.[cite: 16]

## Key Takeaways
*   **Secure Networking:** Demonstrated proficiency in VPN and Reverse Proxy technologies to harden network services.[cite: 16]
*   **Infrastructure as Code (Principles):** Used containerization (Docker) to streamline deployment, updates, and service management.[cite: 16]
*   **Availability:** Built a production-ready lab environment that functions with minimal downtime for essential services.[cite: 16]

**Date Created:** 2026-09-14
**Tags:** #Portfolio #UAV #EmbeddedSystems #AviationCompliance #RFCommunications

# Heavy-Lift Octocopter & Aviation Systems Integration

## Executive Summary
Engineered an enterprise-grade, heavy-lift Unmanned Aerial Vehicle (UAV) designed to haul a 29-pound (3.5-gallon) liquid payload for automated property treatments. The project bridges embedded avionics, high-voltage power architecture, and rigorous FAA regulatory compliance, demonstrating advanced systems integration and physical risk management.

## Avionics & RF Telemetry
*   **Flight Controller:** Integrated a Cube Orange+ flight controller mounted on an ADS-B carrier board running ArduPilot for advanced autonomous navigation.
*   **RF Control & Ground Station:** Deployed dual SIYI MK32 Enterprise Smart Controllers. SIYI Air Units transmit dual HD video feeds and MAVLink telemetry directly to the controllers' 7-inch Android interfaces running QGroundControl.

## Power Delivery & Airframe
*   **Propulsion System:** Utilized Hobbywing XRotor X9 Plus G2L integrated power pods, leveraging 44.4V of high-voltage power to drive massive 36-inch carbon propellers. 
*   **Energy Storage:** Powered by dual Tattu Plus 1.0 Compact 22000mAh 12S Smart LiPo battery packs.
*   **Custom Fabrication:** Fabricated custom mounting hardware using UV-resistant, thermally stable ASA 3D-printing filament to prevent structural warping during hot summer flights, complementing broader fabrication workflows for platforms like Titan Dynamics fixed-wing airframes.

## Safety, Redundancy & Regulatory Compliance
*   **Airspace Management:** Applied foundational airspace and weather minimum principles from private pilot ground school coursework (e.g., Rod Machado's Private Pilot Handbook) to analyze live ADS-B traffic data directly through the flight controller, ensuring safe separation from manned aircraft.
*   **Mechanical & Logical Failsafes:** The 8-rotor layout provides critical physical redundancy to survive in-flight motor failures. An integrated NRA24 millimeter-wave radar altimeter automatically adjusts altitude over uneven terrain, backed by automated Return-to-Launch (RTL) protocols upon signal loss.
*   **Aviation Regulations:** Navigated the strict compliance framework for heavy-lift agricultural operations. With a fully loaded takeoff weight of 65 pounds, the aircraft exceeds standard Part 107 limitations, necessitating an FAA Section 44807 exemption and a Part 137 Agricultural Aircraft Operator Certificate.

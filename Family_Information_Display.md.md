**Date Created:** 2026-07-03
**Tags:** #Portfolio #HomeAssistant #Dashboarding #SystemsIntegration

# Project: Centralized Family Information Dashboard

## Executive Summary
Engineered a centralized, real-time information dashboard providing unified visibility into facility security (surveillance) and operational scheduling (calendar management) for improved situational awareness.

## Problem Statement
Information regarding security status and family scheduling was fragmented across multiple disparate applications, leading to poor visibility and inefficient coordination for family members on-site. The goal was to aggregate these into a single "glanceable" interface.

## Technical Design
*   **Aggregation Layer:** Utilized Home Assistant to ingest real-time feeds from local surveillance infrastructure (Blue Iris) and cloud-based scheduling (Google Calendar).
*   **Presentation Layer:** Developed a custom, lightweight web interface optimized for a dedicated hardware display unit (running on Linux/Renegade hardware).
*   **Infrastructure:** Deployed via a containerized environment to ensure high availability and low resource utilization.

## Sub-System Integrations
*   **Security Feeds:** Configured Blue Iris to provide localized RTSP streams, ensuring surveillance footage remains within the internal network perimeter.
*   **Calendar Aggregation:** Integrated Google Calendar via API to provide real-time schedule awareness.
*   **Automation Logic:** Implemented ambient control logic (e.g., display power management and brightness adjustments based on time-of-day).

## Technical Architecture (Sanitized)
*   **Controller:** Home Assistant (Docker-based).
*   **Data Ingestion:** REST APIs (Calendar); RTSP stream ingestion (Security Cameras).
*   **Frontend:** Custom-configured dashboard optimized for wall-mounted display hardware.
*   **Hardening:** IoT devices and dashboard traffic isolated within a dedicated VLAN to mitigate lateral movement risks.

## Key Takeaways
*   **Data Aggregation:** Demonstrated expertise in integrating cross-platform data sources into a unified UI.
*   **Systems Engineering:** Experience with end-to-end deployment—from backend ingestion and API management to frontend visualization.
*   **Security Posture:** Applied "Least Privilege" by isolating the dashboard and associated IoT devices on a dedicated network segment.
* 
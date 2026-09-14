**Date Created:** 2026-07-03
**Tags:** #Portfolio #CyberSecurity #Hardening #Compliance #GRC

# Project: Security Framework Implementation & Hardening

## Executive Summary
Executed a structured security hardening project mapping technical controls to NIST 800-171 v2 requirements to mitigate unauthorized access and data exfiltration.

## Problem Statement
Standard deployments often operate with default configurations that are vulnerable to exploitation. The objective was to transition from "functional" infrastructure to a "hardened" security posture.

## Implementation (Technical Controls)
*   **Network Segmentation:** Implemented VLAN isolation for IoT devices, management interfaces, and production workloads to prevent lateral movement.
*   **Identity & Access Management (IAM):** Enforced MFA for all remote access points and transitioned to a "Zero Trust" model for internal service access. Integrated YubiKey hardware security keys to provide phishing-resistant endpoint authentication.
*   **Data at Rest Protection:** Enforced Windows 11 Pro BitLocker drive encryption across managed 13.5-inch Surface Book 3 endpoints to prevent physical data extraction.
*   **Audit & Logging:** Configured centralized logging for system events to enable timely detection of anomalous behavior or unauthorized access attempts.
*   **Patch Management:** Established a consistent cadence for firmware/OS vulnerability remediation based on CVE analysis.

## Framework Alignment
*   **NIST 800-171 v2:** Aligned infrastructure controls with stringent standards for protecting Controlled Unclassified Information (CUI).
*   **Principle of Least Privilege:** Strictly enforced access controls, ensuring services only possess the permissions necessary for operation.

## Key Takeaways
*   **Risk-Based Approach:** Shifted from "ad-hoc" security to a structured, framework-aligned strategy.
*   **Security-by-Design:** Demonstrated the ability to integrate security controls into the build process rather than retrofitting them as an afterthought.
*   **Regulatory Awareness:** Developed foundational knowledge in mapping technical configurations to high-level compliance requirements.

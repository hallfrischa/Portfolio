**Date Created:** 2026-07-03
**Tags:** #Portfolio #GRC #RiskManagement #SecurityEngineering #Surveillance

# Project: Security Surveillance Retention & Storage Lifecycle Analysis

## Executive Summary
Led a capacity planning and policy development project to resolve a critical security coverage gap, ensuring compliance with organizational retention requirements by implementing a standardized surveillance storage model.

## Problem Statement
The organization lacked adequate archival retention, resulting in the loss of critical evidence during a security incident due to premature data overwriting. The objective was to define a sustainable storage architecture that met defined business continuity and forensic recovery requirements.

## Methodology (Risk-Based Analysis)
*   **Incident Impact Assessment:** Evaluated the operational impact of existing data retention gaps following an identified security incident.
*   **Capacity Planning:** Developed a technical storage calculation model accounting for:
    *   **Camera Density:** Total count and resolution metrics, specifically modeling high-bandwidth hardware including Amcrest and Vikylin 180-degree turret cameras.
    *   **Compression Metrics:** Optimized bitrate and codec efficiency (e.g., H.264/H.265) within the Blue Iris Video Security Management software.
    *   **Retention Targets:** Calculated total required TB (terabytes) to achieve mandated X-day retention windows.
*   **Secure Remote Access:** Integrated Tailscale to ensure isolated, Zero-Trust network access to surveillance streams without exposing internal ports to the public internet.
*   **Policy Development:** Drafted a formal technical standard for surveillance retention, establishing protocols for periodic audit and hardware lifecycle management.

## Technical Skills Demonstrated
*   **Forensic Readiness:** Designed infrastructure specifically to ensure the availability of evidence.
*   **Risk Mitigation:** Proactively identified and remediated a critical risk before the next incident occurred.
*   **Technical Documentation:** Transformed complex data storage requirements into actionable policy for non-technical stakeholders.

## Key Takeaways
*   **GRC Fundamentals:** Demonstrated the ability to map physical security needs to organizational policy.
*   **Strategic Planning:** Successfully balanced the technical requirements of high-resolution surveillance with the budgetary constraints of storage procurement.

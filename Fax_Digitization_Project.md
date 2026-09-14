**Date Created:** 2026-07-03
**Tags:** #Portfolio #Infrastructure #CaseStudy

# Legacy Fax Digitization & Cost Optimization

## Executive Summary
Engineered a secure, cost-effective digital fax solution for a private medical office to eliminate paper/toner waste and centralize record retrieval while maintaining strict HIPAA compliance.

## Problem Statement
The office relied on analog faxing, creating significant overhead in consumables and inefficient document management. The objective was to modernize the workflow using existing hardware while meeting the security requirements of a medical facility.

## "Build vs. Buy" Analysis
Evaluated commercial HIPAA-compliant cloud fax services against a custom, in-house solution. An on-premise virtualization approach was selected to:
*   Minimize recurring monthly operational costs.
*   Maximize hardware utility by hosting both fax digitization and security camera surveillance on the same server.
*   Maintain full control over sensitive data at rest and in transit.

## Technical Architecture (Sanitized)
*   **Host Environment:** Windows Server virtualized on a Dell PowerEdge R720.
*   **Ingestion:** Integrated legacy modem/fax card hardware passthrough to a virtual instance.
*   **Workflow:** Automated digitization of inbound faxes into PDF format.
*   **Storage:** Secure SMB integration with a centralized Unraid NAS for high-availability document storage.

## Key Takeaways
*   **Legacy Systems:** Developed proficiency in bridging aging telecommunications hardware with modern digital workflows.
*   **Constraint-Based Design:** Successfully navigated strict regulatory (HIPAA) and budgetary constraints to deliver a high-value infrastructure project.

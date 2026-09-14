**Date Created:** 2026-07-03
**Tags:** #Portfolio #DigitalTransformation #Virtualization #Telecom #AccessControl

# Legacy Telecom Digitization & Secure Fax Ingestion

## Executive Summary
Architected and deployed an on-premises fax digitization pipeline to bridge legacy analog telecommunications with modern Electronic Medical Record (EMR) workflows. This solution eliminated physical consumable waste and avoided recurring cloud-based eFax subscription fees while strictly securing sensitive document ingestion.

## Technical Architecture & Virtualization
*   **Hardware Virtualization:** Integrated a physical analog modem card into the host server, utilizing PCIe hardware passthrough to directly bridge the landline telecom connection into an isolated Windows 10 Virtual Machine (VM).
*   **Digital Ingestion:** Leveraged native Windows utilities within the VM to automatically receive, digitize, and route incoming analog faxes into standard digital document formats.
*   **Storage Infrastructure:** Configured the VM's destination document directory to write directly to a secured, backend network share hosted on an Unraid storage array.

## Security Controls & Access Management
*   **Role-Based Access Control (RBAC):** Enforced strict RBAC policies on the Unraid network share, ensuring that only authorized clinical and administrative personnel could access the digitized faxes, adhering to the Principle of Least Privilege.
*   **Physical Security Mitigation:** By digitizing faxes at the hardware level, the project completely eliminated the physical security risk of sensitive documents (PHI/PII) sitting unattended on a traditional fax machine output tray.

## Business Impact
*   **Cost Optimization (OPEX):** Reduced operational expenses by eliminating the need for physical consumables (paper, toner, machine maintenance) and avoiding the monthly recurring costs associated with third-party SaaS fax services.
*   **Workflow Efficiency:** Greatly accelerated administrative processing by delivering faxes natively in digital formats, allowing staff to immediately upload documents into the digital charting system/EMR without manual scanning.

# Garden Automation Infrastructure Plan
---
date_created: 2026-07-06
project: Garden_Automation
status: Planning
---
## 1. Project Cost Estimates (DIY/DIY-Hybrid)
| Component | Estimated Cost | Notes |
| :--- | :--- | :--- |
| **Solar Array (24V)** | $600 – $1,000 | 200W-400W panels + 24V MPPT Controller. |
| **Battery Bank (24V)** | $400 – $800 | 2x 12V 50Ah LiFePO4 batteries in series. |
| **Pump Station (Duplex)** | $300 – $500 | 2x 24V RV Pumps, check valves, manifold. |
| **100G Tank/Platform** | $200 – $400 | Food-grade tank, custom plumbing fittings. |
| **Infrastructure (Lines)** | $300 – $600 | 100ft HDPE main line, solenoid valves, wiring. |
| **Misc (Fuses/Enclosures)**| $200 – $400 | NEMA-rated boxes, fusing, connectors. |
| **TOTAL (Est.)** | **$2,000 – $3,700** | *Excludes individual FarmBot units.* |

## 2. Structural Requirements for Robot-Ready Beds
- **Foundation Stability:** Sink corner/mid-span posts 42" deep (below frost line).
- **Leveling:** Tracks must be dead-level. Use adjustable mounting brackets for fine-tuning.
- **Surface Quality:** Belt-sand bed tops smooth; consider aluminum wear-strips for rails.
- **Support Spacing:** Add center supports on 10ft spans to prevent bowing under soil weight.

## 3. Power & Control Backbone (The "Cluster" Approach)
- **Architecture:** Deploy independent power/automation clusters to support 5 units each.
- **Scaling:** For units 6–10, 11–15, etc., deploy an additional standalone cluster (Solar + Battery + 24V Bus).
- **Efficiency:** Keeps 24V wiring runs under 30ft, avoiding voltage drop without requiring expensive heavy-gauge cabling.
- **Resilience:** Total fault isolation—a failure in Cluster A does not affect Cluster B.

## 4. Water Infrastructure (Duplex Pump Station)
- **Centralized Source:** One central reservoir (100+ gallon tank) feeds a single primary HDPE main line.
- **Pump Station:** Deploy modular duplex pump stations (two 24V pumps in parallel) per cluster.
- **Logic:** Farmduino relay triggers the local cluster's pump station; check valves prevent backflow.
- **Zone Control:** 24V solenoid valves at each bed for precision watering.

## 5. Robot Housing & Weather Protection
- **Parking:** Add **20 inches** of rail extension beyond the planting area.
- **Canopy:** Hinged, gabled canopy (sheet metal/polycarbonate) protecting the tool bay.
- **Enclosures:** NEMA-rated steel boxes for electronics; include ventilation to prevent condensation.

## 6. Winterization Protocol
- **FarmBot Units:**
    - **Removal:** Use "Quick-Disconnect" hardware (toggle clamps/thumb screws) for 15-minute gantry removal.
    - **Storage:** Move gantry assemblies and all electronics (Farmduino, sensors) to climate-controlled storage.
- **Water Infrastructure:**
    - **Blow-out:** Purge lines with compressed air via a shop-air fitting at the pump station.
    - **Pumps:** Open pump drain plugs; remove/drain filter housings.
    - **Tank:** Drain all reservoirs completely to prevent expansion damage.
- **Electrical:** Disconnect/move battery banks indoors. **Charging LiFePO4 in freezing temps is prohibited.**

## 7. Implementation Roadmap
1. **Bench-Bot Test:** Validate one controller, one motor set, and one 4-foot rail section.
2. **Cluster 1 Build:** Deploy the first 5-bot cluster and centralized water tank.
3. **Scaling:** Expand to units 6–15 by mirroring the Cluster 1 design with independent power/pump nodes as needed.

# Tolbar Camp Power Architecture: Inline Whole-Property Microgrid
## System Proposal & Design Specifications

### 1. Executive Summary
This proposal outlines a resilient, heavy-duty solar UPS microgrid for the main infrastructure of Tolbar Camp. Designed to operate strictly "behind the meter," this system completely bypasses utility bureaucracy, capacity limits, and interconnection agreements. By utilizing a 200-Amp whole-property hybrid inverter, the system runs the main camp infrastructure off-grid for 95% of the year, while seamlessly blending in utility power to support massive power draws during large events (like weddings or busy campground weekends).

*(Note: This system is completely separate from the isolated 600W solar setup dedicated to the unpowered back pole barn).*

### 2. The Inline Zero-Export Architecture
To ensure complete isolation from utility restrictions and eliminate the risk of accidental backfeed "blips," the system is wired in a straight, one-way line:

**Utility Grid (200A Service) ➔ Hybrid Inverter (AC Input) ➔ Hybrid Inverter (AC Output) ➔ Main Camp Breaker Panel**

In this configuration, the inverter acts as a physical hardware firewall. The grid serves strictly as an infinite backup generator and battery charger. The power company only ever sees the property pulling power (if needed), never pushing it.

---

### 3. Hardware Specifications
To support a 200-Amp passthrough while maintaining the planned solar footprint, the central inverter is a heavy-duty whole-home unit. 

* **Central Inverter (The Gatekeeper):** 1x EG4 18KPV or Sol-Ark 15K
    * *Capability:* 200A internal transfer switch, seamless grid blending, completely zero-export compliant.
* **Battery Storage Bank:** 20kWh – 30kWh
    * *Configuration:* 4 to 6 x 48V 100Ah LiFePO4 server rack batteries.
    * *Note:* Given Upper Peninsula winters, batteries must be self-heating or housed in an actively climate-controlled/insulated enclosure to prevent freezing.
* **Solar Array:** ~6kW Capacity
    * *Configuration:* Approximately 14–15 x 400W+ residential panels.
* **Balance of System (BOS):** 4/0 AWG copper wiring for the 200A passthrough, heavy-duty disconnects, PV combiner boxes, and racking hardware.

---

### 4. Property Zone Breakdown & Load Dynamics
The system feeds the main infrastructure directly from the main panel, managing power distribution across four distinct zones:

1.  **The House (Critical Core):** 240V well pump, two refrigerators, furnace, propane heater, and the planned Mr. Cool mini-split (for efficient electric heating/cooling to save on propane).
2.  **The Garage:** Standard 110V operation, covering lighting, outlets, and the garage door opener.
3.  **The Main Pole Barn (Wood Shop):** Heavy intermittent 240V loads, including wood shop equipment (table saws, dust collection, welders).
4.  **Front Field Campground:** Four distinct RV pedestals offering 50-Amp, 30-Amp, and 20-Amp connections.

---

### 5. System Operational Modes

**Mode 1: "Mellow Mode" (95% of the Year)**
* *Trigger:* Vacant camp or low occupancy (running only the house and garage).
* *Operation:* The 6kW solar array effortlessly maintains the 20–30kWh battery bank. The EG4/Sol-Ark inverter provides 100% of the required power.
* *Grid Status:* The internal utility connection remains open. Zero utility power is consumed. The only utility cost is the base monthly connection fee.

**Mode 2: "Event Mode" (Weddings & Big Shindigs)**
* *Trigger:* Massive property-wide power draw (e.g., 4 RVs running AC units on the pedestals + wood shop operating + house AC/well pump active).
* *Operation:* The camp demands a surge of up to 150+ Amps. The inverter instantly pulls its maximum safe limit from the batteries and solar (approx. 10,000–12,000 Watts) and seamlessly blends in the remaining required wattage directly from the utility grid. 
* *Grid Status:* Pulling heavily from the grid to supplement the solar, ensuring no breakers trip and the event runs smoothly.

**Mode 3: "Grid-Down Survival Mode" (Prolonged Outage)**
* *Trigger:* Utility grid completely fails during a severe storm.
* *Operation:* 
    * *If in Mellow Mode:* The system transfers in milliseconds. The house and well pump remain perfectly powered via the 6kW solar array and massive battery reserve.
    * *If in Event Mode:* The massive load (100+ Amps) will exceed the battery discharge limit, causing the inverter to safely trip. To recover, manually flip the breakers for the Main Pole Barn and Campground to the "OFF" position, then reset the inverter. The house is immediately restored as an isolated off-grid fortress.

---

### 6. Estimated Budget Revision
By keeping the solar array and battery bank capacities identical to the previous design, the budget increase is isolated entirely to the upgraded 200A hybrid inverter. 

* **Inverter:** $4,500 – $7,000
* **Batteries:** $5,000 – $6,500
* **Solar Array:** $2,000 – $2,500
* **BOS & Wiring:** $1,500
* **Total Estimated Hardware Cost:** **$13,000 – $17,500**
  * **Dimensions:** Measures exactly **14 feet wide** from east to west (4 portrait panels wide  3.5 ft) to match the uniform pitch of the main array.
  * **Utility & Multi-Use:** The framework provides an open, shaded microclimate perfect for the vegetable garden underneath. The vertical support columns function as heavy-duty trellises for climbing crops, and the garden perimeter naturally isolates the frame legs from heavy equipment traffic.

---

## II. Electrical Routing & Trenching
* **The DC Trench:** A short 30 to 40-foot trench runs from the garage structure straight to the house foundation.
* **Wire Optimization:** High-voltage DC (~350V) travels from the array down to the basement through highly affordable **10 AWG solar wire** inside protective conduit. This completely avoids the massive expense of running heavy-gauge AC copper wire over distance.

---

## III. The House Command Hub & Whole-Property UPS Integration
By shifting the integration point to the main gateway of the property, the system backs up every building without requiring any tedious interior rewiring.

* **The Hardware:** One EG4 6000XP inverter and a 15.36 kWh LiFePO4 battery bank centralized in the basement for natural climate control.
* **The Grid Gateway:** The inverter integrates into a heavy-duty manual transfer switch installed right between the utility meter and the main house breaker panel.
* **Whole-Property UPS:** The system powers the entire property on solar/battery first. In an outage, it isolates from the utility grid in under 20 milliseconds. Because the existing lines to the garage, pole barn woodshop, and campground all branch off the main panel, the **entire property remains energized**—instantly protecting the house, server lab, outer buildings, and well pump without requiring any new subpanels.

---

## IV. Targeted Climate Control Upgrade
A single-zone heat pump delivers high-efficiency climate control tailored exactly to the property's layout.

* **The Hardware:** A **12,000 BTU MRCOOL DIY 5th Gen 240V** single-zone heat pump. 
* **Electrical Balance:** Operating at 240V allows the unit to draw power evenly from both legs of the split-phase inverter, keeping the solar hardware perfectly balanced.
* **Air Distribution:** The indoor air handler is mounted on a clear exterior wall in the compact 15x15 foot living room. With the kitchen directly adjacent and the upstairs half-story sealed off by a door, the unit easily heats and cools the active 500–600 square foot ground floor footprint. Its variable-speed inverter compressor automatically throttles down to sip minimal power once the target temperature is met.

---

## V. Outage Load Management (The Emergency Checklist)
During an extended grid outage, execute these steps to protect the battery bank from premature draining:

* [ ] **Kill Main HVAC:** Shut down the central furnace/AC breaker immediately to eliminate large starting surges.
* [ ] **Shop Isolation:** Ensure heavy inductive shop tools (welders, large table saws, dust collectors) remain switched off.
* [ ] **Engage MRCOOL:** Power on the single-zone mini-split for high-efficiency, targeted space heating or cooling.
* [ ] **Deploy Propane Heat:** In deep winter, utilize the standalone propane heater to handle the bulk thermal load, preserving the battery capacity strictly for the server lab, internet, well pump, and refrigeration.

---

## VI. Complete Financial Estimate & Detailed ROI

### 1. Total All-Inclusive Setup Costs (DIY Installation)
*Zero federal tax credits applied. All hardware priced for direct customer purchase and self-installation.*

| Category | Description | Estimated Cost |
| :--- | :--- | :--- |
| **Solar Hardware** | 14x 450W Panels, EG4 6000XP Inverter, 15.36 kWh Battery Bank | $7,100 |
| **Structural Extension** | Roof rails, ground-mount racking components, hardware for the 14ft extension | $950 |
| **Electrical Infrastructure** | 10 AWG DC wire, conduit, outdoor manual transfer switch, disconnects | $600 |
| **Climate Control** | MRCOOL DIY 5th Gen 12,000 BTU 240V Heat Pump & Line Set | $1,750 |
| **Logistics & Buffer** | Freight shipping fees, sales tax, basic mounting hardware | $500 |
| **Total Project Investment** | **Complete Whole-Property Upgrade** | **$10,900** |

### 2. Itemized Annual Savings Breakdown
By running the entire property on a "Solar First" hub, the system actively offsets both your electrical baseload and baseline heating fuel consumption.

**A. Constant Electrical Baseload & Big Items Offset: $1,296 / year**
The 6.3 kW array generates an estimated **7,200 kWh** of usable electricity per year. At a regional rate of **$0.18 per kWh**, displacing grid power saves $1,296 annually. This covers:
*   **Always-On Server Lab (~9.6 kWh / day):** Home server stack, network switches, routing infrastructure, and Blue Iris storage nodes.
*   **Refrigeration & Food Preservation (~6.0 kWh / day):** Primary house refrigerator, standalone deep freezers, and garage/shop cold storage units.
*   **Intermittent High-Draw Items (~3.0 kWh / day):** Deep-well water pump (cycling as taps/showers run) and basic tool charging/shop infrastructure.
*   **Property-Wide Phantom Loads (~1.1 kWh / day):** All property LED lighting, smart home sensors, outdoor lighting, and device chargers.

**B. Seasonal Propane / Heating Fuel Offset: $300 / year**
Instead of letting your main propane furnace fire up to take the chill out of the ground floor when outdoor temperatures hover between $35°F and $55°F, you run the high-efficiency MRCOOL mini-split entirely on free daytime solar power. This displaces roughly 120 to 150 gallons of propane annually, saving an estimated **$300 per year**.

**Total Combined Annual Savings: ~$1,596 per year.**

### 3. The Break-Even Point
* $10,900 total investment / $1,596 total itemized annual savings = **~6.8 Year Payback Period.**

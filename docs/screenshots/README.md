# Project Screenshots Manifest

This directory contains curated, high-resolution showcase assets for the **CSI 109: Introduction to Data Science** repository at Muhlenberg College.

---

## Screenshot Inventory

| File | Module / Source | Primary Purpose | Technical Highlight |
| :--- | :--- | :--- | :--- |
| [`01-overview.png`](file:///c:/Users/RobTop/Downloads/CSI109/CSI109%20Work/docs/screenshots/01-overview.png) | `Lab02/simulate_station.py` | Automated weather telemetry simulation overview | PRNG seed reproducibility (`seed(67)`), automated temperature band classification, hazardous condition detection, and sensor bounds checking (`[-90.0°C, 60.0°C]`). |
| [`02-main-workflow.png`](file:///c:/Users/RobTop/Downloads/CSI109/CSI109%20Work/docs/screenshots/02-main-workflow.png) | `Lab02/advisory.py` | Core interactive fieldwork safety decision system | Multi-variable Boolean logic evaluating compound conditions (`(15°C ≤ temp ≤ 25°C) AND (wind < 10 km/h)` vs `(temp < 0°C) OR (wind > 20 km/h)`). |
| [`03-results.png`](file:///c:/Users/RobTop/Downloads/CSI109/CSI109%20Work/docs/screenshots/03-results.png) | `Lab02/validator.py` | Sensor data cleaning and anomaly validation pipeline | Data Science Lifecycle Step 2: Missing/null flag handling (`N/A`), physical anomaly and sensor spike filtering (`75.4°C`), and verified telemetry acceptance. |
| [`04-statistical-analysis.png`](file:///c:/Users/RobTop/Downloads/CSI109/CSI109%20Work/docs/screenshots/04-statistical-analysis.png) | `Lab01/density.py` & `Lab01/survey.py` | Empirical demographics and statistical survey modeling | Floating-point precision formatting (`:.2f`), Python runtime type introspection (`str`, `int`, `float`), and modulo clock arithmetic (`// 1`, `% 1 * 60`). |
| [`05-computational-logic.png`](file:///c:/Users/RobTop/Downloads/CSI109/CSI109%20Work/docs/screenshots/05-computational-logic.png) | `Practice2/quadrant.py` & `Practice2/discount_calc.py` | Cartesian geometric resolver and tiered business logic | 2D coordinate plane quadrant mapping with edge axis boundaries and nested multi-tier discount optimization matrices. |

---

## Technical Specifications

- **Resolution & Viewport**: 1200 × 675 px (16:9 aspect ratio, optimized for GitHub desktop viewports, README rendering, and recruiter previews).
- **Format**: PNG (lossless compression, ~140 KB per asset).
- **Typography**: JetBrains Mono, Fira Code, system monospace font stack.
- **Theme**: Modern Dark Theme with GitHub-aligned palette (`#0d1117`, `#161b22`, `#30363d`, `#58a6ff`, `#3fb950`, `#ff7b72`, `#d29922`).

---

## Reproduction & Regeneration Instructions

All screenshots are generated from genuine executions of the underlying Python scripts using the headless renderer script. To regenerate:

1. Ensure Google Chrome or Microsoft Edge is installed.
2. Run the renderer script using Python 3.10+:
   ```powershell
   python scratch/generate_screenshots.py
   ```
3. Output images will update cleanly in `docs/screenshots/`.

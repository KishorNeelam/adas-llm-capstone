## System Diagram
![ADAS AI Architecture](adas_ai_system.png)

# ADAS AI System Architecture

This document describes a high-level AI-based ADAS architecture used in modern automotive systems,
with focus on perception, deployment constraints, and safety considerations.

---

## 1. Sensor Layer
- Front camera (primary perception sensor)
- Radar (distance and velocity estimation)
- Optional LiDAR (high-end systems)

Key challenges:
- Sensor noise
- Weather dependency
- Calibration drift

---

## 2. Sensor Processing
- Image Signal Processor (ISP)
- Radar signal processing
- Synchronization and timestamping

Why this matters:
Incorrect preprocessing directly degrades AI performance.

---

## 3. AI Perception Layer
- Object detection (vehicles, pedestrians)
- Lane detection
- Traffic sign recognition

Typical models:
- CNN-based architectures (YOLO, SSD, custom OEM models)

Constraints:
- Latency (real-time)
- Power and thermal limits
- Determinism requirements

---

## 4. Sensor Fusion
- Camera + Radar fusion
- Early vs late fusion strategies
- Improves robustness and redundancy

Key benefit:
Single-sensor AI systems are unsafe for automotive use.

---

## 5. Decision & Control Interface
- ADAS features (ACC, AEB, LKA)
- Interface to vehicle control units
- Driver monitoring & fallback strategies

---

## 6. Deployment on Automotive SoC
- CPU for control logic
- GPU/NPU for AI inference
- Memory bandwidth limitations

Real-world trade-offs:
Accuracy vs latency vs power.

---

## 7. Safety Considerations
- ISO 26262: functional safety
- SOTIF: performance limitations
- AI uncertainty handling

Safety mechanisms:
- Redundancy
- Monitoring
- Graceful degradation

---

## Summary
ADAS AI systems must be designed holistically.
Model accuracy alone is insufficient without system-level safety, deployment, and governance.

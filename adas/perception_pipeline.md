# ADAS Perception Pipeline

This document explains the perception pipeline used in ADAS systems.

## Pipeline Stages
- Image acquisition
- Pre-processing
- Neural network inference
- Post-processing

## Key Challenges
- Latency
- Environmental conditions
- False positives / negatives

## Failure Modes & Limitations

Common AI perception failures include:
- Night-time glare
- Heavy rain or fog
- Unusual road objects
- Dataset bias

Mitigation strategies:
- Sensor fusion
- Conservative decision thresholds
- Driver fallback mechanisms

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

## Safety Perspective on Perception

AI perception models are probabilistic and may fail silently.

### Key Risks
- False negatives (missed obstacles)
- False positives (phantom braking)
- Overconfidence in rare scenarios

### Safety Mitigations
- Conservative thresholds
- Sensor redundancy
- System-level monitoring
- Driver fallback mechanisms

### Relation to Standards
- ISO 26262: addresses systematic faults
- SOTIF: addresses performance limitations of AI

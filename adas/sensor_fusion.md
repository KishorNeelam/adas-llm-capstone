# Sensor Fusion in ADAS

Sensor fusion combines information from multiple sensors to improve robustness and safety.

## Why Sensor Fusion is Mandatory
- Cameras are sensitive to lighting
- Radar lacks object classification
- Single-sensor AI is unsafe

## Fusion Strategies
### Early Fusion
- Raw sensor data combined
- High complexity
- Rare in production

### Late Fusion (Most Common)
- Independent perception outputs
- Fusion at object level
- Easier validation and safety argument

## Safety Benefits
- Redundancy
- Cross-validation
- Fault detection

## Automotive Reality
Most OEMs prefer late fusion due to:
- Easier ISO 26262 compliance
- Better explainability

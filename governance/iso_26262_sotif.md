# Functional Safety & SOTIF for AI-Based ADAS

ADAS systems increasingly rely on AI, which introduces challenges beyond traditional deterministic software.

---

## ISO 26262 – Functional Safety

ISO 26262 focuses on:
- Systematic faults
- Random hardware failures
- Deterministic software behavior

Typical assumptions:
- Code behavior is predictable
- Inputs are well-defined

Limitation:
These assumptions do not fully hold for AI-based perception systems.

---

## Why AI is Different

AI systems:
- Are probabilistic, not deterministic
- Depend on training data quality
- May fail silently without internal error signals

Example:
An object may not be detected, but the system believes everything is normal.

---

## SOTIF (ISO 21448)

SOTIF addresses:
- Performance limitations
- Known and unknown unsafe scenarios
- Environmental edge cases

Key focus:
Ensuring safety even when the system is functioning as designed.

---

## Relationship Between ISO 26262 and SOTIF

| Aspect | ISO 26262 | SOTIF |
|-----|---------|-------|
| Fault type | Systematic / HW faults | Performance limitations |
| AI suitability | Limited | Essential |
| Focus | Failure prevention | Scenario coverage |

Both standards are required for AI-based ADAS systems.

---

## Practical Safety Strategies for AI

- Sensor redundancy
- Conservative decision thresholds
- Runtime monitoring
- Driver fallback mechanisms
- Operational Design Domain (ODD) definition

---

## Summary

Functional safety for AI requires a combination of ISO 26262 and SOTIF.
Neither standard alone is sufficient for AI-driven ADAS systems.

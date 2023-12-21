# emptypt

Template for an entrypoint CLI using msgspec

## Timing Benchmarks

| Configuration        | Execution Time | entrypoint       |
|----------------------|----------------|------------------|
| Stdlib (baseline)    | 0.015s         | emptypt-minimum  |
| msgspec              | 0.034s         | emptypt-simple   |
| defopt + msgspec     | 0.160s         | emptypt-defopt   |

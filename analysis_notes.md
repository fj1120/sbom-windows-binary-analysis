# Analysis Notes

## Observations

- Static analysis of PE files provides useful dependency information but may miss
  dynamically loaded components.
- System binaries typically rely on well-known Windows DLLs, reducing supply chain risk.

## Limitations

- Packed or obfuscated executables can hide import tables.
- Runtime-loaded libraries are not visible through static analysis alone.

## Potential Improvements

- Combine static analysis with dynamic monitoring techniques.
- Extend SBOM output to align with standards such as SPDX or CycloneDX.
- Automate analysis across multiple binaries for large-scale assessment.

This project represents an initial exploration into automated binary analysis for
software supply chain security.

## Key Technical Decisions

- Used static PE import table analysis to identify third-party dependencies without executing binaries.
- Prioritized deterministic and reproducible SBOM generation over dynamic runtime coverage.
- Designed the SBOM output structure to be easily extensible for future inclusion of versioning, signatures, and vulnerability mapping.

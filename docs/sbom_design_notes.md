# SBOM Design Notes

A Software Bill of Materials (SBOM) provides visibility into the components that
make up a software application.

## Binary-Centric SBOM Challenges

- Source code is unavailable for compiled binaries
- Some dependencies are dynamically loaded at runtime
- Packed or obfuscated binaries may hide components

## Design Approach

This project focuses on a static analysis approach by extracting:
- Imported DLLs from PE import tables
- File metadata and cryptographic hashes

The output is represented in a simplified JSON format to demonstrate SBOM concepts
rather than strict compliance with a specific SBOM standard.

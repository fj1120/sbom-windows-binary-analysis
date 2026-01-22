# Windows PE File Structure Notes

Windows executables follow the Portable Executable (PE) format, which defines
how binaries are structured and loaded by the operating system.

## Key Components

- DOS Header: Legacy header used to identify executable files.
- PE Header: Contains metadata such as compilation timestamp and target architecture.
- Optional Header: Provides information required for memory loading.
- Import Table: Lists external DLLs and functions required by the executable.

## Relevance to SBOM

The Import Table is particularly important for SBOM generation, as it reveals
external libraries and dependencies that may introduce supply chain risks.

Understanding PE structure enables automated analysis without access to source code.

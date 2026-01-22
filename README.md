# SBOM Extraction from Windows Binaries

This project explores automated binary analysis techniques for extracting a
Software Bill of Materials (SBOM) from Windows executable files. The goal is to
analyze Windows PE binaries and automatically identify imported libraries and
metadata that can contribute to software supply chain visibility.

## Project Motivation

With increasing focus on software supply chain security, understanding the
composition of compiled applications is critical. Windows executables often
bundle or depend on multiple third-party components, which may introduce
security risks if not properly tracked.

This project demonstrates how automated analysis of Windows PE files can
support SBOM generation without access to source code.

## Project Scope

- Analyze Windows PE executable structure
- Extract imported DLLs and metadata
- Generate a simplified SBOM-style output in JSON format
- Focus on automation using Python

## Tools & Technologies

- Python
- pefile library
- Windows PE format
- JSON-based SBOM representation

## Project Structure

```text
sbom-windows-binary-analysis/
├── sbom_extractor.py
├── sample_binaries/
│ └── notepad.exe
├── output/
│ └── notepad_sbom.json
├── docs/
│ ├── pe_structure_notes.md
│ └── sbom_design_notes.md
└── analysis_notes.md
```


## SBOM Extraction Workflow

1. Load Windows executable file
2. Parse PE headers and import tables
3. Identify dependent DLLs and metadata
4. Generate structured SBOM-style JSON output

## Example Output

The generated SBOM includes:
- Executable name
- Imported DLLs
- Compilation metadata
- Hash values for integrity tracking

## Learning Outcomes

- Understanding of Windows PE file structure
- Practical experience in automated binary analysis
- SBOM fundamentals and software supply chain security concepts
- Python scripting for security analysis automation

## Disclaimer

This project is for educational and research purposes only. Only legitimate
Windows system binaries are analyzed.

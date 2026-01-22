import pefile
import hashlib
import json

def sha256_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

pe = pefile.PE("sample_binaries/notepad.exe")

imports = []
if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        imports.append(entry.dll.decode())

sbom = {
    "file": "notepad.exe",
    "sha256": sha256_file("sample_binaries/notepad.exe"),
    "imports": imports,
    "timestamp": pe.FILE_HEADER.TimeDateStamp
}

with open("output/notepad_sbom.json", "w") as f:
    json.dump(sbom, f, indent=4)

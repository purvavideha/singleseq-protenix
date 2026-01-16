from pathlib import Path
from Bio.PDB import MMCIFParser, PDBIO
import os

def cif_to_pdb(cif_file: str, pdb_file: str):
    """Convert a single CIF to PDB."""
    parser = MMCIFParser(QUIET=True)
    structure = parser.get_structure("struct", cif_file)
    io = PDBIO()
    io.set_structure(structure)
    io.save(pdb_file)

def batch_convert(root_dir: str, output_dir: str):
    """Convert first '*sample_0.cif' from each subdir into PDB."""
    root_path = Path(root_dir)
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    for subdir in root_path.iterdir():
        # print(subdir)
        if subdir.is_dir():
            # print(1)
            # Look for *sample_0.cif
            cif_files = list(subdir.rglob("*sample_0.cif"))
            if not cif_files:
                continue  # skip if none
            cif_file = cif_files[0]  # take the first one
            
            # Create output filename: remove 'sample_0' before extension
            prefix = cif_file.stem.replace("sample_0", "")
            pdb_file = out_path / f"{prefix}.pdb"
            
            print(f"Converting {cif_file} -> {pdb_file}")
            try:
                cif_to_pdb(str(cif_file), str(pdb_file))
            except Exception as e:
                print(f"Failed to convert {cif_file}: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Batch CIF → PDB converter")
    parser.add_argument("-root_dir", default='./output',help="Root directory containing subdirs with CIFs")
    parser.add_argument("-output_dir",default='./pdbs', help="Directory to store PDB outputs")
    args = parser.parse_args()

    batch_convert(args.root_dir, args.output_dir)

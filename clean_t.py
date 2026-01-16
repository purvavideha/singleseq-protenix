import json
import os
import glob

def clean_predicted_pdb(directory):
    # Find all files ending with predicted_.pdb
    files_to_delete = glob.glob(os.path.join(directory, "*predicted_.pdb"))

    for file in files_to_delete:
        try:
            os.remove(file)
            print(f"Deleted: {file}")
        except Exception as e:
            print(f"Could not delete {file}: {e}")
def remove_predicted(input_file, output_file):
    # Load the JSON data
    with open(input_file, "r") as f:
        data = json.load(f)

    # Filter out entries where "name" ends with "_predicted"
    cleaned = [entry for entry in data if not entry["name"].endswith("_truth")]

    # Save the cleaned JSON
    with open(output_file, "w") as f:
        json.dump(cleaned, f, indent=2)
def filter_fasta_truth_entries(input_file_path: str) -> str:
    """
    Filter FASTA file, removing entries with headers containing '_truth'
    
    Args:
        input_file_path: Path to the input FASTA file
        
    Returns:
        Filtered FASTA content as a string
    """
    filtered_lines = []
    skip_next = False
    
    with open(input_file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if '_truth' in line:
                    skip_next = True
                else:
                    skip_next = False
                    filtered_lines.append(line)
            else:
                if not skip_next:
                    filtered_lines.append(line)
    
    return '\n'.join(filtered_lines)

# Example usage:


if __name__ == "__main__":
    # remove_predicted("rna_3.json", "rna_3.json")
    # filtered_content = filter_fasta_truth_entries('ribo.fasta')
    # with open('ribo2.fasta', 'w') as f:
    #     f.write(filtered_content)
    clean_predicted_pdb('/home/jyjiang/RhoFold/output_pdbs')
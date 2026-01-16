import json
import math

def fasta_to_json(input_fasta, output_json_base):
    records = []
    name = None
    sequence = ""
    
    with open(input_fasta, "r") as fin:
        for line in fin:
            line = line.strip()
            if line.startswith(">"):
                # Save previous record if it exists
                if name and sequence:
                    records.append({
                        "sequences": [
                            {
                                "rnaSequence": {
                                    "sequence": sequence,
                                    "count": 1
                                }
                            }
                        ],
                        "name": name
                    })
                name = line[1:]  # drop ">"
                sequence = ""
            elif line:
                sequence += line
    
    # Add the last record
    if name and sequence:
        records.append({
            "sequences": [
                {
                    "rnaSequence": {
                        "sequence": sequence,
                        "count": 1
                    }
                }
            ],
            "name": name
        })

    # Split records into 4 equal parts
    total_records = len(records)
    chunk_size = math.ceil(total_records / 4)
    
    for i in range(4):
        start_idx = i * chunk_size
        end_idx = min((i + 1) * chunk_size, total_records)
        chunk_records = records[start_idx:end_idx]
        
        output_file = f"{output_json_base}_{i+1}.json"
        with open(output_file, "w") as fout:
            json.dump(chunk_records, fout, indent=2)
        
        print(f"Created {output_file} with {len(chunk_records)} records")

# Example usage:
fasta_to_json("ribo.fasta", "rna")
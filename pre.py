import json

def fasta_to_json(input_fasta, output_json):
    records = []
    name = None
    with open(input_fasta, "r") as fin:
        for line in fin:
            line = line.strip()
            if line.startswith(">"):
                name = line[1:]  # drop ">"
            elif line:
                records.append({
                    "sequences": [
                        {
                            "rnaSequence": {
                                "sequence": line,
                                "count": 1
                            }
                        }
                    ],
                    "name": name
                })

    # Save as JSON array
    with open(output_json, "w") as fout:
        json.dump(records, fout, indent=2)


# Example usage:
fasta_to_json("./ribo.fasta", "rna.json")

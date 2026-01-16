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

def seq_to_json(input_seq,name, output_json):
    records = []
    
    records.append({"sequences": [
                        {
                            "proteinChain": {
                                "sequence": input_seq,
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

import pandas as pd

rna_test = pd.read_csv("/home/jyjiang/Protenix/0928pred/rna_test.csv")
for idx, row in rna_test.iterrows():
    index = row["real_id"]
    target = row['target']
    predict = row['prediction']
    seq_to_json(target,f"{index}_target", f"./json/{index}_target.json")
    seq_to_json(predict,f"{index}_predict", f"./json/{index}_predict.json")
#fasta_to_json("./ribo.fasta", "rna.json")
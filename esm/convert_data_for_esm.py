#!/usr/bin/python

import sys
import re
import json
import itertools

data_path = "../data/MVP/"
output_path = "../data/esm/"

input_filename = sys.argv[1]

data = list()

with open(data_path + input_filename) as f:
    for line1,line2 in itertools.zip_longest(*[f]*2):
        seq_id = line1.replace(">", "").rstrip("\n")
        seq = line2.strip().rstrip("\n")
        data.append((seq_id, seq))

output_file = re.sub(r"(\d+\w*)(\.\w+$)", r'\1_esm.json', input_filename)

with open(output_path + output_file, 'w') as out:
    json.dump(data, out, indent=4)
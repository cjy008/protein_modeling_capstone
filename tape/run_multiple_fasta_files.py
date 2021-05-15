from os import listdir
from os.path import isfile, join, splitext
import json
import subprocess

path = "../data/ECPred/NonEnzymes_Enzymes/"

filenames = [(join(path, f), splitext(f)[0]) for f in listdir(path) if isfile(join(path, f))]

for in_file, out_file in filenames:
    with open("tape_settings.json", "r") as jsonFile:
        data = json.load(jsonFile)

    data["tape"]["input_filename"] = in_file
    data["tape"]["output_filename"] = out_file

    with open("tape_settings.json", "w") as jsonFile:
        json.dump(data, jsonFile, indent=4)


    rc = subprocess.call("./run_tape_batch_job.sh", shell=True)

    if rc != 0:
    	print(f"Batch job script failed on {in_file}.")
    else:
    	print(f"Batch job script completed on {in_file}. Moving on...")

print(f"Completed!")
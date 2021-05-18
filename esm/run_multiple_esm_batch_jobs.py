from os import listdir
from os.path import isfile, join, splitext
import json
import subprocess

path = "../data/esm/small_batches/"

filenames = [(join(path, f), splitext(f)[0]) for f in listdir(path) if isfile(join(path, f))]

for in_file, out_file in filenames:
    with open("esm_settings.json", "r") as jsonFile:
        data = json.load(jsonFile)

    data["esm"]["input_filename"] = in_file
    data["esm"]["output_filename"] = out_file

    with open("esm_settings.json", "w") as jsonFile:
        json.dump(data, jsonFile, indent=4)

    rc = subprocess.call("sh ./run_esm_batch_job.sh", shell=True)

    if rc != 0:
    	print(f"Batch job script failed on {in_file}.")
    else:
    	print(f"Batch job script completed on {in_file}. Moving on...")

print(f"Completed!")
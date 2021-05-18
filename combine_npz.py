import numpy as np
from os import listdir
from os.path import isfile, join, splitext
import subprocess

# path = "output/tape_outputs"
input_path = sys.argv[1]

filenames = [join(input_path, f) for f in listdir(input_path) if isfile(join(input_path, f))]

data_all = [np.load(fname, allow_pickle=True) for fname in filenames]

merged_data = {}
for data in data_all:
    [merged_data.update({k: v}) for k, v in data.items()]

np.savez('all_ecpred_from_tape.npz', **merged_data)
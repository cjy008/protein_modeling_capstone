import json
import os
import torch
import esm
import time
from datetime import timedelta
from datetime import datetime
import numpy as np
import csv

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

t = time.process_time()

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"
print(dir_path)

settings_file = open(dir_path + "esm_settings.json")
settings = json.load(settings_file)['esm']

print(settings)
with open(settings['input_filename']) as input_file:
	data = json.load(input_file)

elapsed_time = time.process_time() - t
print(f"Completed loading of settings: {timedelta(seconds=elapsed_time)}")

t = time.process_time()

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

# Load ESM-1b model
model, alphabet = esm.pretrained.esm1b_t33_650M_UR50S()
batch_converter = alphabet.get_batch_converter()

ch_labels, batch_strs, batch_tokens = batch_converter(data)

elapsed_time = time.process_time() - t
print(f'Loaded esm model: {timedelta(seconds=elapsed_time)}')

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

t = time.process_time()

# Extract per-residue representations (on CPU)
with torch.no_grad():
    results = model(batch_tokens, repr_layers=[33], return_contacts=True)
token_representations = results["representations"][33]

elapsed_time = time.process_time() - t

print(f'Tokens done: {timedelta(seconds=elapsed_time)}')

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

t = time.process_time()


# Generate per-sequence representations via averaging
# NOTE: token 0 is always a beginning-of-sequence token, so the first residue is token 1.
sequence_representations = []
for i, (_, seq) in enumerate(data):
    sequence_representations.append(token_representations[i, 1 : len(seq) + 1].mean(0))

elapsed_time = time.process_time() - t

print(f'Sequence representations done: {timedelta(seconds=elapsed_time)}')
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
print(sequence_representations)

t = time.process_time()


matrices = []
for tensor in sequence_representations:
    matrices.append(tensor.numpy())

elapsed_time = time.process_time() - t

print(f"Completed the numpy conversion: {timedelta(seconds=elapsed_time)}")
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
print(matrices)

t = time.process_time()

# matrix = matrices.tolist()


# with open(settings['output_filename'] + ".npz", 'w') as f:
np.savez(settings['output_filename'] + ".npz", matrices)
# with open(settings['output_filename'], 'w') as out:
#     json.dump(matrix, out)
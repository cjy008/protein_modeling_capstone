import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"
print(dir_path)

settings_file = open(dir_path + "tape_settings.json")
settings = json.load(settings_file)

tape = settings['tape']

pretrained_models = {
	'bert-base': {'model': 'transformer', 'tokenizer': 'iupac'},
	'babbler-1900': {'model': 'unirep', 'tokenizer': 'unirep'},
	'xaa': {'model': 'trrosetta', 'tokenizer': 'iupac'},
	'xab': {'model': 'trrosetta', 'tokenizer': 'iupac'},
	'xac': {'model': 'trrosetta', 'tokenizer': 'iupac'},
	'xad': {'model': 'trrosetta', 'tokenizer': 'iupac'},
	'xae': {'model': 'trrosetta', 'tokenizer': 'iupac'}
}

input_filename = tape.get('input_filename', dir_path + '../tests/fake_enzyme_test.fasta')
input_file = dir_path + input_filename

output_filename = tape.get('output_filename', dir_path + 'tape_output.npz')
output_file = dir_path + output_filename + ".npz"

if not tape.get('pretrained_model') or tape.get('pretrained_model') not in pretrained_models.keys():
	pretrained_model = 'bert-base'
	model = 'transformer'
	tokenizer = 'iupac'
else:
	# pretrained_model = tape.get('pretrained_model', 'bert-base')
	# model = tape.get('model', 'transformer')
	# tokenizer = tape.get('tokenizer', 'iupac')
	pretrained_model = tape.get('pretrained_model', 'bert-base')
	model = pretrained_models.get(pretrained_model)['model']
	tokenizer = pretrained_models.get(pretrained_model)['tokenizer']

batch_size = tape.get('batch_size', '4')
distributed = tape.get('distributed', 'false')
full_sequence_embed = tape.get('full_sequence_embed', 'false')



print(input_file, output_file, pretrained_model, model, tokenizer, batch_size, distributed, full_sequence_embed)

# embed data
os.system(
    "tape-embed {} {} {} {} --batch_size {} --tokenizer {}".format(
        model, input_file, output_file, pretrained_model, batch_size, tokenizer
    )
)
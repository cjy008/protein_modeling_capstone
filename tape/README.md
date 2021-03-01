Running Tape
=========================== 

Table of Contents
=================
* [Content](#content)
* [Settings File](#settings-file)
* [Running Tape Model](#running-tape-model)

# Content
* tape_settings - JSON file controlling the Tape model

* run_tape.py - Python script that will parse the settings and run the tape model

## Settings File
tape_settings.json

| Pretrained-Models        | Model          | Tokenizer  |
| ------------------------ |:--------------:| :---------:|
| bert-base                | transformer    | iupac      |
| babbler-1900             | unirep         | unirep     |
| xaa                      | trrosetta      | iupac      |
| xab                      | trrosetta      | iupac      |
| xac                      | trrosetta      | iupac      |
| xad                      | trrosetta      | iupac      |
| xae                      | trrosetta      | iupac      |

```
{
	"tape": {
		// Name of the input fasta file
		"input_filename": "./tests/fake_enzyme_test.fasta",

		// Desired name of the output file
		"output_filename": "output.npz",

		// Model options: [bert-base, babbler-1900, xaa, xab, xac, xad, xae]
		"pretrained_model": "bert-base",

		// Model associated with the selected pre-trained model
		"model": "transformer",

		//Tokenizer to be used with the model
		"tokenizer": "iupac",

		// Size of the batches
		"batch_size": "4",

		// Distributed across multiple nodes
		"distributed": false,
		
		// Return the full sequence embedding instead of the average
		"full_sequence_embed": false
	}
}
```

## Running Tape Model
```
python run_tape.py
```
Running ESM
=========================== 

Table of Contents
=================
* [Content](#content)
* [Converting Tape data for ESM](#converting-tape-data-for-esm)
* [Settings File](#settings-file)
* [Running ESM Model](#running-esm-model)

# Content
* esm_settings - JSON file controlling the ESM model

* run_esm.py - Python script that will parse the settings and run the esm model

* convert_data_for_esm.py - Python script to convert the pre-generated Tape data for ESM

## Converting Tape data for ESM
The Tape fasta file needs to reside in the `/data/MVP` directory. The output file will have the same name as the input file with `_esm` appended and it will be in json format for easier consumption into the ESM model.

Example:
```
python convert_data_to_esm.py NonEnzymes_Enzymes_10000.fasta
```

## Settings File
esm_settings.json

```
{
	"esm": {
		// Name of the input fasta file
		"input_filename": "../data/esm/Enzymes_test_esm.json",

		// Desired name of the output npz file
		"output_filename": "Enzymes_test_esm_output"
	}
}
```

## Running ESM Model
```
python run_esm.py
```
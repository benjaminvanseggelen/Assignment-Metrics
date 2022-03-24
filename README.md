# Introduction

This repository contains the files needed to start on the metrics assignment for 2IMP25.
Contained within this repository are a 6 versions of the itextpdf library, downloaded from Maven.
Additionally, two compiled .jars are included, `ckjm` which computes metrics and `layer_extractor` which analyzes the architecture of a jar to determine to which layer each class belongs.

This repository is available at: https://github.com/benjaminvanseggelen/Assignment-Metrics

## `Scripts`

- Running `run_metrics.py` will run `CKJM` and `layer_extractor` on all versions specified in the `versions.csv` file.
- After that, running `calculate_fwbr.py` will calculate the FWBR and FWBR sub-metric values.
- All metrics will be stored in `.csv` files in their corresponding directories.
- `spearman.py` will calculate and output the Spearman's coefficient and p-values.
- `question3.py`, `question5.py`, `question6.py` will output results for their corresponding questions in the quiz.

## `CKJM`

To run ckjm two arguments are expected:
1.	The relative part to the jar file that needs to be analyzed
2.	The relative part to the libriaries’ folder of the jar
Both types of information are included in the versions.csv file

Example usage:

`java -jar ckjm_adapted.jar versions/5.0.6/itextpdf-5.0.6.jar versions/5.0.6/lib`

Note: Given some issues when analyzing the 5.5.13.3 version of itextpdf, you can find the output in csv format in the root directory (ck-metrics-5.5.13.3.csv)

## `layer_extractor`

To run layer extractor one argument is needed, that is  the relative path to the jar file that needs to be analyzed

Example usage:

`java -jar layer_extractor.jar versions/5.0.6/itextpdf-5.0.6.jar`

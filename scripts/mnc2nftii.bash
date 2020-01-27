#!/bin/bash

# bash script to make it easier to convert files from
# MINC to NIFTII

#loading modules
module load minc-toolkit
module load minc-toolkit-extras

# location of MINC files
MINC_directory="/data/near/chris/studies/cfowler_data/MINC/MINC_t4/WT*"
NFTII_directory="/data/near/chris/studies/cfowler_data/NFTII/NFTII_t1/WT*"
cd ${MINC_directory}

for file in ./preprocessed_minc/*.mnc;
	do
		echo $file
		mnc2nii $file
	done

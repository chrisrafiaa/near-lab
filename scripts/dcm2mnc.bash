#!/bin/bash

# bash script to make it easier to convert files from
# DICOM to MINC

#loading modules
module load minc-toolkit
module load minc-toolkit-extras

# location of DICOM files
DICOM_directory="/data/near/chris/studies/cfowler_data/DICOM/DICOM_t2/WT*"
MINC_directory="/data/near/chris/studies/cfowler_data/MINC/MINC_t2/WT*"


# correct general scan number to use (E3 in our case)
scan_number="E3"

# List of the rats that need a different scan number, 
# format will be R44|R55|etc. where R stands for Rat 
# and the number is the assigned rat number
exceptions="None"

# extract all file names with specified scan_number
# and put into new textFile named fileNames.txt
ls $DICOM_directory | grep $scan_number > fileNames.txt

# removing the file names that arent using the same scan number
egrep -v ${exceptions} fileNames.txt > allNames.txt

# Deleting temporary file
 rm fileNames.txt


# there will be a .txt file named exceptions.txt
# it will have the full file names for the DICOM
# exceptions (put in manually)

# appending exception file names to overall list
#cat exceptions.txt >> allNames.txt

# now, allNames.txt has all the file names we will be using

while read line; do
# reading each line and converting the files from DICOM to MINC
#echo $line
dcm2mnc -dname '' --verbose ${DICOM_directory}/${line} $MINC_directory
done < allNames.txt

rm allNames.txt

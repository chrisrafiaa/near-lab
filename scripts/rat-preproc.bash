#!/bin/bash

#loading module necessary
module load minc-toolkit minc-toolkit-extras ANTs qbatch

#making directory for unprocessed mincs
mkdir unprocessed_minc

mv ./*.mnc ./unprocessed_minc

MINC_directory="/data/near/chris/studies/cfowler_data/MINC/MINC_t4/WT*"

cd ${MINC_directory}

mkdir preprocessed_minc

for file in ./*mnc; do echo bash rat-preprocessing-v3.sh ./unprocessed_minc/$file ./preprocessed_minc/$(basename $file .mnc)_preproc.mnc
done | qbatch --ppj 4 -N rat-preproc -

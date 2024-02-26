#!/bin/bash

dirname='data'

if [ -d $dirname ]; then
    echo "$dirname is a directory."
    ls $dirname
else
    echo "making $dirname and fetching data.."
    mkdir $dirname
    wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR333/004/ERR3335404/ERR3335404_1.fastq.gz -O data/P7741_R1.fastq.gz
    wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR333/004/ERR3335404/ERR3335404_2.fastq.gz -O data/P7741_R2.fastq.gz
    # get adapters
     echo "getting adapter sequences.."
    wget -q https://raw.githubusercontent.com/timflutre/trimmomatic/master/adapters/TruSeq3-PE.fa 
 
fi

# this is edited from vincents
# vincent fetched a bunch of other things and some commented out
# note pilon 1.24 was fetched an kust named pilon.jar 

# 





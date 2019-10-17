#!/bin/bash
#
#Ryan Kelly
#
#10/31/2018
#
#prob1
#
#This program counts for the number of Files and Directories in the total home dir

#LOCATION=/home/rck48/CS265/HW/TEST

FILECOUNT=$(find . -mindepth 1 -type f | wc -l)
DIRCOUNT=$(find . -mindepth 1 -type d | wc -l)

echo "Files $FILECOUNT"
echo "DIR's $DIRCOUNT"

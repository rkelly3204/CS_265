#!/bin/bash
#
#Ryan Kelly
#
#10/31/2018
#
#This program finds the largest thread in the home dir



find . -type f |rev |cut -d 'b' -f1 | rev | cut -d '_' -f1|sort| uniq -c | sort -n -r | awk '{$1=$1;print}'| head -n1 




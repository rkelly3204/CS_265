#!/bin/bash
#
#Ryan Kelly
#
#10/31/2018
#
# This program all the files sent at a certain time given by the command line arguments
#LOCATION=/home/rck48/CS265/HW/TEST

DATE=$2'/'$3'/'$1
grep -nr . -e "TimeStamp:"|grep $DATE|cut -d ":" -f1|rev|cut -d "/" -f1|rev

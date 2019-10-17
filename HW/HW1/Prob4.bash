#!/bin/bash
#
# Ryan Kelly
#
#10/31/2018
#
#This program finds the hostname of all the messages then sorts the total list and counts the number 
# of occurance of each hostname. 
#LOCATION=/home/rck48/CS265/HW

grep -nwr . -e "To:"|rev |cut -d "/" -f1 | rev|grep -o '@[^ ,]\+'|sed 's/^.\{1\}//'|sort|uniq -c|sort -n -r|awk '{printf("%s %s\n",$2,$1)}'

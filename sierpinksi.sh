#!/bin/bash

if [ $# -ne 1 ]; then
	echo "$0: usage: sierpinski recursions"
	exit 1
fi

re='^[0-9]+$'
if ! [[ $1 =~ $re ]] ; then
	echo "$0: usage: sierpinski recursions '$1' not numeric"
	exit 1
fi

recursions=$1
scale_to_a_third=.3333


echo	"*"
echo	"* Create a Recursive Sierpinski Carpet with ${recursions} Levels"
CMD="python generate_carpet.py ${recursions} > carpet_${recursions}.txt"
echo "*   ${CMD}"
eval "${CMD}"
#	echo	"*"
#	echo	"Create black and white svg file"
#	CMD="python lines_to_svg.py < nocolour.txt > carpet_${recursions}ST.svg"
#	echo "${CMD}"
#	eval "${CMD}"
echo	"*"
echo	"Create colour svg file"
CMD="python lines_to_svg_colour.py < carpet_${recursions}.txt > carpet_${recursions}.svg"
echo "*   ${CMD}"
eval "${CMD}"
echo	"*"
echo	"* Scale carpet lines down to fit in central third of canvas"
CMD="python rotate_scale_translate.py -f ${scale_to_a_third} < carpet_${recursions}.txt > carpet_${recursions}S.txt"
echo "*   ${CMD}"
eval "${CMD}"
echo	"*"
echo	"* Build some tile patterns from scaled file"
CMD="python transform_carpet.py < carpet_${recursions}S.txt > carpet_${recursions}ST.txt"
echo "${CMD}"
eval "${CMD}"
#	echo	"*"
#	echo	"Create black and white svg file"
#	CMD="python lines_to_svg.py < nocolour.txt > carpet_${recursions}ST.svg"
#	echo "${CMD}"
#	eval "${CMD}"
echo	"*"
echo "Create colour svg file"
CMD="python lines_to_svg_colour.py < carpet_${recursions}ST.txt > carpet_${recursions}ST.svg"
echo "*   ${CMD}"
eval "${CMD}"

exit 0

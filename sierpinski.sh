#!/bin/bash

if [[ $# -ne 3 ]]; then
	echo "$0: usage: sierpinski recursions patterns colour-theme"
	exit 1
fi

re='^[0-9]+$'

if ! [[ $1 =~ $re ]] ; then
	echo "$0: usage: sierpinski recursions '$1' not numeric"
	exit 1
fi
recursions=$1

if [[ $2 == carpet ]] ; then
	pattern=$2
elif [[ $2 == cross ]] ; then
	pattern=$2
elif [[ $2 == diagonal ]] ; then
	pattern=$2
elif [[ $2 == rotate ]] ; then
	pattern=$2
else 
	echo "$0: usage: sierpinski pattern '$2' not valid"
	exit 1
fi

if [[ $3 == light ]] ; then
	col_theme=$3
	background=Black
	background=MidnightBlue
elif [[ $3 == medium ]] ; then
	col_theme=$3
	background=LightGray
	background=WhiteSmoke
elif [[ $3 == dark ]] ; then
	col_theme=$3
	background=LightGoldenRodYellow
	background=BlanchedAlmond
	background=Azure
	background=Linen
else 
	echo "$0: usage: sierpinski colour theme '$3' not valid"
	exit 1
fi

scale_to_a_third=.3333

echo	"*"
echo	"* Create a Recursive Sierpinski Carpet with ${recursions} Levels"
CMD="python generate_carpet.py ${recursions} ${col_theme} > carpet_${recursions}.txt"
echo "${CMD}"
eval "${CMD}"
rc=$?; if [[ $rc != 0 ]]; then exit $rc; fi
echo	"*"
echo	"* Create colour svg file from base carpet"
CMD="python lines_to_svg_colour.py < carpet_${recursions}.txt > carpet_${recursions}.svg"
echo "${CMD}"
eval "${CMD}"
rc=$?; if [[ $rc != 0 ]]; then exit $rc; fi
echo "*"
echo	"* Change background colour in base carpet svg"
CMD="sed -i '' 's/none/${background}/g' carpet_${recursions}.svg"
echo "${CMD}"
eval "${CMD}"
rc=$?; if [[ $rc != 0 ]]; then exit $rc; fi
echo	"*"
echo	"* Scale carpet lines down to fit in central ninth of canvas"
CMD="python rotate_scale_translate.py -f ${scale_to_a_third} < carpet_${recursions}.txt > carpet_${recursions}S.txt"
echo "${CMD}"
eval "${CMD}"
rc=$?; if [[ $rc != 0 ]]; then exit $rc; fi
echo	"*"
echo	"* Build tile patterns from scaled file"
CMD="python transform_carpet.py ${pattern} < carpet_${recursions}S.txt > carpet_${recursions}ST.txt"
echo "${CMD}"
eval "${CMD}"
rc=$?; if [[ $rc != 0 ]]; then exit $rc; fi
echo	"*"
echo "*	Create colour svg file from tiled carpet"
CMD="python lines_to_svg_colour.py < carpet_${recursions}ST.txt > carpet_${recursions}ST.svg"
echo "${CMD}"
eval "${CMD}"
echo	"*"
echo	"* Change background colour in tiled carpet svg"
CMD="sed -i '' 's/none/${background}/g' carpet_${recursions}ST.svg"
echo "${CMD}"
eval "${CMD}"
rc=$?; if [[ $rc != 0 ]]; then exit $rc; fi
exit 0

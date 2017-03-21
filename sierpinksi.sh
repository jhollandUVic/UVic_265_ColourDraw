#!/bin/bash

recursions=2
scale_to_a_third=.3333

#	Create a Recursive Sierpinski Carpet
CMD="python generate_carpet.py ${recursions} > carpet_${recursions}.txt"
echo "${CMD}"
eval "${CMD}"

#	Create svg file
# CMD="python lines_to_svg_colour.py < carpet_${recursions}.txt > carpet_${recursions}.svg"
#	echo "${CMD}"
# eval "${CMD}"

#	Scale carpet lines down to fit in central third of canvas
CMD="python rotate_scale_translate.py -f ${scale_to_a_third} < carpet_${recursions}.txt > carpet_${recursions}S.txt"
echo "${CMD}"
eval "${CMD}"

# Build some tile patterns from scaled file
CMD="python transform_carpet.py < carpet_${recursions}S.txt > carpet_${recursions}ST.txt"
echo "${CMD}"
eval "${CMD}"

# Create svg file
#	CMD="python lines_to_svg_colour.py < carpet_${recursions}ST.txt > carpet_${recursions}ST.svg"
#	echo "${CMD}"
# eval "${CMD}"

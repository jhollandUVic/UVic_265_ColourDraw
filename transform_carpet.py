'''
source
	Modified from rings.py
purpose
	Read a file from stdin: a shape consisting of a list of lines.
	Write to stdout a variety of copies of a Sierpinski Carpet.
	Each carpet consists of the lines in the original carpet arranged
	in tiles, possibly rotated, around the origin.
preconditions
	stdin contains a legal line file with colour
'''

import sys
import copy
import math
import Line_Point

'''
purpose
	write to stdout a set of coloured tiles consisting of 8 copies of the
	original shape in lines, translated horizontally by delta_x,
	vertically by delta_y, rotated by rotation, and scaled to fit in space.
preconditions
	lines is a list with a sublist for each line containing the
	four line coordinates plus a colour
	n > 0
'''
def draw_tile(lines, delta_x, delta_y, rotation, scale):
	new_lines = copy.deepcopy(lines)

	for line in new_lines:
		# line is a list with the four line coordinates plus a colour
		point0 = Line_Point.Point(float(line[0]), float(line[1]))
		point1 = Line_Point.Point(float(line[2]), float(line[3]))
		line_object = Line_Point.Line(point0, point1)
		colour = str(line[4])
		
		# Apply transformations
		line_object.rotate(rotation)
		line_object.scale(scale)
		line_object.translate(delta_x, delta_y)
		
		print 'line', line_object, colour
		
		writeString = 'line ' + str(line_object) + '\n'
		f_nocolour.write( writeString )

'''
purpose
	convert the lines in stdin to a list containing, for each line,
	a sublist of line coordinates plus colour
	return the list
preconditions
	file_object is a reference to a readable file containing legal lines
'''
def load_line_file(file_object):
	line_objects = [ ]
	for line in file_object:
		# Convert text line to a list with line coordinates and colour
		line_object = line.split()
		this_line_list = [ float(line_object[1]), float(line_object[2]), \
		float(line_object[3]), float(line_object[4]), str(line_object[5]) ]
		line_objects.append(this_line_list)

	return line_objects

# ***** process command line arguments

# if len(sys.argv) != 2:
# 	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' number_of_rings'
# 	sys.exit(1)
# try:
# 	number_of_rings = int(sys.argv[1])
# except ValueError:
# 	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' number_of_rings'
# 	sys.exit(2)
# if number_of_rings < 1 or number_of_rings > 5:
# 	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' number_of_rings'
# 	sys.exit(3)
number_of_tiles = 9
angle = math.pi/4
#	Calc height of bounding box of rotated square then invert
#	for amount to scale down to fit in space.
scale = 1 / ( abs(math.sin(angle)) + abs(math.cos(angle)) )

L = load_line_file(sys.stdin)

f_nocolour = open('nocolour.txt', 'w')

# ***** generate the rings
# First tile is in middle, ie. original tile
# Second Tile is above the first
# The succeeding tiles are positioned counterclockwise around original
# delta-x and delta-y relative to origin: center of canvas.
tile_position = [
#	delta-x, delta-y, rotation, scale
#	Angle and Scale setting for "Up, Down, Across" rotated pattern
	[+0.0,		+0.0,	0.0, 1.0],
	[0.0,		+166.0,	angle, scale],
	[-166.0,	+166.0,	0.0, 1.0],
	[-166.0,	0.0,	angle, scale],
	[-166.0,	-166.0,	0.0, 1.0],
	[0.0,		-166.0,	angle, scale],
	[+166.0,	-166.0,	0.0, 1.0],
	[+166.0,	0.0,	angle, scale],
	[+166.0,	+166.0,	0.0, 1.0],
#
#	All Rotated Except for Center
# 	[+0.0,		+0.0,	0.0, 1.0],
# 	[0.0,		+166.0,	angle, scale],
# 	[-166.0,	+166.0,	angle, scale],
# 	[-166.0,	0.0,	angle, scale],
# 	[-166.0,	-166.0,	angle, scale],
# 	[0.0,		-166.0,	angle, scale],
# 	[+166.0,	-166.0,	angle, scale],
# 	[+166.0,	0.0,	angle, scale],
# 	[+166.0,	+166.0,	angle, scale],
#
#	Diagonally Rotated Except for Center
# 	[+0.0,		+0.0,	0.0, 1.0],
# 	[0.0,		+166.0,	0.0, 1.0],
# 	[-166.0,	+166.0,	angle, scale],
# 	[-166.0,	0.0,	0.0, 1.0],
# 	[-166.0,	-166.0,	angle, scale],
# 	[0.0,		-166.0,	0.0, 1.0],
# 	[+166.0,	-166.0,	angle, scale],
# 	[+166.0,	0.0,	0.0, 1.0],
# 	[+166.0,	+166.0,	angle, scale],
]
#	Draw a tile using tile_position which specifies delta-x, delta-y, scale factor, and angle of rotation.
for i in range(number_of_tiles):
	draw_tile(L, tile_position[i][0], tile_position[i][1], tile_position[i][2], tile_position[i][3])

f_nocolour.close

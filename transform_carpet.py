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
import Line_Point_colour

c_number_of_tiles = 9
c_angle = math.pi/4 # 45 degrees
cl_patterns = ['carpet', 'cross', 'diagonal', 'rotate']
#	Calc height of bounding box of rotated square then invert
#	for amount to scale down to fit in space.
c_scale = 1 / ( abs(math.sin(c_angle)) + abs(math.cos(c_angle)) )

'''
purpose
	write to stdout a set of coloured tiles consisting of 8 copies of the
	original shape in lines, translated horizontally by delta_x,
	vertically by delta_y, rotated by rotation, and scaled to fit in space.
preconditions
	lines is a list with a sublist for each line containing the
	four line coordinates plus a colour
'''
def draw_tile(lines, delta_x, delta_y, rotation, c_scale):
	new_lines = copy.deepcopy(lines)

	for line in new_lines:
		# line is a list with the four line coordinates plus a colour
		point0 = Line_Point_colour.Point(float(line[0]), float(line[1]))
		point1 = Line_Point_colour.Point(float(line[2]), float(line[3]))
		colour = str(line[4])
		line_object = Line_Point_colour.Line(point0, point1, colour)
		
		# Apply transformations
		line_object.rotate(rotation)
		line_object.scale(c_scale)
		line_object.translate(delta_x, delta_y)
		
		print 'line', line_object
		
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

if len(sys.argv) != 2:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' pattern required'
	sys.exit(1)
try:
	pattern = str(sys.argv[1])
except ValueError:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' pattern not string'
	sys.exit(2)
if pattern not in cl_patterns:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' pattern ' + sys.argv[1] + ' unknown'
	sys.exit(3)

l_lines = load_line_file(sys.stdin)

# ***** generate the tiles
# First tile is in middle, ie. original tile
# Second Tile is above the first
# The succeeding tiles are positioned counterclockwise around original
# delta-x and delta-y relative to origin: center of canvas.
#
if pattern == cl_patterns[0]:
#	No rotation or scale for complete carpet
	tile_position = [
	#	delta-x, delta-y, rotation, scale
		[+0.0,		+0.0,	0.0, 1.0],		# Center
		[0.0,		+166.0,	c_angle*4, 1.0],	# Upper Center
		[-166.0,	+166.0,	0.0, 1.0],		# Upper Left
		[-166.0,	0.0,	c_angle*4, 1.0],	# Middle Left
		[-166.0,	-166.0,	0.0, 1.0],		# Lower Left
		[0.0,		-166.0,	c_angle*4, 1.0],	# Lower Center
		[+166.0,	-166.0,	0.0, 1.0],		# Lower Right
		[+166.0,	0.0,	c_angle*4, 1.0],	# Middle Right
		[+166.0,	+166.0,	0.0, 1.0],		# Upper Right
	]
#	Angle and Scale setting for Cross: "Up, Down, Across" rotated pattern
if pattern == cl_patterns[1]:
	tile_position = [
	#	delta-x, delta-y, rotation, scale
		[+0.0,		+0.0,	0.0, 1.0], 			# Center
		[0.0,		+166.0,	c_angle, c_scale], 	# Upper Center
		[-166.0,	+166.0,	c_angle*4, 1.0], 	# Upper Left
		[-166.0,	0.0,	c_angle*3, c_scale],	# Middle Left
		[-166.0,	-166.0,	c_angle*4, 1.0],	# Lower Left
		[0.0,		-166.0,	c_angle*5, c_scale],	# Lower Center
		[+166.0,	-166.0,	c_angle*4, 1.0],	# Lower Right
		[+166.0,	0.0,	c_angle*7, c_scale],	# Middle Right
		[+166.0,	+166.0,	c_angle*4, 1.0],	# Upper Right
	]
#	Tiles on Diagonal Rotated
if pattern == cl_patterns[2]:
	tile_position = [
		[+0.0,		+0.0,	c_angle, c_scale],
		[0.0,		+166.0,	0.0, 1.0],
		[-166.0,	+166.0,	c_angle, c_scale],
		[-166.0,	0.0,	0.0, 1.0],
		[-166.0,	-166.0,	c_angle, c_scale],
		[0.0,		-166.0,	0.0, 1.0],
		[+166.0,	-166.0,	c_angle, c_scale],
		[+166.0,	0.0,	0.0, 1.0],
		[+166.0,	+166.0,	c_angle, c_scale],
	]
#	All Rotated Except for Center
if pattern == cl_patterns[3]:
	tile_position = [
		[+0.0,		+0.0,	0.0, 1.0],
		[0.0,		+166.0,	c_angle, c_scale],
		[-166.0,	+166.0,	c_angle*3, c_scale],
		[-166.0,	0.0,	c_angle*5, c_scale],
		[-166.0,	-166.0,	c_angle*7, c_scale],
		[0.0,		-166.0,	c_angle, c_scale],
		[+166.0,	-166.0,	c_angle*3, c_scale],
		[+166.0,	0.0,	c_angle*5, c_scale],
		[+166.0,	+166.0,	c_angle*7, c_scale],
	]
#	Draw tiles using tile_position which specifies delta-x, delta-y,
#	scale factor, and c_angle of rotation.
for i in range(c_number_of_tiles):
	draw_tile(l_lines, tile_position[i][0], tile_position[i][1],
				tile_position[i][2], tile_position[i][3])

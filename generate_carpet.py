import sys
import math
import Line_Point_colour
import random
import re

'''
purpose
	write to stdout a Sierpinski Carpet in a 500 x 500 canvas
	with arbitrary recursion level r
preconditions
	r is a positive integer
reference
	See <http://lodev.org/cgtutor/sierpinski.html>
'''
L_colour_themes = [ 'Dark', 'Light', 'Medium']

def drawRect(x1, y1, x2, y2, colour):
	# Draw boundaries of square
	point0 = Line_Point_colour.Point(x1, y1)
	point1 = Line_Point_colour.Point(x2,y1)
	line = Line_Point_colour.Line(point0, point1, colour)
	print 'line', line
	point0 = Line_Point_colour.Point(x2,y1)
	point1 = Line_Point_colour.Point(x2, y2)
	line = Line_Point_colour.Line(point0, point1, colour)
	print 'line', line
	point0 = Line_Point_colour.Point(x2, y2)
	point1 = Line_Point_colour.Point(x1, y2)
	line = Line_Point_colour.Line(point0, point1, colour)
	print 'line', line
	point0 = Line_Point_colour.Point(x1, y2)
	point1 = Line_Point_colour.Point(x1, y1)
	line = Line_Point_colour.Line(point0, point1, colour)
	print 'line', line
	# Draw cross on square
	point0 = Line_Point_colour.Point(x1, y2)
	point1 = Line_Point_colour.Point(x2, y1)
	line = Line_Point_colour.Line(point0, point1, colour)
	print 'line', line
	point0 = Line_Point_colour.Point(x1, y1)
	point1 = Line_Point_colour.Point(x2, y2)
	line = Line_Point_colour.Line(point0, point1, colour)
	print 'line', line
	
def drawCarpet(this_step, x1, y1, x2, y2, colour, prev_colour):
	# Determine new rectangle 1/3rd the size in center of given coordinates
	r_x1 = (2 * x1 + x2)/3.0
	r_y1 = (2 * y1 + y2)/3.0
	r_x2 = (x1 + 2 * x2)/3.0
	r_y2 = (y1 + 2 * y2)/3.0
	drawRect(r_x1, r_y1, r_x2, r_y2, colour)
	
	# Call drawCarpet another 8 times, once for each of the rectangles
	# around the one that was just drawn.
	if this_step > 0:
		next_step = this_step - 1
		while True:
			random.shuffle(L_colours)
			next_colour = L_colours[0]
			if next_colour != colour and next_colour != prev_colour:
				break
		drawCarpet(next_step, r_x1,   y1, r_x2, r_y1, next_colour, colour) # top center
		drawCarpet(next_step,   x1,   y1, r_x1, r_y1, next_colour, colour) # top left
		drawCarpet(next_step,   x1, r_y1, r_x1, r_y2, next_colour, colour) # center left
		drawCarpet(next_step,   x1, r_y2, r_x1,   y2, next_colour, colour) # bottom left
		drawCarpet(next_step, r_x1, r_y2, r_x2,   y2, next_colour, colour) # bottom center
		drawCarpet(next_step, r_x2, r_y2,   x2,   y2, next_colour, colour) # bottom right
		drawCarpet(next_step, r_x2, r_y1,   x2, r_y2, next_colour, colour) # center right
		drawCarpet(next_step, r_x2,   y1,   x2, r_y1, next_colour, colour) # top right
		
#	A mechanism to load lines of a file into a list
#	This is used to create a list of the 148 css colours supplied
def load_line_file(file_object):
	line_objects = [ ]
	for line in file_object:
		if line[-2:] == '\r\n': # Windows
			line = line[:-2] # strip carriage return and newline
		elif line[-1] == '\n': # Linux
			line = line[:-1] # strip newline
		line_object = line
		line_objects.append(line_object)

	return line_objects

# ********** process the command line arguments
if len(sys.argv) != 3:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' Supply recursion steps and colour choice'
	sys.exit(1)
try:
	recursion_steps = int(sys.argv[1])
except ValueError:
	print >> sys.stderr, 'Value Error: ' + sys.argv[0] + ' Supply recursion steps as integer'
	sys.exit(2)
if recursion_steps > 4:
	print >> sys.stderr, 'Values: ' + sys.argv[0] + ' Too many recursion steps'
	sys.exit(3)
	
try:
	colour_theme = str(sys.argv[2])
	colour_theme = colour_theme.capitalize()
except ValueError:
	print >> sys.stderr, 'Value Error: ' + sys.argv[0] + ' Supply colour theme as string'
	sys.exit(2)
if colour_theme not in L_colour_themes:
	print >> sys.stderr, 'Values: ' + sys.argv[0] + ' Supply colour theme from:',
	print >> sys.stderr, ",".join(map(str, L_colour_themes))
	sys.exit(3)
	
# Load valid css colours into list
fh_css_colours = open('css_colours.txt', 'r')
L_colours = load_line_file(fh_css_colours)
fh_css_colours.close

if colour_theme in L_colour_themes:
	L_colours = filter(lambda x: re.search(colour_theme, x), L_colours)
	random.shuffle(L_colours)
	this_colour = L_colours[0]
	prev_colour = L_colours[1]
			
# Dimensions chosen so side of carpet divisible by 3.
# Co-ordinates describe a square, upper left to bottom right.
drawCarpet(recursion_steps,-249, 249, 249, -249, this_colour, prev_colour )


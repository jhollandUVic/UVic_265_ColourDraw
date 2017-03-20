import sys
import math
import Line_Point

'''
purpose
	write to stdout a Sierpinski Carpet in a 500 x 500 canvas
	with arbitrary recursion level r
preconditions
	r is a positive integer
reference
	See <http://lodev.org/cgtutor/sierpinski.html>
'''
StepColour = ['Red', 'Blue', 'Green', 'Red', 'Orange', 'Lime', 'Maroon']
	
def drawRect(x1, y1, x2, y2, colour):
	# Draw boundaries of square
	point0 = Line_Point.Point(x1, y1)
	point1 = Line_Point.Point(x2,y1)
	line = Line_Point.Line(point0, point1)
	print 'line', line, colour
	point0 = Line_Point.Point(x2,y1)
	point1 = Line_Point.Point(x2, y2)
	line = Line_Point.Line(point0, point1)
	print 'line', line, colour
	point0 = Line_Point.Point(x2, y2)
	point1 = Line_Point.Point(x1, y2)
	line = Line_Point.Line(point0, point1)
	print 'line', line, colour
	point0 = Line_Point.Point(x1, y2)
	point1 = Line_Point.Point(x1, y1)
	line = Line_Point.Line(point0, point1)
	print 'line', line, colour
	# Draw cross on square
	point0 = Line_Point.Point(x1, y2)
	point1 = Line_Point.Point(x2, y1)
	line = Line_Point.Line(point0, point1)
	print 'line', line, colour
	point0 = Line_Point.Point(x1, y1)
	point1 = Line_Point.Point(x2, y2)
	line = Line_Point.Line(point0, point1)
	print 'line', line, colour
	
def drawCarpet(this_step, x1, y1, x2, y2, colour):
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
		colour = StepColour[next_step]
		drawCarpet(next_step,   x1,   y1, r_x1, r_y1, colour)
		drawCarpet(next_step, r_x1,   y1, r_x2, r_y1, colour)
		drawCarpet(next_step, r_x2,   y1,   x2, r_y1, colour)
		drawCarpet(next_step,   x1, r_y1, r_x1, r_y2, colour)
		drawCarpet(next_step, r_x2, r_y1,   x2, r_y2, colour)
		drawCarpet(next_step,   x1, r_y2, r_x1,   y2, colour)
		drawCarpet(next_step, r_x1, r_y2, r_x2,   y2, colour)
		drawCarpet(next_step, r_x2, r_y2,   x2,   y2, colour)

# ********** process the command line arguments
if len(sys.argv) != 2:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + 'recursion_steps'
	sys.exit(1)
try:
	recursion_steps = int(sys.argv[1])
except ValueError:
	print >> sys.stderr, 'Value Error: ' + sys.argv[0] + 'recursion_steps'
	sys.exit(2)
if recursion_steps >= 9:
	print >> sys.stderr, 'Values: ' + sys.argv[0] + 'recursion_steps'
	sys.exit(3)
# Dimensions chosen so side of carpet divisible by 3.
drawCarpet(recursion_steps,-249, 249, 249, -249, StepColour[recursion_steps])


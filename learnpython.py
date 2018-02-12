#!/anaconda/bin/python
"""
Table of Content:
000: Introduction
001: Python to run commands
002: Python and csv files
"""

"""
000: Intro **~**
Lets learn python quickly for admin usage
When I was first learning python it was hard to find any good methods to run
code for linux and it was often a messy way to interface another language with linux.

I will be using a mac with anaconda 2.7 and will eventually make a move to the 3.x as a means to rough out code
and eventually move it to a linux machine - I work from a mac.

I have no idea how any of this code will work on a windows environment but I would recommend looking
to powershell or vbscript as those are native and will give you the less headache - not saying that
python isnt supported. I just dont care/know how to run it on windows machines. I typically write for
both RHEL and debian machines much would assume if you are careful you could right for anything.
"""

# How to read a file!
textfile = "/Users/juehara/github/Python/test.txt"
with open(textfile) as obj_textfile:
	for row in obj_textfile:
		if row:
			print row
			# you can do more here
			
# How to print data/variables with .format!!
print "Here is a simple print function"
# We will set var1, set it as {0} inside the print function and declare it within the .format() function
var1 = "Oh hello mark!"
print "Crazy person: {0}" .format(var1)
# You can set a lot of vars with .format() as long as you declare them carefully with more numbers and inorder
var2 = "Where is LISA?!"
print "Crazy person: {0}\nCrazy person: {1}" .format(var1,var2)
# Since the format works with variables you can even do on the fly funtions inside it and even math
var3 = 256
var4 = 2
print "Some math: {0} * {1} = {2}" .format(var3,var4,var3*var4)

"""
001: Python to run commands **~**
So there are a few different ways to run native commands through python some work better than others. Typically you want to
have your command run and either store the output as a string in python or pass the command as a local file and read that
file with python. Reading a file is a bit more reliable but reading the pure TTY/STDIN-ERR-OUT.
"""
import subprocess
try:
	command = "uptime"
    # TIPS: If your command needs to use double Quotes *"* you will need to triple escape them in a very stupid way that typically will make grpahical syntax coloring mess up
	doublequotecommand = "gotta find it" # TODO its somewhere in my notes
    # TIPS: You can use arrows *> >>* and even pipes *|*
	output = subprocess.check_output(command, shell=True, stderr=subprocess.PIPE)
	print output
except subprocess.CalledProcessError as e:
	output = e.output

"""
002: Python and csv files
If you haven't worked with csv files they stand for Comma Seperated Values, and are used to create text based arrays that
can be used easily in python. You might think of a csv file as a configuration file. You could obviously read a text file
and serach it for certain files to set variables inside your script but thats pretty easy. I found myself using csv files to
create long configuration files that can be easily edited using a text editor like atom (shameless plug). Refer to 000: Python Intro
on how to read and parse a file quickly.

You want to always use a if statement to see if content exists first.
"""

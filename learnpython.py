#!/anaconda/bin/python
"""
Table of Content:
000: Introduction
001: Python to run commands
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
except subprocess.CalledProcessError as e:
	output = e.output

""" hello.py -- print a greeting message and exit.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */
"""

"""
The locale module opens access to the POSIX locale database and functionality. 
The POSIX locale mechanism allows programmers to deal with certain cultural 
issues in an application, without requiring the programmer to know all the 
specifics of each country where the software is executed.
"""
import locale

"""
The argparse module makes it easy to write user-friendly command-line 
interfaces. The program defines what arguments it requires, and argparse 
will figure out how to parse those out of sys.argv. The argparse module 
also automatically generates help and usage messages and issues errors 
when users give the program invalid arguments."""
import argparse
"""
This module provides a portable way of using operating system dependent 
functionality. If you just want to read or write a file see open(), 
if you want to manipulate paths, see the os.path module, and if you want 
to read all the lines in all the files on the command line see the 
fileinput module. For creating temporary files and directories see the 
tempfile module, and for high-level file and directory handling see 
the shutil module."""
import os

"""
The atexit module defines a single function to register cleanup
functions. Functions thus registered are automatically executed 
upon normal interpreter termination. atexit runs these functions in
the reverse order in which they were registered; if you register 
A, B, and C, at interpreter termination time they will be run in 
the order C, B, A.
"""
import atexit
"""
The gettext module provides internationalization (I18N) and localization
(L10N) services for your Python modules and applications. It supports 
both the GNU gettext message catalog API and a higher level, class-based 
API that may be more appropriate for Python files. The interface 
described below allows you to write your module and application messages 
in one natural language, and provide a catalog of translated messages 
for running under different natural languages.
"""
import gettext 
"""
This module provides access to some variables used or maintained by 
the interpreter and to functions that interact strongly with the 
interpreter. It is always available.
"""
import sys

from datetime import date

"save the system date"
COPYRIGHT_YEAR = date.today().year

"System output function"
def close_stdout(greeting_msg):
	open("retorno", "w").write("%s" % greeting_msg)

def main():
	
	lose = False
	# Default settings based on the user's environment.
	locale.setlocale(locale.LC_ALL, '')
	
	# locate the folder locations (with the correct structure)
	localedir = os.path.abspath(os.path.join(os.path.dirname(__file__), 
							'locales'))

	#Set the text message domain.
	gettext.bindtextdomain('hello', localedir)
	gettext.textdomain('hello')
	#bind the lookup function you want to use to the name _
	_ = gettext.gettext
	
	#Having initialized gettext, get the default message.
	greeting_msg = _("Hello, world!")

	"""
	This is implemented in C++ the Gnulib module "closeout".
	Python is not the implementation of the library, which should 
	perform the same
	"""
	atexit.register(close_stdout, greeting_msg)

	#Initialize the module
	parser = argparse.ArgumentParser()
	#We define the parameters for argparse
	parser.add_argument("-t", "--traditional", 
					help=_("-t, --traditional       use traditional greeting"),
					action="store_true")
	parser.add_argument("-g", "--greeting", 
					help=_("-g, --greeting=TEXT     use TEXT as the greeting message"),
					action="store")
	parser.add_argument("-v", "--version", 
					help=_("-v, --version       display version information and exit"),
					action="store_true")
	args = parser.parse_args()
	
	if args.traditional:
		greeting_msg = _("hello, world")
	elif args.greeting is not None:
		greeting_msg = args.greeting
	elif args.version:
		print_version(_)
		sys.exit()
	
	#Print greeting message and exit.
	print greeting_msg
	return greeting_msg
	sys.exit()

def print_version(_):
	"""It is important to separate the year from the rest of the message,
     as done here, to avoid having to retranslate the message when a new
     year comes around. """
	print _("Copyright (C) {} Free Software Foundation, Inc.\n\
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>\n\
This is free software: you are free to change and redistribute it.\n\
There is NO WARRANTY, to the extent permitted by law.".format(COPYRIGHT_YEAR).strip())


if __name__ == "__main__":
	main()

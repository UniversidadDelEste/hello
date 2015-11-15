#!/usr/bin/env python
#encoding:utf-8
''' pyhello.py -- print a greeting message and exit.
   Copyright 2015 Ing María Andrea Vignau <mavignau@gmail.com>
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  '''

import sys

import os
import codecs

import gettext
# Set up message catalog access
t = gettext.translation('pyhello', 'locale', fallback=True)
_ = t.ugettext
PACKAGE="pyHello"
VERSION="0.1"
PACKAGE_NAME=""

import argparse

def generate_version():
	'Generate the version string'
	out="%s (%s) %s\n"%(PACKAGE, PACKAGE_NAME, VERSION)
	out+=_(u"""
Copyright 2015 Ing María Andrea Vignau <mavignau@gmail.com>
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.""")
	return out + '\n'

def generate_help():
	'Generate the help string'
	out=[_("Usage: %s [OPTION]...\n") % sys.argv[0],
		_("Print a friendly, customizable greeting.\n"),
		"\n",
		_("  -t, --traditional       use traditional greeting\n"),
		_("  -g, --greeting=TEXT     use TEXT as the greeting message\n"),
		"\n",
		_("      --help     display this help and exit\n"),
		_("      --version  output version information and exit\n"), 
		"\n",
		_("General help using GNU software: <http://www.gnu.org/gethelp/>\n")]
	return u''.join(out)
	

def main(args_list,streams=None):
	'''main part. 
	args_list: list of command arguments, 
	streams: pair of file-like objects'''
	
	#redirect standard output and standard error, used on tests
	if streams: 
		sys.stdout = streams[0]
		sys.stderr = streams[1]
	
	#initialize argparse, invalidate option to create help string
	parser = argparse.ArgumentParser(add_help=False) 
	#boolean argument, store True on associated var
	parser.add_argument("-v", "--version", action="store_true")
	parser.add_argument("-t", "--traditional", action="store_true")
	parser.add_argument("-h", "--help", action="store_true")
	# accepts a string argument, type of it unicode utf-8
	parser.add_argument("-g", "--greeting", type=lambda s: unicode(s, 'utf8'))
	
	# creates the args object. When some error occurs, here is where pops
	args=parser.parse_args(args_list)

	if args.help:
		#generate &show help info
		sys.stdout.write(generate_help())
	elif args.version:
		#generate &show version info
		sys.stdout.write(generate_version())
	elif args.traditional:
		#show traditional form
		sys.stdout.write(_("hello, world")+"\n")
	elif args.greeting:
		#show greeting 
		sys.stdout.write(args.greeting+"\n")
	else:
		#default behavior, without arguments
		sys.stdout.write(_("Hello, world!")+"\n")


if __name__=='__main__':
	# reconfigure standard output to accept utf8
	sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
	#call main function
	main(sys.argv[1:])
	#exit from program
	sys.exit(0)

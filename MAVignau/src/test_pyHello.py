#!/usr/bin/env python
#encoding:utf-8
''' test_pyhello.py -- unit testing of pyhello program
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

from pyhello import *
import unittest

import StringIO
import gettext

#needed to compare translated strings correctly
t = gettext.translation('pyhello', 'locale', fallback=True)
_ = t.ugettext

class PyHelloTest(unittest.TestCase):
	'''Test cases to test different cases of pyHello
	'''
	def testSimple(self):
		'To test default without arguments'
		#create to redirect standard output & error
		out = [StringIO.StringIO(),StringIO.StringIO()] 
		main([],out)
		self.assertEqual(out[0].getvalue(),_("Hello, world!")+"\n")
		
	def testFail(self):
		'To test some erroneous arguments'
		out = [StringIO.StringIO(),StringIO.StringIO()]
		with self.assertRaises(SystemExit):
			main(['-i'],out)
		
	def testTraditional(self):
		'To test traditional greeting'
		out = [StringIO.StringIO(),StringIO.StringIO()]
		main(['-t'],out)
		self.assertEqual(out[0].getvalue(),_("hello, world")+"\n")
		
	def testCustom(self):
		'To test custom greeting message'
		out = [StringIO.StringIO(),StringIO.StringIO()]
		main(['-gbuenas tardes, profesor'],out)
		self.assertEqual(out[0].getvalue(),"buenas tardes, profesor\n")
		

		
if __name__ == '__main__':
	unittest.main()

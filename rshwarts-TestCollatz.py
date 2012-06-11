#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2011
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestCollatz.py > TestCollatz.py.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py > TestCollatz.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_eval_num

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

	def test_read1 (self) :
		r = StringIO.StringIO("1 10\n")
		a = [0, 0]
		b = collatz_read(r, a)
		self.assert_(b    == True)
		self.assert_(a[0] ==  1)
		self.assert_(a[1] == 10)
		
	def test_read2 (self) :
		r = StringIO.StringIO("1 1\n")
		a = [0, 0]
		b = collatz_read(r, a)
		self.assert_(b    == True)
		self.assert_(a[0] ==  1)
		self.assert_(a[1] == 1)

	def test_read3 (self) :
		r = StringIO.StringIO("2 1\n")
		a = [0, 0]
		b = collatz_read(r, a)
		self.assert_(b    == True)
		self.assert_(a[0] ==  2)
		self.assert_(a[1] == 1)
		
	def test_read4 (self) :
		r = StringIO.StringIO("")
		a = [0, 0]
		b = collatz_read(r, a)
		self.assert_(b    == False)

	def test_read5 (self) :
		r = StringIO.StringIO("1 10 51\n")
		a = [0, 0]
		b = collatz_read(r, a)
		self.assert_(b    == True)
		self.assert_(a[0] ==  1)
		self.assert_(a[1] == 10)
    # ----
    # eval
    # ----

	def test_eval_1 (self) :
		v = collatz_eval(1, 10)
		self.assert_(v == 20)

	def test_eval_2 (self) :
		v = collatz_eval(100, 200)
		self.assert_(v == 125)

	def test_eval_3 (self) :
		v = collatz_eval(201, 210)
		self.assert_(v == 89)

	def test_eval_4 (self) :
		v = collatz_eval(900, 1000)
		self.assert_(v == 174)
		
	def test_eval_5 (self) :
		v = collatz_eval(10, 1)
		self.assert_(v == 20)
		
	def test_eval_6 (self) :
		v = collatz_eval(1, 1)
		self.assert_(v == 1)
		
	def test_eval_7 (self) :
		v = collatz_eval(10, 10)
		self.assert_(v == 7)
		
	def test_eval_8 (self) :
		v = collatz_eval(200, 100)
		self.assert_(v == 125)
		

    # -----
    # print
    # -----

	def test_print1 (self) :
		w = StringIO.StringIO()
		collatz_print(w, 1, 10, 20)
		self.assert_(w.getvalue() == "1 10 20\n")

	def test_print2 (self) :
		w = StringIO.StringIO()
		collatz_print(w, 2, 1, 2)
		self.assert_(w.getvalue() == "2 1 2\n")
	def test_print3 (self) :
		w = StringIO.StringIO()
		collatz_print(w, 5, 5, 6)
		self.assert_(w.getvalue() == "5 5 6\n")
	def test_print4 (self) :
		w = StringIO.StringIO()
		collatz_print(w, 105150105, 15066406, 1230)
		self.assert_(w.getvalue() == "105150105 15066406 1230\n")

    # -----
    # solve
    # -----

	def test_solve1 (self) :
		r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
		w = StringIO.StringIO()
		collatz_solve(r, w)
		self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
	def test_solve2 (self) :
		r = StringIO.StringIO("1 1\n")
		w = StringIO.StringIO()
		collatz_solve(r, w)
		self.assert_(w.getvalue() == "1 1 1\n")
	def test_solve3 (self) :
		r = StringIO.StringIO("10 1\n200 100\n210 201\n1000 900\n")
		w = StringIO.StringIO()
		collatz_solve(r, w)
		self.assert_(w.getvalue() == "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")
	def test_solve4 (self) :
		r = StringIO.StringIO("5 5\n")
		w = StringIO.StringIO()
		collatz_solve(r, w)
		self.assert_(w.getvalue() == "5 5 6\n")
	
	#----
	# eval_num
	#
	
	def test_eval_num1 (self):
		cycle = collatz_eval_num(1)
		self.assert_(cycle==1)
	def test_eval_num2 (self):
		cycle = collatz_eval_num(5)
		self.assert_(cycle==6)
	def test_eval_num3 (self):
		cycle = collatz_eval_num(2)
		self.assert_(cycle==2)

		

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."

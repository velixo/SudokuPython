#!/usr/bin/python3

import unittest
# import src.incrementModule
from ..src import incrementModule

def fun(x):
	return x + 1


class MyTest(unittest.TestCase):
	def testNativeMethod(self):
		self.assertEqual(fun(3), 4)

	def testIncrementNumber(self):
		self.assertEqual(incrementModule.incrementNumber(3), 4)
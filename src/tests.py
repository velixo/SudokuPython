#!/usr/bin/python3

import unittest
from incrementModule import incrementNumber

def fun(x):
	return x + 1


class MyTest(unittest.TestCase):
	def testNativeMethod(self):
		self.assertEqual(fun(3), 4)

	def testIncrementNumber(self):
		self.assertEqual(incrementNumber(3), 4)

	def testIncorrectTest(self):
		self.assertEqual(incrementNumber(4), 5)


def main():
	unittest.main()

if __name__ == '__main__':
	main()
# -*- encoding: utf-8 -*-
import numpy
import sys
import numpy as np

def confidence(n1, n2, c, x1, x2, s1, s2):

	""" if n1 < 30 and n2 < 30, but n1+n2 >= 30

		[x1 - x2 - c x s \sqrt{1/n1+1/n2}, x1 - x2 - c x s \sqrt{1/n1+1/n2}]

		where s = \sqrt{((n1-1)s1^2 + (n2-1)s2^2) / (n1+n2-2)}
	"""

	sp1 = np.sqrt(((n1-1)*s1**2+(n2-1)*s2**2)/(n1+n2-2)) 
	sp2 = np.sqrt(1./n1 + 1./n2)
	a = x1 - x2 - c * sp1 * sp2 
	b = x1 - x2 + c * sp1 * sp2 

	return a,b
	

if __name__ == '__main__':

	if len(sys.argv) != 8:
		print("Usage: python confidence.py [n1] [n2] [c] [x1] [x2] [s1] [s2]")
		exit(0)

	n1 = int(sys.argv[1])
	n2 = int(sys.argv[2])
	c = float(sys.argv[3])
	x1 = float(sys.argv[4])
	x2 = float(sys.argv[5])
	s1 = float(sys.argv[6])
	s2 = float(sys.argv[7])
	a, b = confidence(n1, n2, c, x1, x2, s1, s2)
	print("[a,b]", a, b)
	print("hi")

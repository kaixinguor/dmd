import math
import sys

def C(n,m):
	return math.factorial(n)//(math.factorial(m)*math.factorial(n-m))

def probC(p, n, start, end):
	p_sum = 0
	for k in range(start,end+1):
		p_sum += C(n,k)*p**k*(1-p)**(n-k)

	return p_sum

if __name__ == '__main__':

	if len(sys.argv) != 5:
		print("Usage: python prob.py [p] [n] [start] [end]")
		exit(0)
	_, p, n, start, end = sys.argv
	p = float(p)
	n = int(n)
	start = int(start)
	end = int(end)
	prob = probC(p,n,start,end)
	print(prob)

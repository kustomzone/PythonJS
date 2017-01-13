'''
loop and add (integer)
'''

from time import time
from time import sleep
import threading

def main():
	if PYTHON=='PYTHONJS':
		pythonjs.configure( direct_operator='+' )
		pass

	start = time()
	n = 2000
	seq = []
	#cache = {0:True, 1:True, 2:True, 3:True}
	cache = []

	#w = worker(n,seq, cache)
	w1 = threading.start_webworker( worker, (0, n, seq, cache) )
	w2 = threading.start_webworker( worker, (10, n, seq, cache) )
	#w3 = threading.start_webworker( worker, (400, n, seq, cache) )
	sleep(1.0)

	testtime = time()-start
	primes_per_sec = len(seq) * (1.0 / testtime)

	#print('#%s' %len(seq))
	#seq.sort()  ## TODO fix sort for numbers
	print(primes_per_sec)
	print('#total test time: %s' %testtime)
	print('-----main exit')


with webworker:
	def worker(start, end, seq, cache):
		print('------enter worker------')
		for i in range(start, end):
			if i in cache:
				#continue  ## TODO - fix continue
				pass
			else:
				cache.append( i )
				if is_prime(i):
					seq.append( i )
		print('#worker reached: %s' %i)

	def is_prime(n):
		hits = 0
		for x in range(2, n):
			for y in range(2, n):
				if x*y == n:
					hits += 1
					if hits > 1:
						return False
		return True


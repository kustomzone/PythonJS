'''
map loop
'''

def main():
	a = {'x':100, 'y':200}
	b = ''
	c = 0
	for key,value in a:
		b += key
		c += value

	print( b )
	print( c )
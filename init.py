
#!/usr/bin/python

import sys
import subprocess as sbp

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print('Error!')
		sys.exit()
	
	dir_name = sys.argv[1]
	sbp.call(['mkdir', dir_name])

	for i in range(6):
		sbp.call(['touch', '{}/{}.py'.format(dir_name, chr(ord('a')+i))])

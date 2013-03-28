#!/usr/bin/python
#used to copy from one dist to another
import re
import os
import sys
import shutil

def copier(source,dest):
	if os.path.exists(source)==False:
		print 'incorrect source'
		sys.exit(1)

	dest_path=os.path.abspath(dest)
	if os.path.exists(dest_path)==False:
		print 'creating folder'
		os.mkdir(dest_path)
	print 'going to copy'
	shutil.copy(source,dest)
	print 'copied from: '+source+' to '+dest

def main():
	args=sys.argv[1:]
	if len(args)==0:
		print 'usage: ./copier.py source dest'
		sys.exit(1)
	source=args[0]
	dest=args[1]
	
	copier(source,dest)
if __name__=='__main__':
	main()
	

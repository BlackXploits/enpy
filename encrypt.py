#!/usr/bin/env python
# Encrypt your file here!
# Author: BlackXploits

import hashlib
import sys
import os

w  = '\033[0m'
g  = '\033[32m'
r  = '\033[31m'
b  = '\033[34m'

os.system('clear')

class Encrypt():
	def __init__(self, filepath, encrypt='MD5', chunksize=64):
		if not encrypt in hashlib.algorithms:
			raise ValueError(r+'type encrypt not supported')
		self.encrypt = encrypt

		if not os.path.isfile(filepath):
			raise ValueError(r+'file does not exist')
		self.fp = filepath

		self.chunksize = 64

	def hashFile(self):
		self.Encrypt = hashlib.new(self.encrypt)
		with open(self.fp, 'rb') as file:
			while 1:
				data = file.read(self.chunksize)
				self.Encrypt.update(data)
				if len(data) < self.chunksize:
					break
		return self.Encrypt.hexdigest()

if __name__ == '__main__':
	import argparse
	print(b+"""
		8888888888          8888888b.           
		888                 888   Y88b          
		888                 888    888          
		8888888    88888b.  888   d88P 888  888 
		888        888 "88b 8888888P"  888  888 
		888        888  888 888        888  888 
		888        888  888 888        Y88b 888 
		8888888888 888  888 888         "Y88888 
		                                    888 
		                               Y8b d88P 
		                                "Y88P"
	"""+w)
	parser = argparse.ArgumentParser(description='File Encrypt')
	parser.add_argument('-f', '--file', help='Path to file', action='store', dest='file', default=False)
	parser.add_argument('-e', help='Type to encrypt your file (must be supported by your hashlib version)', action='store', dest='encrypt', default='MD5')
	parser.add_argument('--chunksize', help='Chunk size', action='store', dest='cs', default='64')
	parser.add_argument('--list', help='List supported hash types', action='store_true', dest='list', default=False)
	args = parser.parse_args()
	if (len(sys.argv)==1) or ('--help' in sys.argv or '-h' in sys.argv):
		parser.print_help()
		sys.exit(0)
	else:
		pass
	if not args.file and not args.list:
		parser.error('No filepath given')
	else:
		pass
	try:
		chunksize = int(args.cs)
	except ValueError:
		parser.error('Invalid chunksize given')
	if args.list:
		print 'Listing supported hash types: \n'
		for i in hashlib.algorithms:
			print i.upper()
		sys.exit(0)
	try:
		print ('[*] Encrypting Files... '),;sys.stdout.flush()
		Encrypt = Encrypt(args.file, encrypt=args.encrypt.lower())
		hash = Encrypt.hashFile()
		print (g+'[DONE]')
		print ('[*]'+w+' %s'+w+' Hash: '+g+'%s') %(args.encrypt.upper(), hash)
	except ValueError, e:
		if 'file does not exist' in e:
			parser.error(r+'File does not exist')
		elif 'encrypt not supported' in e:
			parser.error(r+'Hash type not supported')

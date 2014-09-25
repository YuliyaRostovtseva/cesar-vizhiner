#!/usr/bin/python
# -*- coding: UTF-8 -*-

# КМЗИ. ЛР№1. Шифр Цезаря
def getArgs():
	import argparse
	parser = argparse.ArgumentParser(prog = "cesvizh")
	parser.add_argument ('cesar_vizhiner', choices=['c', 'v'], help = "cesar or vizhiner")
	parser.add_argument ('infile', type = argparse.FileType(mode='rb'), help = "input file")
	parser.add_argument ('key', help = "crypt key (string or number)")
	parser.add_argument ('outfile', type = argparse.FileType(mode='wb'), help = "output file")
	parser.add_argument ('crypt_decrypt', choices=['c', 'd'], help = "crypt or decrypt")
 	return parser.parse_args()

def main():	
	args = getArgs()

	if (args.cesar_vizhiner == 'c'): # Цезарь
		if (args.crypt_decrypt == 'c'):
			args.outfile.write(''.join([chr ((ord(c) + int(args.key)) % 256) for c in args.infile.read()]))
		else:
			args.outfile.write(''.join([chr ((ord(c) - int(args.key)) % 256) for c in args.infile.read()]))
	
	else: # Вижинер
		if (args.crypt_decrypt == 'c'):
			args.outfile.write(''.join([chr ((ord(c) + int(args.key[args.infile.tell() % len(args.key)]) ) % 256) for c in args.infile.read()]))
		else:
			args.outfile.write(''.join([chr ((ord(c) - int(args.key[args.infile.tell() % len(args.key)]) ) % 256) for c in args.infile.read()]))

if __name__ == "__main__":
	main()
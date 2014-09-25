#!/usr/bin/python
# -*- coding: UTF-8 -*-

# КМЗИ. ЛР№1. Шифр Цезаря и Вижинера
def getArgs():
	import argparse
	parser = argparse.ArgumentParser(prog = "cesvizh")
	parser.add_argument ('cesar_vizhiner', choices=['c', 'v'], help = "cesar or vizhiner")
	parser.add_argument ('infile', type = argparse.FileType(mode='rb'), help = "input file")
	parser.add_argument ('key', help = "crypt key (string or number)")
	parser.add_argument ('outfile', type = argparse.FileType(mode='wb'), help = "output file")
	parser.add_argument ('crypt_decrypt', choices=['c', 'd'], help = "crypt or decrypt")
 	return parser.parse_args()
	
def cesCrypt(infile, key):
	return [chr ((ord(c) + int(key)) % 256) for c in infile.read()]
	
def cesDecrypt(infile, key):
	return [chr ((ord(c) - int(key)) % 256) for c in infile.read()]
	
def vizhCrypt(infile, key):
	return [chr ((ord(c) + ord(key[infile.tell() % len(key)]) ) % 256) for c in infile.read()]
	
def vizhDecrypt(infile, key):
	return [chr ((ord(c) - ord(key[infile.tell() % len(key)]) ) % 256) for c in infile.read()]
	

def main():	
	args = getArgs()
	res = 0

	if (args.cesar_vizhiner == 'c'): # Цезарь
		if (args.crypt_decrypt == 'c'):
			res = cesCrypt(args.infile, args.key)
		else:
			res = cesDecrypt(args.infile, args.key)
	
	else: # Вижинер
		if (args.crypt_decrypt == 'c'):
			res = vizhCrypt(args.infile, args.key)
		else:
			res = vizhDecrypt(args.infile, args.key)
			
	args.outfile.write(''.join(res))

if __name__ == "__main__":
	main()
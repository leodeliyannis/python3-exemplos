# -*- coding: utf-8 -*-
from sys import stdin 

def isPrime(N):
	if N < 2: 
		return False
	i = 2
	while i*i <= N:
		if N%i == 0:
			return False
		i += 1
	return True

for line in stdin:
	N = int(line)
	if not isPrime(N):
		print('Nada')
	else:
		super = True
		for c in line:
			if c == '\n': break
			if not isPrime(ord(c) - ord('0')):
				super = False
				break
		print('Super' if super else 'Primo')

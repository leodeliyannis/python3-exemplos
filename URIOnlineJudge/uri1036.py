# -*- coding: utf-8 -*-
# URI 2674 - Fase
from math import sqrt

l = input().split()

a, b, c = float(l[0]), float(l[1]), float(l[2])

# print("%.1f %.1f %.1f" % (a, b, c))

delta = b*b - 4.0 * a * c

if (a == 0.0) or (delta < 0.0):
	print('Impossivel calcular')
else:
	R1 = (-b + sqrt(delta)) / (2.0 * a)
	R2 = (-b - sqrt(delta)) / (2.0 * a)
	print('R1 = %.5f' % R1)
	print('R2 = %.5f' % R2)
	
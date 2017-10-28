# -*- coding: utf-8 -*-
# URI 2663 - Fase

N = int(input())
K = int(input())

v = []
for i in range(0, N):
	v.append(int(input()))
	
# v = sorted(v, reverse=True)
v.sort(reverse=True)

while K < len(v) and v[K-1] == v[K]:
	K += 1
	
print(K)


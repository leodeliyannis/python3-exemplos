# -*- coding: utf-8 -*-
# URI 2670 - Máquina de Café

v = []

for i in range(0, 3):
	v.append(int(input()))

print(min(v[0]*2 + v[2]*2,
          v[0]*4 + v[1]*2,
		  v[1]*2 + v[2]*4))

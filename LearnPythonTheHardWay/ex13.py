# Recebendo parâmetros da linha de comando
# exemplo: python3 ex13.py <primeiro> <segundo> <terceiro>

from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

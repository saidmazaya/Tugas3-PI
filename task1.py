"""
Nama : Said Muhammad Mazaya
NIM : 221402129

Soal 1 = Write a program that reads in integer numbers from a text file named indata.txt in the same directory as the executing program.
"""

import os

file_path = os.path.join(os.path.dirname(__file__), 'indata.txt')

with open(file_path, 'r') as file:
    data = file.readlines()
    
data = [int(x) for x in data] 

sum_data = sum(data)

print(f'{sum_data:.2f}')
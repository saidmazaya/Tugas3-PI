"""
Nama : Said Muhammad Mazaya
NIM : 221402129

Soal 2 = Write a class that calculates and stores the height and weight of a person in metric. The file should be named lab.py.  
"""

class BMI:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        
    def BMI_Value(self):
        return self.weight / (self.height ** 2)
    
    def __eq__(self, other):
        return self.weight == other.weight and self.height == other.height
    
bmi1 = BMI(80, 1.8)
bmi2 = BMI(75, 1.87)
bmi3 = BMI(80, 1.8)
print(bmi1 == bmi2)
print(bmi1 == bmi3)
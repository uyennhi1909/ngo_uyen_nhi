# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 16:30:13 2024

@author: UNHI
"""

# Nhập hai số a, b.
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))

# Tính toán biểu thức
if (pow(a,1/3)-pow(b,1/3))**2 != 0 : 
    B = ( (a+b)/(pow(a,1/3)+pow(b,1/3)) - pow(a*b,1/3) ) / (pow(a,1/3)-pow(b,1/3))**2
    print(f"Kết quả biểu thức là {B:.2f}")
else:
    print("Không thể tính giá trị biểu thức vì mẫu số bằng 0")
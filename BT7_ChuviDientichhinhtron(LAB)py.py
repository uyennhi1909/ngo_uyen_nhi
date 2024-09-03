# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 21:58:45 2024

@author: UNHI
"""
import math

# Nhập vào bán kính của hình tròn

r = float(input("Nhập vào bán kính của hình tròn: "))

if r>0 : 
    # Tính chu vi của hình tròn
    print("Chu vi của hình tròn là: ", round(2*r*math.pi,1))
    # Tính diện tích của hình tròn
    print(" Diện tích của hình tròn là: ", round(pow(r,2)*math.pi,1))
else:
    print("Lỗi ! Vui lòng nhập lại bán kính")


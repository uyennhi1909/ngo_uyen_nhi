# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 22:20:20 2024

@author: UNHI
"""

# Viết chương trình tính số đo kiểm tra sức khỏe BMI

kg = float(input("Nhập số đo cân nặng của bạn (kg): "))
m = float(input("Nhập số đo chiều cao của bạn (m): "))

if kg>0 and m>0:
    print(" Vậy chỉ số BMI của bạn là: ", round(kg/pow(m,2),2))
else:
    print(" Vui lòng nhập lại số đo hợp lệ ")
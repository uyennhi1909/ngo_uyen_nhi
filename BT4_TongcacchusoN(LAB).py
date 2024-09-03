# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:37:17 2024

@author: UNHI
"""

# Viết chương trình cho phép nhập vào số nguyên dương N có 2 chữ số. 

N = int(input("Nhập số nguyên dương N có 2 chữ số: "))

# Xuất ra màn hình tổng các chữ số của N. Ví dụ: Nhập N=48, kết quả xuất ra màn hình là 4 + 8 = 12 

if N >= 10 and N <= 99:
    hangchuc =  N // 10
    donvi = N % 10
    print(f"{hangchuc} + {donvi} = ", hangchuc + donvi )
else: 
    print("Vui lòng nhập lại số nguyên dương có 2 chữ số !")
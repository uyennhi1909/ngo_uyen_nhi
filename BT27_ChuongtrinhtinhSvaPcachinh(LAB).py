# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 16:51:15 2024

@author: UNHI
"""

# Viết chương trình tính diện tích và chu vi các hình: hình vuông (v), hình chữ nhật (n) và hình tròn (t) với những thông tin được nhập từ bàn phím. 

import math

hinh = input("Nhập hình: ").lower()

# Hình chữ nhật
if hinh == "n":
    print("Tính P và S của hình chữ nhật")
    r = float(input("Nhập chiều rộng = "))
    d = float(input("Nhập chiều dài = "))
    P = (r+d)*2
    S = r*d
    

# Hình vuông
elif hinh == "v":
    print("Tính P và S của hình vuông")
    c = float(input("Nhập độ dài cạnh = "))
    P = c*4
    S = c**2
    print(f"\tKết quả P = {P:.2f}\tS = {S:.2f}")

# Hình tròn
elif hinh == "t":
    print("Tính P và S của hình tròn")
    r = float(input("Nhập vào bán kính hình tròn = "))
    P = 2*r*math.pi
    S = r**2*math.pi
    print(f"\tKết quả P = {P:.2f}\tS = {S:.2f}")
else:
    print("Vui lòng nhập đúng hình dạng 'n','v','t'")
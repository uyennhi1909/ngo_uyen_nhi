# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:37:07 2024

@author: UNHI
"""

# Nhập vào 4 số nguyên a,b,c,d
a = int(input("Nhập vào số nguyên thứ nhất: "))
b = int(input("Nhập vào số nguyên thứ hai: "))
c = int(input("Nhập vào số nguyên thứ ba: "))
d = int(input("Nhập vào số nguyên thứ tư: "))

#  In ra màn hình số có giá trị nhỏ nhất (không dùng hàm min)
if a<b:
    min = a
else:
    min = b
if c < min:
    min = c
if d < min:
    min = d
print("Vậy số có giá trị nhỏ nhất là: ",min)
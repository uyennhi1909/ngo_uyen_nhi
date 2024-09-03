# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:02:53 2024

@author: UNHI

"""

# Nhập vào 3 số a, b, c từ bàn phím.

a = int(input("Nhập vào số nguyên thứ nhất: "))
b = int(input("Nhập vào số nguyên thứ hai: "))
c = int(input("Nhập vào số nguyên thứ ba: "))

#  In ra màn hình số có giá trị lớn nhất (không dùng hàm hỗ trợ).
if a>b:
    max = a
else:
    max = b
if c > max:
    max = c
print("Vậy số có giá trị lớn nhất là: ",max)
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:47:31 2024

@author: UNHI
"""

# Cho 1 ký tự chữ thường. In ra ký tự chữ hoa tương ứng

T = input("Nhập một ký tự chữ thường: ")

if len(T) == 1 and T.islower() and T.isalpha():
    print("Ký tự chữ hoa tương ứng là: ",T.upper())
else:
    print("Vui lòng nhập lại theo đúng yêu cầu")
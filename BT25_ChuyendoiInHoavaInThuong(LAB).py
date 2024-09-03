# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:33:22 2024

@author: UNHI
"""

# Nhập 1 chữ cái, nếu là chữ thường thì đổi thành chữ hoa, ngược lại đổi thành chữ thường.
T = input("Nhập một chữ cái: ")

if len(T) == 1 and T.isalpha():
    if T.isupper():
        print("Chữ thường tương ứng là: ",T.lower())
    if T.islower():
        print("Chữ hoa tương ứng là: ",T.upper())
else:
    print("Vui lòng nhập lại theo đúng yêu cầu")
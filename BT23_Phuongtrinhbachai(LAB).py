# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:19:31 2024

@author: UNHI
"""

#  Giải và biện luận phương trình bậc hai: ax2 + bx + c = 0
a = float(input("Nhập số thực a: "))
b = float(input("Nhập số thực b: "))
c = float(input("Nhập số thực c: "))
delta = (b**2-4*a*c)

if delta == 0 :
    n = -b/(2*a)
    print(f"Vậy phương trình có nghiệm kép là: {n:.2f}")
elif delta > 0:
    n1 = (-b + delta**0.5)/(2*a)
    n2 = (-b - delta**0.5)/(2*a) 
    print(f"Vậy phương trình có 2 nghiệm phân biệt là: {n1:.2f} và {n2:.2f}")
else:
    print("Vậy phương trình vô nghiệm") 
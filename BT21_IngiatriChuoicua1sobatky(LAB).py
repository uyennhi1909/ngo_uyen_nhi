# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:07:57 2024

@author: UNHI
"""

# Nhập 1 số bất kỳ.

i = int(input("Nhập vào một số nguyên bất kỳ từ 0 đến 9: "))

# Hãy in giá trị (chuỗi) của số nguyên đó nếu nó có giá trị từ 0 đến 9, ngược lại thông báo không đọc được.
chuoi = ['Không','Một', 'Hai', 'Ba', 'Bốn', 'Năm', 'Sáu', 'Bảy', 'Tám', 'Chín']
if 0 <= i <= 9:
    print(chuoi[i])
else:
    print("Không đọc được")
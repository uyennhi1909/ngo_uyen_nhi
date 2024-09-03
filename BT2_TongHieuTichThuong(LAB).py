# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:28:24 2024

@author: UNHI
"""

# Viết chương trình nhập vào 2 số nguyên a, b. 

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

# Tính tổng, hiệu, tích, thương của 2 số trên và in kết quả ra màn hình. 
# Kết quả phép chia làm tròn 2, 3 chữ số sau dấu chấm (ví dụ kết quả 3.333333 thì làm tròn 3.333). 

thuong = a/b
print("Tổng của 2 số trên là: ", a + b )
print("Hiệu của 2 số trên là: ", a - b )
print("Tích của 2 số trên là: ", a * b )
print(f"Thương của 2 số trên là: {thuong:.2f}")
print("Chia lấy dư của 2 số trên là: ", a % b ) 
print("Chia lấy nguyên của 2 số trên là: ", a // b ) 
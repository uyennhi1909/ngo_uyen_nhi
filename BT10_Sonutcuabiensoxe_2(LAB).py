# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 22:34:14 2024

@author: UNHI
"""

# Cho số xe (gồm 4 chữ số) của bạn. Cho biết số xe của bạn được mấy nút? 

xe = input("Nhập số xe gồm 4 số: ")

if int(xe) > 999 and int(xe) <= 9999:
    tong = int(xe[0]) + int(xe[1]) + int(xe[2]) + int(xe[3]) 
    print(f"Số xe {xe} của bạn được",tong % 10, "nút" )
else: 
    print("Vui lòng hãy nhập lại đúng số xe của bạn !")
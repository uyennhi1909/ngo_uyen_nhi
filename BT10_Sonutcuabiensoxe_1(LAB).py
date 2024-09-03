# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:19:02 2024

@author: UNHI
"""
# Cho số xe (gồm 4 chữ số) của bạn. Cho biết số xe của bạn được mấy nút?
xe = int(input("Nhập số xe gồm 4 số: "))

if xe > 999 and xe <= 9999:
    nhat = xe // 1000
    nhi = xe // 100 - nhat*10
    ba = xe // 10 - nhat*100 - nhi*10
    tu = xe % 10 
    tong = nhat + nhi +  ba + tu
    print(f"Số xe {xe} của bạn được",tong%10,"nút" )
else: 
    print("Vui lòng hãy nhập lại đúng số xe của bạn !")
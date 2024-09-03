# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:46:21 2024

@author: UNHI
"""

# Viết chương trình cho phép nhập vào giờ, phút và giây theo định dạng hh:mm:ss. Hãy đổi ra giây và in kết quả ra màn hình.

time = input("Nhập vào giờ, phút và giây theo định dạng hh:mm:ss nhé: ")
if ":" in time:
    gio, phut, giay = map(int, time.split(":")) 
    if 0 <= gio < 24 and 0 <= phut < 60 and 0 <= giay < 60  :
        print("Tổng số giây là: ", gio*3600 + phut*60 + giay, "s")
    else:
        print("Thời gian không hợp lệ. Vui lòng nhập lại")
else:
    print("Định dạng giờ phút giây không hợp lệ. Vui lòng nhập lại đúng định dạng")
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:28:19 2024

@author: UNHI
"""

#  Nhập vào giờ, phút, giây. 
gio = int(input("Nhập giờ: "))
phut = int(input("Nhập phút: "))
giay = int(input("Nhập giây: "))

# Kiểm tra xem giờ, phút, giây đó có hợp lệ hay không? In kết quả ra màn hình
if 0 <= gio < 24 and 0 <= phut < 60 and 0 <= giay < 60:
    print("Bây giờ là:", gio ,"giờ", phut ,"phút", giay ,"giây")
else:
    print("Vui lòng nhập lại thòi gian hợp lệ !")
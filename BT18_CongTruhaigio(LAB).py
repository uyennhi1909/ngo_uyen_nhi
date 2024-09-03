# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:34:39 2024

@author: UNHI
"""

# Viết chương trình cho 2 giờ (giờ, phút, giây) và thực hiện cộng, trừ 2 giờ này. 
h1 = int(input("Nhập vào thời gian thứ nhất\n\tGiờ: "))
p1 = int(input("\tPhút: "))
s1 = int(input("\tGiây: "))

h2 = int(input("Nhập vào thời gian thứ hai\n\tGiờ: "))
p2 = int(input("\tPhút: "))
s2 = int(input("\tGiây: "))

if ( 0 <= h1 < 24 and 0 <= p1 < 60 and 0 <= s1 < 60
    and 0 <= h2 < 24 and 0 <= p2 < 60 and 0 <= s2 < 60):
    giay1 = h1 * 3600 + p1 * 60 + s1
    giay2 = h2 * 3600 + p2 * 60 + s2

    tonggiay = giay1 + giay2
    giotong = tonggiay // 3600
    tonggiay = tonggiay % 3600
    phuttong = tonggiay // 60
    giaytong = tonggiay % 60
    print("Tổng hai giờ này là: ",giotong,"giờ",phuttong,"phút",giaytong,"giây")

    if giay1 < giay2:
        giay1, giay2  = giay2, giay1
    hieugiay = giay1 - giay2
    giohieu = hieugiay // 3600
    hieugiay = hieugiay % 3600
    phuthieu = hieugiay // 60
    giayhieu = hieugiay % 60
    print("Hiệu hai giờ này là: ",giohieu,"giờ",phuthieu,"phút",giayhieu,"giây")
else:
    print("Vui lòng nhập lại thời gian hợp lệ !")





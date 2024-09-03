# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 12:29:19 2024

@author: UNHI
"""

#  Viết chương trình đổi từ giờ/phút/giây thành giây. Ví dụ, nhập 1h8p8s thì in ra 4088 giây

time = input("Nhập vàp thời gian theo mẫu (ví dụ: 1h8p8s): ")

try:
    h = p = s = 0
    if "h" in time:
        h, time = time.split("h")
    if "p" in time:
        p, time = time.split("p")
    if "s" in time:
        s = time.split("s")[0]
except ValueError:
    print("Vui lòng nhập lại thời gian đúng theo mẫu !")
else:
    h, p, s = map(int,[h, p, s])
    if 0 <= h < 24 and 0 <= p < 60 and 0 <= s < 60:
        tong = h*3600 + p*60 + s
        print(f"Vậy thời gian quy đổi ra giây là: {tong}s")
    else: 
        print("Vui lòng nhập lại đúng thời gian")


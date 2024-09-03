# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 12:29:25 2024

@author: UNHI
"""

# Cho số xe (gồm 4 chữ số) của bạn. Cho biết số xe của bạn được mấy nút?

xe = input("Nhập số xe gồm 4 số: ") 
if len(xe) == 4 :
    so = map(int,list(xe)) 
    print(f"Số xe {xe} của bạn được",sum(so)%10,"nút" ) 
else:
   print("Vui lòng hãy nhập lại đúng số xe của bạn !")

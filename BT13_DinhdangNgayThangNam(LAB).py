# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:43:19 2024

@author: UNHI
"""

# Nhập lần lượt ngày, tháng, năm sinh. Sau đó xuất ra theo định dạng sau rồi làm ngược lại: 

d = int(input("Nhập ngày sinh của bạn: "))
m = int(input("Nhập tháng sinh của bạn: "))
y = int(input("Nhập năm sinh của bạn: "))

# Gần giống bài kiểm tra ngày tháng năm hợp lệ (file: buoi2_ngaythangnam.py)
if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
    namnhuan = True
else:
    namnhuan = False
ngaytrongthang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if namnhuan: 
    ngaytrongthang[1] = 29 

if (0 < d <= ngaytrongthang[m-1]) and ( 0 < m <= 12) and y > 0: 

# a) Ngày/tháng/năm (Nhập 20 8 1990 thì xuất 20/8/1990) 
    print("\n\ta) dd/mm/yyyy: ")
    a = f"{d}/{m}/{y}"
    print("Bạn sinh vào ",a)

    # Làm ngược lại
    da, ma, ya = map(int, a.split("/"))
    print(f"Ngày {da} \nTháng {ma} \nNăm {ya}")

# b) Ngày/tháng/năm (Nhập 20 8 1990 thì xuất 20/8/90) 
    print("\n\tb) dd/mm/yy: ")
    y1 = y % 100
    b = f"{d}/{m}/{y1:02}"
    print("Bạn sinh vào ",b)

    # Làm ngược lại
    db, mb, yb = map(int, b.split("/"))
    if 00 <= yb <= 25: 
        print(f"Ngày {db} \nTháng {mb} \nNăm", yb + 2000)
    else:
        print(f"Ngày {db} \nTháng {mb} \nNăm", yb + 1900)

# c) Năm/tháng/ngày (Nhập 20 8 1990 thì xuất 1990/8/20) 
    print("\n\tc) yyyy/mm/dd: ")
    c = f"{y}/{m}/{d}"
    print("Bạn sinh vào ",c)

    # Làm ngược lại
    yc, mc, dc = map(int, c.split("/"))
    print(f"Ngày {dc} \nTháng {mc} \nNăm {yc}")

else:
    print("Ngày tháng năm không tồn tại. Vui lòng nhập lại ngày tháng năm hợp lệ")












# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 16:04:54 2024

@author: UNHI
"""

# (a) Cho ba số a, b, c được nhập vào từ bàn phím.
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))

# Hãy in ra màn hình theo thứ tự tăng dần các số (Chỉ dùng 1 biến phụ).
if a > b:
    bien = a
    a = b
    b = bien
if a > c:
    bien = a
    a = c
    c = bien
if b > c:
    bien = b
    b = c
    c = bien
print("Các số theo thứ tự tăng dần là: ", a, b, c)

# (b) Nhập vào 1 số nguyên N sau đó in ra số có các con số theo thứ tự tăng dần. Ví dụ: nhập số 6879 thì in ra số 6789
N = input("\nNhập một số nguyên: ")

if N.isdigit():
    ds = list(N)
    ds.sort()
    xep = "".join(ds)
    print(xep)
else:
    print("Vui lòng nhập lại một số nguyên")
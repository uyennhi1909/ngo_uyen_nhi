# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 15:09:02 2024

@author: UNHI 
"""

#  Viết chương trình nhập vào năm sinh, in ra tuổi. Ví dụ nhập 1988 in ra (giả sử năm hiện tại là 2023): Ban sinh nam 1988 vay ban 35 tuoi.

nam = int(input("Nhập năm sinh của bạn: "))
if nam < 2022 or nam > 0:
    print(f"Bạn sinh năm {nam} vậy tuổi của bạn là", 2022 - nam)
else:
    print("Năm sinh không đúng. Vui lòng nhập lại !")
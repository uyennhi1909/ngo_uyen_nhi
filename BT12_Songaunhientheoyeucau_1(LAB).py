# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 12:55:16 2024

@author: UNHI

"""
import random 

#  Xuất ra một số (nguyên, thực) ngẫu nhiên theo yêu cầu
so = random.choices([True, False],k=4)
# a) 0 đến 100
if so[0]: 
   a = round(random.uniform(0, 100),2)
else:
   a = random.randint(0,100)
print(f"Số ngẫu nhiên từ 0 đến 100 là: {a}")

# b) 50 đến 99 
if so[1]: 
   b = round(random.uniform(50, 99),2)
else:
   b = random.randint(50, 99)
print(f"Số ngẫu nhiên từ 50 đến 99 là: {b}")


# c) -39 đến 79 
if so[2]: 
   c = round(random.uniform(-39, 79),2)
else:
   c = random.randint(-39, 79)

print(f"Số ngẫu nhiên từ -39 đến 79 là: {c}")

# d) -79 đến -39
if so[3]: 
   d = round(random.uniform(-79, -39),2)
else:
   d = random.randint(-79, -39)
print(f"Số ngẫu nhiên từ -79 đến -39 là: {d}")

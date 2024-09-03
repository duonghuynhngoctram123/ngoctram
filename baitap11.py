# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 01:08:31 2024

@author: Administrator
"""

char_lower=input("Nhap mot ky tu thuong:")
if len(char_lower)==1 and char_lower.islower():
    char_upper=char_lower.upper()
    print("Ky tu chu ho tuong ung la:")
else:
    print("Nhap mot ki tu chu thuong khac.")
        


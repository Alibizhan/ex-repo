# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 23:07:38 2019

@author: Fianchetto
"""

'''file = open("Deep_Learning.txt","r")
print(file.read())
file.close()
print(file.closed)'''

import pandas as pd
xls = pd.read_excel(r"sinav_programi.xlsx")
df = pd.DataFrame(xls,columns=["I. ÖĞRETİM ","I.SINIF","II.SINIF","III.SINIF","4.SINIF"])
print(df.head(4))

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def bSort(listT) :
    for cnt in range (0, len(listT) - 1):
        for cnt2 in range(0, len(listT) - 1 - cnt):
            if listT[cnt2] > listT[cnt2+1]:
                listT[cnt2], listT[cnt2+1] = listT[cnt2+1], listT[cnt2]
    return listT


listT = []

i = int(input("Enter the length of the list: "))

for j in range(0, i):
    eInt = int(input())
    listT.append(eInt)

print (bSort(listT))
print (bSort(listT)[::-1])
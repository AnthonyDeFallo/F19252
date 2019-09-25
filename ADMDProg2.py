# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 12:35:40 2019

@author: teke
"""

class Employee:
    _fname = ""
    _lname = ""
    _addr = ""
    _ein = 0
    _dob = ""
    _hdte = ""
    

    def __init__(self, fname, lname, addr, ein, dob, hdte):
        self._fname = fname
        self._lname = lname
        self._addr = addr
        self._ein = ein
        self._dob = dob
        self._hdte = hdte
        
        print("First Name:",self._fname)
        print("Last Name",self._lname)
        print("Address:",self._addr)
        print("ID:",self._ein)
        print("Birth:",self._dob)
        print("Hired:",self._hdte,"\n")
        
        
    def __next__(self):
        self.EmployeeList = []

def main ():
    EmployeeList = [
            Employee("Anthony", "DeFallo", "99 ff", "2566555", "11/05/98", "2/2/02"),
            Employee("A", "DeFallo", "9f", "25455442", "11/05/98", "2/2/02"),
            Employee("Your", "Mom", "99 ff", "2566555", "11/05/98", "2/2/02"),
            Employee("A", "DeFallo", "9f", "25455442", "11/05/98", "2/2/02")
            ]
    


if __name__== "__main__":
  main()    
        
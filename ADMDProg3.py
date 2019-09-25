# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 13:03:33 2019

@author: teke
"""
"""
 --------------------------ADMDAccount-----------------------------
 | + __init(self,int,int)                                         |
 | + deposit(self,int)                                            |
 | + getOwner(self)                                               |
 | + getAccountNumber(self)                                       |
 | + close(self)                                                  |
 ------------------------------------------------------------------
  """

class ADMDAccount(object):

    
    def __init__(self,bal,acctstatus):
        self.acctstatus = acctstatus
        self.bal = bal
            
    def deposit(self,num=0):
        if self.acctstatus == 1:
                self.bal = self.bal + num
                print ('New Balance after $', num, 'deposit is $', self.bal)
                
        else:
                print('Failed. Account closed')
                
    def getOwner(self):
        print ('Owner:',self.name)
    
    def getAccountNumber(self):
        print ('Account Number:',self.accnm)
    
    def close(self):
        self.acctstatus = 0
        print('Account Successfully Closed')

"""
 --------------------------ADMDChecking----------------------------
 | + __init__(self, string, string, int, int)                     |
 | + withdraw(self, int)                                          |
 ------------------------------------------------------------------
  """

class ADMDChecking(ADMDAccount):
    def __init__(self, name, accnm, bal=0, cfee=0):
        super().__init__(bal,1)
        self.name = name
        self.bal = bal
        "self.accnm = random.randint(123456789,999999999)"
        self.accnm = accnm
        self.cfee = cfee
        print('Checking Account Created')
        
    def withdraw(self,num=0):
        if num < self.bal:
                if self.acctstatus == 1:
                    self.bal = self.bal - num - self.cfee
                    print ('$', self.bal, 'is your new balance')
                else:
                    print('Failed. Account closed')
        else:
            print('not enough funds')  
    
"""
 --------------------------ADMDPerson------------------------------
 | + __init__(self, string, string, int, int)                     |
 | + withdraw(self, int)                                          |
 ------------------------------------------------------------------
  """    
    

class ADMDPerson(ADMDAccount):
    def __init__(self, name, accnm, bal=0):
        super().__init__(bal,1)
        self.name = name
        self.bal = bal
        "self.accnm = random.randint(123456789,999999999)"
        self.accnm = accnm
        print('Personal Account Created')
        
    def withdraw(self,num=0):
        if num < self.bal:
                if self.acctstatus == 1:
                    self.bal = self.bal - num
                    print ('$', self.bal, 'is your new balance')
                else:
                    print('Failed. Account closed')
        else:
            print('not enough funds')

"""
 --------------------------ADMDBusiness----------------------------
 | + __init__(self, string, int, string, string, int)             |
 | + withdraw(self, int)                                          |
 | + getInfo(self)                                                |
 ------------------------------------------------------------------
  """
    
class ADMDBusiness(ADMDAccount):
    def __init__(self, name, accnm, addr, btype, bal=0):
        super().__init__(bal,1)
        self.name = name
        self.bal = bal
        "self.accnm = random.randint(123456789,999999999)"
        self.accnm = accnm
        self.addr = addr
        self.btype = btype
        print('Business Account Created')
        
    def getInfo(self):
        print ('Owner:',self.name, 'Address:', self.addr, 'Type:', self.btype)
        
    def withdraw(self,num=0):
        if num < self.bal:
                if self.acctstatus == 1:
                    self.bal = self.bal - num
                    print ('$', self.bal, 'is your new balance')
                else:
                    print('Failed. Account closed')
        else:
            print('not enough funds')
    
"""
 --------------------------ADMDSavings-----------------------------
 | + __init__(self, string, string, int, int)                     |
 | + withdraw(self, int)                                          |
 ------------------------------------------------------------------
  """    

class ADMDSavings(ADMDAccount):
    def __init__(self, name, accnm, bal=0, wfee=0):
        super().__init__(bal,1)
        self.name = name
        self.bal = bal
        "self.accnm = random.randint(123456789,999999999)"
        self.accnm = accnm
        self.wfee = wfee
        print('Savings Account Created')
        
    def withdraw(self,num=0):
        if num < self.bal:
                if self.acctstatus == 1:
                    self.bal = self.bal - num
                    print ('$', self.bal, 'is your new balance')
                else:
                    print('Failed. Account closed')
        else:
            print('not enough funds')

"""
 --------------------------ADMDChecking----------------------------
 | + __init__(self, string, string, int, int)                     |
 | + withdraw(self, int)                                          |
 ------------------------------------------------------------------
  """    
    
class ADMDTrust(ADMDSavings):
    def __init__(self, name, accnm, bal=0, irate=0, age=0):
        super().__init__(bal,1)
        self.name = name
        self.bal = bal
        "self.accnm = random.randint(123456789,999999999)"
        self.accnm = accnm
        self.irate = irate
        self.age = age
        print('Trust Account Created')
        
    def withdraw(self,num=0):
        if num < self.bal:
                if self.acctstatus == 1:
                    if self.age >= 21:
                        self.bal = self.bal - num
                        print ('$', self.bal, 'is your new balance')
                    else:
                        print('FAILED: Too young to withdraw')
                else:
                    print('Failed. Account closed')
        else:
            print('not enough funds')
    

"Main function"
"""
 ------------------------------main--------------------------------
 | + ADMDChecking(name, acctnum, bal,cfee)                        |
 | + ADMDPerson(name, acctnum, bal)                               |
 | + ADMDBusiness(name, acctnum, addr, btype, bal)                 |
 | + ADMDSavings(name, acctnum, bal, wfee)                        |
 | + ADMDTrust(name, acctnum, bal, wfee, age)                     |
 ------------------------------------------------------------------
  """
def main():
    checking = ADMDChecking('Anthony DeFallo', 2848327, 3843,2)
    checking.deposit(100)
    checking.withdraw(100)
    checking.getOwner()
    checking.getAccountNumber()
    checking.close()
    checking.withdraw(100)
    print('\n')
    personal = ADMDPerson('Anthony DeFallo', 2848327, 3843)
    personal.deposit(100)
    personal.withdraw(100)
    personal.getOwner()
    personal.getAccountNumber()
    personal.close()
    personal.withdraw(100)
    print('\n')
    business = ADMDBusiness('Tekenology', 28473345, '2401 Alexander', 'Technology', 38457)
    business.deposit(3455)
    business.withdraw(100)
    business.getInfo()
    business.getAccountNumber()
    business.close()
    business.withdraw(100)
    print('\n')
    savings = ADMDSavings('Anthony DeFallo', 2847374, 453821, 2.75)
    savings.deposit(342)
    savings.withdraw(223)
    savings.getOwner()
    savings.getAccountNumber()
    savings.close()
    savings.withdraw(33)
    print('\n')
    trust1 = ADMDTrust('Anthony DeFallo', 1123234, 583722, 10.95, 21)
    trust1.deposit(384)
    trust1.withdraw(223)
    trust1.getOwner()
    trust1.getAccountNumber()
    trust1.close()
    trust1.withdraw(200)
    print('\n')
    trust1 = ADMDTrust('NOTAnthony DeFallo', 1123234, 583722, 10.95, 18)
    trust1.deposit(384)
    trust1.withdraw(223)
    trust1.getOwner()
    trust1.getAccountNumber()
    trust1.close()
    trust1.withdraw(200)
    
    
"Run the main function"   
if __name__== "__main__":
  main()  
  
  
  
  
  
  
  
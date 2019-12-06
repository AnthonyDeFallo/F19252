# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:12:47 2019

@author: teke
"""

class cake:
    
    def c_recipe(self, nev1):
         r_dt = {'nev' : "dobostorta", 'liszt' : (18, 'dkg'), 'tojas' : 9, 
           'cukor' : (20, 'dkg'), 'vaj' :  (5 , 'dkg')}    
         r_ks = {'nev' : "kalacs", 'tej' : (3, 'dl'), 'liszt' : (5, 'dkg'), 
          'tojas' : 1, 'cukor' :(10, 'dkg'), 'vaj' : (1, 'dkg')}
         r_la = {'nev' : "liszerestorta", 'viz' : (1, 'kanal'), 'liszt' : (20, 'dkg'),'tojas sargaja' : 0, 
          'cukor' : (10, 'dkg'), 'vaj' : (5, 'dkg')}

         db = {'kalacs' : r_ks, 'liszerestorta' :r_la, 'dobostorta' : r_dt}

         w = list(db[nev1].items())
  
         return w
     
        
    def e_recipe(self, nev1):
         r_dt = {'name' : "dobostorta", 'flour' : (18, 'dkg'), 'egg' : 9, 
           'sugar' : (20, 'dkg'), 'butter' :  (5 , 'dkg')}    
         r_ks = {'name' : "kalacs", 'tej' : (3, 'dl'), 'flour' : (5, 'dkg'), 
          'egg' : 1, 'sugar' :(10, 'dkg'), 'butter' : (1, 'dkg')}
         r_la = {'name' : "liszerestorta", 'water' : (1, 'kanal'), 'flour' : (20, 'dkg'),'egg yolk' : 0, 
          'sugar' : (10, 'dkg'), 'butter' : (5, 'dkg')}

         db = {'kalacs' : r_ks, 'liszerestorta' :r_la, 'dobostorta' : r_dt}

         w = list(db[nev1].items())
  
         return w
    
 
def main():
     a = cake()
     dolog = input('Enter the pastry name: ')
     if dolog == 'liszerestorta':
        print(a.e_recipe(dolog))
     elif dolog == 'kalacs':
        print(a.e_recipe(dolog))
     elif dolog == 'dobostorta':
        print(a.e_recipe(dolog))
            
     else:
        print('INCORRECT INPUT')
     
main()      
        
        
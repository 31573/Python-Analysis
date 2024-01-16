# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 13:52:31 2024

@author: Elsie
"""


import statistics
import csv

with open("Resources\\budget_data.csv", "r") as f:
    reader = csv.reader(f)

# skip header row  
    next(reader)
    
    total = 0
    months = 0    
    pre_pl = 0
    total_ch = 0
    max_inc = 0
    max_dec = 0
   
    for row in reader:
        months += 1
        
        p_l = int(row[1])
        total += p_l
          
      #Average Change
        ch = p_l - pre_pl
        if pre_pl == 0:
            ch = 0
            
        total_ch += ch
        
        #Greatest Increase
        if ch > max_inc:
            max_inc = ch
            max_inc_month = row[0]
            
         #Greatest Decrease
        if ch < max_dec:
            max_dec = ch
            max_dec_month = row[0]
       
        
        pre_pl = p_l
        
        
                
output = f'''
Financial Analysis
------------------------------------------------------------
Total Months: {months}
Total: $ {total:,}   
Average Change: $ {total_ch/(months-1):.2f}
Greatest Increase in Profits: {max_inc_month} (${max_inc:,})
Greatest Decrease in Profits: {max_dec_month} (${max_dec:,})
'''  
print (output)
open('Analysis/Budget_Analysis.txt','w').write(output)
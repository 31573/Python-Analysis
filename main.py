# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 13:52:31 2024

@author: Elsie
"""


# To import csv file
import csv
# to open file with file path
with open("Resources\\budget_data.csv", "r") as f:
    reader = csv.reader(f)

# skip header row  
    next(reader)
    
# To set variables  
    total = 0
    months = 0    
    pre_pl = 0
    total_ch = 0
    max_inc = 0
    max_dec = 0
    
# To set up loop   
    for row in reader:
        months += 1
        
# To loop and sum the profit & Loss        
        p_l = int(row[1])
        total += p_l

# to calculate the monthly variance          
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
       
# to reset the p_l     
        pre_pl = p_l
        
        
 # use f string template and display the results               
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
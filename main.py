
# to import csv
import csv

# to open the csv file with file path
with open("C:\\Users\\Elsie\\Desktop\\Classwork\\Python\\Module 3\\election_data.csv", "r") as f:
    reader = csv.reader(f)
# skip header row   
    next(reader)
 
    # to set the variables
    total = 0    
    candidates = {}

# to set loop
    for row in reader:
        total += 1
        candidate = row[2]
   
        #to create conditional 
        if candidate not in candidates.keys():
            candidates[candidate] = 0
        
        candidates[candidate] += 1
 
# to create f string template and print results    
output = f'''
-------------------------
Total Votes: {total:,}
-------------------------    
'''

# set winner varianle
winner = [0,'']

#Set loop and print the ouput
for candidate in candidates.keys():
    votes = candidates[candidate]
    output += f"{candidate}: {votes/total * 100:.3f}% ({votes:,})\n"
 
    #set conditional
    if votes > winner[0]:
        winner[0] = votes
        winner[1] = candidate

# print winner
output += f'-------------------------\nWinner: {winner[1]}\n-------------------------'
print(output)

# print report
my_report = open('Analysis/Election_Report.txt','w')
my_report.write(output)

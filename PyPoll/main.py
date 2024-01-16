

import csv

with open("C:\\Users\\Elsie\\Desktop\\Classwork\\Python\\Module 3\\election_data.csv", "r") as f:
    reader = csv.reader(f)
# skip header row   
    next(reader)
   
    total = 0    
    candidates = {}

    for row in reader:
        total += 1
        candidate = row[2]
     
        if candidate not in candidates.keys():
            candidates[candidate] = 0
        
        candidates[candidate] += 1
    
output = f'''
-------------------------
Total Votes: {total:,}
-------------------------    
'''

winner = [0,'']

for candidate in candidates.keys():
    votes = candidates[candidate]
    output += f"{candidate}: {votes/total * 100:.3f}% ({votes:,})\n"
    
    if votes > winner[0]:
        winner[0] = votes
        winner[1] = candidate

output += f'-------------------------\nWinner: {winner[1]}\n-------------------------'
print(output)

my_report = open('Analysis/Election_Report.txt','w')
my_report.write(output)

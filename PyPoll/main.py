#import csv and operating system libraries
import csv
import os

#locating specific csv file and storing it in a constant
CSV_PATH = os.path.join("resources", "election_data.csv")

#set the current working directory to the folder of the csv file
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#initialize the variable vote_count to 0
vote_count = 0 

#initialize the variable for candidate name and set to empty string
candidate_name = ""

#initialize a dictionary to hold candidate names and vote counts
candidate_dict = {}

#initialize a variable for winning candidate

winner = ""

#initialize a variable for maximum votes 

max_votes = 0

# open the CSV using the UTF-8 encoding
with open(CSV_PATH, encoding='UTF-8') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")

 # read the header row and set the csv reader to the next row 
   csv_header = next(csvreader)

#set loop that goes through each row in csvreader
   for row in csvreader:
      #add 1 to counter as it loops through the file
      vote_count += 1   
      if candidate_name != row[2]:
         candidate_name = row[2]
         if candidate_name not in candidate_dict.keys():
# a dictionary to hold candidate names and votes 
            candidate_dict[candidate_name] = 0
      candidate_dict.update({candidate_name: candidate_dict[candidate_name] + 1})

for candidate, votes in candidate_dict.items():
   print(candidate, "received ", votes, "votes.")

   if votes > max_votes:
      max_votes = votes
      winner = candidate
   
#print title to terminal
print("Election Results")
print("------------------")
#print final monthcount to terminal
print(f'Total Votes: {vote_count}')
for candidate, votes in candidate_dict.items():
   print(candidate,":", "{:.2%}".format(votes/vote_count), "(",votes, ")" )
print("Winner:", winner)
print("------------------")


#  Open the output file
f = open("analysis/pypoll_text.txt", "w")
    # Write the header row
f.write("Election Results\n")
f.write("------------------\n")
f.write(f'Total Votes: {vote_count}\n')
for candidate, votes in candidate_dict.items():
   f.write(candidate + ": "+ "{:.2%}".format(votes/vote_count)+ " ("+str(votes)+ ")\n")
f.write("Winner: " + winner + '\n')
f.write("------------------\n")


f.close()

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

#initialize a list to hold every unique candidate name
candidates = []

# open the CSV using the UTF-8 encoding
with open(CSV_PATH, encoding='UTF-8') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")

 # read the header row and set the csv reader to the next row 
   csv_header = next(csvreader)
   print(f"CSV Header: {csv_header}")

#set loop that goes through each row in csvreader
   for row in csvreader:
#add 1 to counter as it loops through the file
      vote_count += 1      
      if candidate_name != row[2]:
         candidate_name = row[2] 
         if candidate_name not in candidates:
            candidates.append(candidate_name)
         
print(candidates)

         

   

#1. read the file (existing loop) and save the names of the candidates (list or dict)
#   - declare a variable for the current name and set to empty string.
#   - when the candidate name changes in the file, make that the current name and save it.
#   - print the result
  




#print title to terminal
print("Election Results")
print("------------------")
#print final monthcount to terminal
print(f'Total Votes: {vote_count}')
print("------------------")



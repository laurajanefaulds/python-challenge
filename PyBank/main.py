#import csv and operating system libraries
import csv
import os

#locating specific csv file and storing it in a constant
CSV_PATH = os.path.join("resources", "budget_data.csv")

#set the current working directory to the folder of the csv file
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# open the CSV using the UTF-8 encoding
with open(CSV_PATH, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

 # read the header row and set the csv reader to the next row 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#initialize the variable monthcount to 0
    month_count = 0

#Initialize variable for profit_loss_total to 0
    profit_loss_total = 0

#Declare a boolean for first row 
    first_row = True

#Initialize  variable for previous_profit
    previous_profit = 0

#Initialize variable for current_profit: 
    current_profit = 0

#Initialize variable for profit_change: 
    profit_change = 0

#Initialize variable for total_change: 
    total_change = 0

#set loop that goes through each row in csvreader
    for row in csvreader:
#add 1 to counter as it loops through the file
        month_count += 1
#set the current_profit to the value in the current row
        current_profit = int(row[1])
#add current profit to profit total 
        profit_loss_total = profit_loss_total + current_profit
#check if the current row is the first row 
        if first_row == True:
            first_row = False
#after the first row, calculate profit_change and add to total_change
        else: 
            profit_change = current_profit - previous_profit
            total_change += profit_change
#saving current_profit as previous_profit for next loop 
        previous_profit = current_profit   

#print title to terminal
print("Financial Analysis")
print("------------------")
#print final monthcount to terminal
print(f'Total Months: {month_count}')
print(f'Total: ${profit_loss_total}')
print(f'Average Change: ${round(total_change/(month_count - 1),2)}')
 
        



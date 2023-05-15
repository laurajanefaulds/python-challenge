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

#Initialize variable for greatest_increase:
    greatest_increase = 0

#Initialize variable for greatest_decrease:
    greatest_decrease = 0

#Initialize variable for month of greatest increase and decrease:
    increase_month = ''
    decrease_month = ''

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
            if profit_change > greatest_increase:
                greatest_increase = profit_change
                increase_month = row[0]
            if profit_change < greatest_decrease:
                greatest_decrease = profit_change
                decrease_month = row[0]

#saving current_profit as previous_profit for next loop 
        previous_profit = current_profit



#calculate average change
average_change = round(total_change/(month_count - 1),2)

#print title to terminal
print("Financial Analysis")
print("------------------")
#print final monthcount to terminal
print(f'Total Months: {month_count}')
print(f'Total: ${profit_loss_total}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {increase_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})')
        


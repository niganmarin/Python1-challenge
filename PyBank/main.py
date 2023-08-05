import csv
import os

# Define the file path
file_path = os.path.join("Resources", "budget_data.csv")

# Initialize variables
totalmonths = 0
PnL = []
Dates = []

# Open and read the CSV file
with open(file_path) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    header = next(csvreader)

    # Read and process each row in the CSV
    for row in csvreader:
        totalmonths += 1
        Dates.append(row[0])
        PnL.append(int(row[1]))

# Calculate the net total amount of "Profit/Losses"
total_pnl = sum(PnL)

# Calculate the changes in "Profit/Losses" over the entire period
avg_changes = []
for i in range(1, len(PnL)):
    avg_changes.append(PnL[i] - PnL[i - 1])

# Calculate the average change
avg_change = sum(avg_changes) / len(avg_changes)

# Find the greatest increase and decrease in profits
greatest_increase = max(avg_changes)
greatest_increase_index = avg_changes.index(greatest_increase) + 1  
greatest_increase_date = Dates[greatest_increase_index]

greatest_decrease = min(avg_changes)
greatest_decrease_index = avg_changes.index(greatest_decrease) + 1  
greatest_decrease_date = Dates[greatest_decrease_index]

# Print the results
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {totalmonths}")
print(f"Total: ${total_pnl}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

import csv

# File path to your CSV file
file_path = r"C:\Users\board\python-challenge\PyBank\Resources\budget_data.csv"

# Initialize variables
months = []
profit_losses = []
changes = []
total_profit_losses = 0

# Read the CSV file
with open(file_path, mode='r') as file:
    csvreader = csv.reader(file)
    next(csvreader)  # Skip the header row

    # Read the first row to initialize previous value for changes calculation
    first_row = next(csvreader)
    months.append(first_row[0])
    profit_losses.append(int(first_row[1]))
    previous_profit_losses = int(first_row[1])
    
    # Loop through each row in the CSV file
    for row in csvreader:
        # Append months and profit/losses
        months.append(row[0])
        profit_losses.append(int(row[1]))
        
        # Calculate total profit/losses
        total_profit_losses += int(row[1])
        
        # Calculate the change from the previous month and store in changes list
        change = int(row[1]) - previous_profit_losses
        changes.append(change)
        previous_profit_losses = int(row[1])

# Calculate the total number of months
total_months = len(months)

# Calculate the net total of profit/losses
net_total_profit_losses = sum(profit_losses)

# Calculate the average of changes
average_change = sum(changes) / len(changes)

# Find the greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_decrease = min(changes)

# Get the corresponding dates for the greatest increase and decrease
greatest_increase_date = months[changes.index(greatest_increase) + 1]
greatest_decrease_date = months[changes.index(greatest_decrease) + 1]

# Generate the analysis summary as a formatted string
analysis = (
    "Financial Analysis\n"
    "-------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total_profit_losses}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"
)

# Print the analysis to the terminal
print(analysis)

# Export the analysis to a text file
output_file_path = r"C:\Users\board\python-challenge\PyBank\analysis\financial_analysis.txt"
with open(output_file_path, mode='w') as output_file:
    output_file.write(analysis)



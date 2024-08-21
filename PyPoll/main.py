import csv

# File path to your CSV file
file_path = r"C:\Users\board\python-challenge\PyPoll\Resources\election_data.csv"

# Initialize variables
total_votes = 0
candidate_votes = {}

# Read the CSV file
with open(file_path, mode='r') as file:
    csvreader = csv.reader(file)
    next(csvreader)  # Skip the header row
    
    # Loop through each row in the CSV file
    for row in csvreader:
        # Increment total votes
        total_votes += 1
        
        # Get the candidate's name from the row
        candidate_name = row[2]
        
        # If the candidate is not in the dictionary, add them
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0
        
        # Increment the vote count for that candidate
        candidate_votes[candidate_name] += 1

# Prepare the analysis summary
results = []
results.append("Election Results")
results.append("-------------------------")
results.append(f"Total Votes: {total_votes}")
results.append("-------------------------")

# Determine the winner by the popular vote and calculate percentages
winner = None
max_votes = 0

for candidate, votes in candidate_votes.items():
    # Calculate the percentage of votes the candidate won
    vote_percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {vote_percentage:.3f}% ({votes})")
    
    # Determine the winner based on popular vote
    if votes > max_votes:
        max_votes = votes
        winner = candidate

results.append("-------------------------")
results.append(f"Winner: {winner}")
results.append("-------------------------")

# Print the results to the terminal
for line in results:
    print(line)

# Export the results to a text file
output_file_path = r"C:\Users\board\python-challenge\PyPoll\analysis\Election_Results.txt"
with open(output_file_path, mode='w') as output_file:
    for line in results:
        output_file.write(line + "\n")


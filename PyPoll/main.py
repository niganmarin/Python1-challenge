import csv 
import os

# Define file path
filepath = os.path.join("Resources", "election_data.csv")

# Initialize variables
ID = []
Candidates = []

# Read file
with open(filepath) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    header = next(csvreader)

    # Extract data
    for row in csvreader:
        ID.append(row[0])
        Candidates.append(row[2])

# Find total number of votes
total_votes = len(ID)

# Create a dictionary to store candidate vote counts
candidate_votes = {}
for candidate in Candidates:
    if candidate in candidate_votes:
        candidate_votes[candidate] += 1
    else:
        candidate_votes[candidate] = 1

# Calculate percentages and find the winner
winner = None
winner_votes = 0

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    formatted_percentage = "{:.3f}%".format(percentage)  # Format to 3 decimal places
    print(f"{candidate}: {formatted_percentage} ({votes})")
    
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Save output to a text file
output_file = "output.txt"
with open(output_file, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")

    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        formatted_percentage = "{:.3f}%".format(percentage)
        txt_file.write(f"{candidate}: {formatted_percentage} ({votes})\n")

    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("-------------------------\n")

print("Results saved to", output_file)

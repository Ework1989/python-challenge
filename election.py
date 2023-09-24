import os
import csv

# Define the path to the election data CSV file
poll_data_path = os.path.join(".", "Resources", "election_data.csv")

# Initialize variables to store election results
total_votes = 0
candidate_votes = {}
winner = None
winner_votes = 0

# Open the CSV file
with open(poll_data_path, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Iterate through each row in the CSV file
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]

        # Update candidate vote counts
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

        # Check if this candidate has the most votes so far
        if candidate_votes[candidate_name] > winner_votes:
            winner_votes = candidate_votes[candidate_name]
            winner = candidate_name

# Calculate the percentage of votes each candidate won
candidate_percentages = {}
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    candidate_percentages[candidate] = percentage

# Print the election results to the terminal
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes:,}")
print("----------------------------")
for candidate, percentage in candidate_percentages.items():
    print(f"{candidate}: {percentage:.3f}% ({candidate_votes[candidate]:,})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

# Write the election results to a file (PyPoll.txt)
with open("PyPoll.txt", "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Votes: {total_votes:,}\n")
    output_file.write("----------------------------\n")
    for candidate, percentage in candidate_percentages.items():
        output_file.write(f"{candidate}: {percentage:.3f}% ({candidate_votes[candidate]:,})\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("----------------------------\n")

# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of botes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote. 
#import csv
#import os

#csvpath = os.path.join('Resources', 'election_results.csv')
#with open(csvpath) as csvfile:
 #   csvreader = csv.reader(csvfile, delimiter=",")
  #  print(csvreader)
   # csv_header = next(csvreader)
    #print(csv_header)

#Assign a variable for the file to load and the path. 
#file_to_load = os.path.join('Resources', 'election_results.csv')

#with open(file_to_load) as election_data:
 #   print(election_data)

#import csv
#import os
# Assign a variable for the file to load and the path.
#with open(file_to_load) as election_data:
    # Print the file object.
     #print(election_data)

# Create a filename variable to a direct or indirect path to the file.
 #file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Hello World")
    #txt_file.write("Counties in the Election")
    # Write three counties to the file.
   # txt_file.write("\nArapahoe\nDenver\nJefferson")
    
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter. 
total_votes = 0 
# Candidate options
candidate_options = []
# Declear the empty dictionary.
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader =csv.reader(election_data)
    
    headers= next(file_reader)
    
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Print the candidate list.
print(candidate_votes)

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
    #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
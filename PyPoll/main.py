# 1. Importing

import os
import csv

# 2. setting the path
csvpath = os.path.join('Resources','election_data.csv')
text_path = "output.txt"

#3. Setting the variables
count = 0
candidates = []
candidate_votes = {}
winner_count = 0
W = ""


#4. Open the File
with open(csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile)
 
    #loop through to find the total votes
    for row in csvreader:

        # Find the total vote count
        count = count + 1

        candidate = row["Candidate"]
        # if statement to run on first occurence of candidate name
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 1
        
        candidate_votes[candidate] = candidate_votes[candidate] + 1


#5. Print the results to a text and terminal

    print("Election results")
    print("-------------------------")
    print("Total votes: " + str(count))
    print("-------------------------")

with open(text_path, 'w') as txt_file:
    election_header = (f"Election Results\n"
    f"---------------\n")
   
    txt_file.write(election_header)
    
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes)/float(count)*100
        if (votes > winner_count):
            winner_count = votes
            W = candidate
        print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
        txt_file.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")
 
    print("-------------------------")
    txt_file.write("---------------------\n")
    print(f"Winner: {W}")
    txt_file.write(f"Winner: {W}\n")
    txt_file.write("---------------------\n")
    print("-------------------------")
    
    txt_file.close

import os
import csv


csvpath = os.path.join('Resources','election_data.csv')
text_path = "output.txt"


total_votes = 0
candidates = []
candidate_votes = []


with open(csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile)
 
    #loop through to find the total votes
    for row in csvreader:

        # Find the total vote count
        total_votes += 1

        candidate = row["Candidate"]
        # if statement to run on first occurence of candidate name
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 1
        
        candidate_votes[candidate] = candidate_votes[candidate] + 1

    

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote


    print("Election results")

    print("--------------------------------------------------------------------------")

    print("Total votes: " + str(total_votes))

    print("----------------------------------------------------------------------------")

 
    print("----------------------------------------------------------------------------------------")
      
    print("Winner: " + winner)
    

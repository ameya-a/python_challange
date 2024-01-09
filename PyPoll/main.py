import os
import csv


csvpath = os.path.join('Resources','election_data.csv')

count = []

text_path = "output.txt"

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first
    csv_header = next(csvreader)

#The total number of votes cast
    total_votes = len(count)
#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote


    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + str(total_votes))

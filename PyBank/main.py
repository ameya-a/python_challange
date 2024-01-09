import os
import csv


#joining path
csvpath = os.path.join('Resources1','budget_data.csv')
text_path = "output.txt"

# open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    
    
    PL = []
    months = []

    #skip header
    for rows in csvreader:
        PL.append(int(rows[1]))
        months.append(rows[0])

    # The total number of months included in the dataset
    total_months = len(months)
    
    # revenue change
    pl_change = []


    for x in range(1, len(PL)):
        pl_change.append((int(PL[x]) - int(PL[x-1])))
    
    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    total_average = sum(pl_change) / len(pl_change)
    
  

    # The greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(pl_change)
    # The greatest decrease in profits (date and amount) over the entire period
    greatest_decrease = min(pl_change)


    # print the Results
    print("Financial Analysis")

    print("----------------------------")

    print("total months: " + str(total_months))

    print("Total: " + "$" + str(sum(PL)))

    print("Average change: " + "$" + str(total_average))

    print("Greatest Increase in Profits: " + str(months[pl_change.index(max(pl_change))+1]) + " (" + "$" + str(greatest_increase) + ")" )

    print("Greatest Decrease in Profits: " + str(months[pl_change.index(min(pl_change))+1]) + " (" + "$" + str(greatest_decrease) + ")")


file = open(text_path, 'w')
file.write("Financial Analysis + \n")
file.write("--------------------- + \n")
file.write("total months: " + str(total_months) + "\n")
file.write("Total: " + "$" + str(sum(PL)) + "\n")
file.write("Average Change: " + "%" + str(total_average) + "\n")
file.write("Greatest Increase in Profits: " + str(months[pl_change.index(max(pl_change))+1]) + " (" + "$" + str(greatest_increase) + ")" + "\n")
file.write("Greatest Decrease in Profits: " + str(months[pl_change.index(min(pl_change))+1]) + " (" + "$" + str(greatest_decrease) + ")" + "\n")
file.close()


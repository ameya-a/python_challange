import os
import csv


csvpath = os.path.join('Resources1','budget_data.csv')

months = []
PL = []
averageChange = []
#greatest_decrease = ["", 9999999]
#greatest_increase = ["", 0]

text_path = "output.txt"

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first
    csv_header = next(csvreader)


    #The total number of months included in the dataset
    total_months = len(months)
       
  
    #The net total amount of "Profit/Losses" over the entire period
    for row in csvreader:
        PL.append(int(row[1]))
        months.append(row[0])
        
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
    for x in range(1, len(PL)):
        averageChange.append((int(PL[x]) - int(PL[x-1])))
        
    #Average = group/count
    averageChange = sum(averageChange)/ len(averageChange)
       

#The greatest increase in profits (date and amount) over the entire period
    greatestIncrease = max(averageChange)
    

#The greatest decrease in profits (date and amount) over the entire period
    greatestDecrease = min(averageChange)



    print("Financial Analysis\n")
    print("----------------------------")
    print("Total Months: " + str(total_months))
    print("Total: " + "$" + str(sum(PL)))
    print("Average Change: " + "%" + str(averageChange))
    print("Greatest Increase in Profits: " + str(months[averageChange.index(max(averageChange))+1]) + " " + "$" + str(greatest_increase))
#print("Greatest Decrease In Profits: " + str(months[averageChange.index(min(averageChange))+1]))+ " " + "$" + str(greatestDecrease))


#file = open(text_path, 'w')
#    file.write("Financial Analysis\n")
#    file.write("---------------------\n")
 #   file.write("total months: " + str(total_months) + "\n")
    #file.write("Total: " + "$" + str(sum(PL))+ "\n")
    #file.write("Average Change: " + "%" + str(averageChange) + "\n")
    #file.write("
    #file.write("



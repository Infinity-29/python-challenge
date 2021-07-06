#!/usr/bin/env python
# coding: utf-8

# In[8]:


import os 
import csv


# In[9]:


csvpath = os.path.join('..', 'Resource','budget_data.csv')


# In[10]:


with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    months = []
    Finaltotal = []
    averagechange = []
    greatestincrease = []
    greatestdecrease = []
#Move pointer to next row , dont need header
    csv_header = next(csvfile)
    rowsvar = 0
    sums=0
#read through each row of data after header
    for row in csvreader:
        Finaltotal.append(row[1])
        months.append(row[0])
        rowsvar += 1
        sums = sums +int(row[1])
#Print Headline for Data
    print("Financial Analysis")
    print("----------------------------")

#Sum Total Number of Months in Budget Data
    totalmonths = len(months)
#print total months
    print("Total Months: " + str(totalmonths))
    print("Total: " +"$"+str(sums))


# In[11]:


#calculate average revenue change
change = []
for y in range(1, len(Finaltotal)):
    #append change list
    change.append(int(Finaltotal[y]) - int(Finaltotal[y-1]))
    average = sum(change) / len(change)
# print(change)
# print(average)
#print the average change   
print("Average change: " + "$" + str(round(average, 2)))
#Greatest increase max
greatestincrease = max(change)
#print greatest increase in profits
print("Greatest Increase in Profits: " + str(months[change.index(max(change))+1]) + " " + "($" + str(greatestincrease) + ")")
#Greatest decrease min
greatestdecrease = min(change)
#print greatest decrease in profits
print("Greatest Decrease in Profits: " + str(months[change.index(min(change))+1]) + " " + "($" + str(greatestdecrease) + ")")


# In[12]:


# Specify the file to write to
output_path = os.path.join("..", "Analysis", "Result.txt")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:
    # Initialize csv.writer
    #txtfile =txt.writer(txtfile)
    txtfile.write("Financial Analysis"+"\n")
    txtfile.write("----------------------------"+"\n")
    txtfile.write("Total Months: " + str(totalmonths)+"\n")
    txtfile.write("Total: " +"$"+str(sums)+"\n")
    txtfile.write("Average change: " + "$" + str(round(average, 2))+"\n")
    txtfile.write("Greatest Increase in Profits: " + str(months[change.index(max(change))+1]) + " " + "($" + str(greatestincrease) + ")\n")
    txtfile.write("Greatest Decrease in Profits: " + str(months[change.index(min(change))+1]) + " " + "($" + str(greatestdecrease) + ")\n")


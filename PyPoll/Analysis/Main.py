#!/usr/bin/env python
# coding: utf-8

# In[411]:


import os
import csv


# In[412]:


# Path to collect data from the Resources folder
election_csv = os.path.join('..', 'Resource', 'election_data.csv')
uniquecandidate=[]
Votes={}
totalvote=0
winningnumber=0
# Candidate={}
with open(election_csv) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
#Move pointer to next row , dont need header
    csv_header = next(csvfile)
#read through each row of data after header
    for row in csvreader:
        candidate_name = row[2]
        totalvote =totalvote  + 1
        if candidate_name not in uniquecandidate:
            uniquecandidate.append(candidate_name)
            Votes[candidate_name]=0
                
        Votes[candidate_name]=Votes[candidate_name] + 1
#uniquecandidate
    print("Election Results" + "\n")
    print("----------------------------")
    print("Total Votes: " +str(totalvote)+"\n")
    print("----------------------------" +"\n")
    
    for Candidate in Votes:
        uniquevotes = Votes.get(Candidate)
        vote_percentage =  (uniquevotes) /  (totalvote) * 100
        if (uniquevotes > winningnumber):
                winningnumber = uniquevotes
                winningcandidate = Candidate          
        voter_output = f"{Candidate}: {vote_percentage:.3f}% ({uniquevotes})\n"
        print(voter_output,end="")
    print("----------------------------")
    print("Winner: " + winningcandidate)
    print("----------------------------")


# In[422]:


# Specify the file to write to
output_path = os.path.join("..", "Analysis", "Result.txt")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:
        txtfile.write("Election Results" + "\n")
        txtfile.write("----------------------------" + "\n")
        txtfile.write("Total Votes: " +str(totalvote)+"\n")
        txtfile.write("----------------------------" +"\n")
        for Candidate in Votes:
            uniquevotes = Votes.get(Candidate)
            vote_percentage =  (uniquevotes) /  (totalvote) * 100
            if (uniquevotes > winningnumber):
                winningnumber = uniquevotes
                winningcandidate = Candidate          
            voter_output = f"{Candidate}: {vote_percentage:.3f}% ({uniquevotes})\n"
            txtfile.write(f"{Candidate}: {vote_percentage:.3f}% ({uniquevotes})\n")
        txtfile.write("----------------------------" +"\n")
        txtfile.write("Winner: " + winningcandidate + "\n")
        txtfile.write("----------------------------")


# In[ ]:





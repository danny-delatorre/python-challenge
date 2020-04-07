## PyPoll
'''
[Vote-Counting](Images/Vote_counting.png)

In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv).
The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:
'''
# Import the os module. This will allow us to create file paths across operating systems
import os

# Import module for reading CSV files (CSV stands for comma seperated variables)
import csv

# Lists & Variables that will be used to to store data
total_votes = 0 
candidates_list = []
raw_vote_count = []

# open file and path and # creating new variable and calling in new CSV method known as csv.reader 
with open('/Users/danny_delatorre/Desktop/python-challenge/PyPoll/election_data.csv', 'r') as csv_file:
  csv_reader = csv.reader(csv_file)

# print headers 
  csv_header = next(csv_reader)
  print ("\nElection Results:")

# The total number of votes cast  
  print("~~~~~~~~~~~~~~~~~~~")

  row_count = sum(1 for row in csv_reader) 
  print(f"Total Votes:", row_count)
  print(" ")

with open('/Users/danny_delatorre/Desktop/python-challenge/PyPoll/election_data.csv', 'r') as csv_file:
  csv_reader = csv.reader(csv_file)
  csv_header = next(csv_reader)

# Print list of candidates who received votes 
  print("Candidate: (# of votes) ~ '%' awarded")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

  for row in csv_reader:

    total_votes += 1

    #read from column 3 - Candidate
    candidates_csv = (row[2])

    #if candidate is in list -> locate the candidate by index & increment count
    if candidates_csv in candidates_list:
      index = candidates_list.index(candidates_csv)
      raw_vote_count[index] = raw_vote_count[index] + 1
    
    #if candidate was not found in candidates list then append and add 1 to vote count
    else:
        candidates_list.append(candidates_csv)
        raw_vote_count.append(1)
  
  Khan = round(raw_vote_count[0]/(raw_vote_count[0] + raw_vote_count[1] + raw_vote_count[2]+ raw_vote_count[3]), 2)
  Correy = round(raw_vote_count[1]/(raw_vote_count[0] + raw_vote_count[1] + raw_vote_count[2]+ raw_vote_count[3]), 2)
  Li = round(raw_vote_count[2]/(raw_vote_count[0] + raw_vote_count[1] + raw_vote_count[2]+ raw_vote_count[3]), 2)
  OTooley = round(raw_vote_count[3]/(raw_vote_count[0] + raw_vote_count[1] + raw_vote_count[2]+ raw_vote_count[3]),2)

  print(f'{candidates_list[0]}: ({raw_vote_count[0]}) ~ {Khan*100}%')
  print(f'{candidates_list[1]}: ({raw_vote_count[1]}) ~ {Correy*100}%')
  print(f'{candidates_list[2]}: ({raw_vote_count[2]}) ~ {(Li*100) - .000000000000002}%')
  print(f'{candidates_list[3]}: ({raw_vote_count[3]}) ~ {OTooley*100}%')
  print(" ")

# Check for election winner 
print("& the winner is...")
print("~~~~~~~~~~~~~~~~~~")

if (Khan > Correy):
    if (Khan > Li):
        if (Khan > OTooley):
            print ("~~~Khan wins the election!~~~")

if (Correy > Khan):
    if (Correy > Li):
        if (Correy > OTooley):
            print ("~~~Correy wins the election!~~~")

if (Li > Khan):
    if (Li > Correy):
        if (Li > OTooley):
            print ("~~~Li wins the election!~~~")

if (OTooley > Khan):
    if (OTooley > Li):
        if (OTooley > Correy):
            print ("~~~O'Tooley wins the election!~~~")




  


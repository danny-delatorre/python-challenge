'* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)
' * Your task is to create a Python script that analyzes the records to calculate each of the following:

# allows us to create file path across operating systems 
import os

# module in order for us to read a CSV file 
import csv 

# Store the file path associated with the file (note the backslash may be OS specific)
file = "..\python-challenge\PyBank\budget_data.csv"

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file, 'r') as text:

    # This stores a reference to a file stream
    print(text)

    # Store all of the text inside a variable called "lines"
    lines = text.read()

    # Print the contents of the text file
    print(lines)


  ' * The total number of months included in the dataset

  ' * The net total amount of "Profit/Losses" over the entire period

  ' * The average of the changes in "Profit/Losses" over the entire period

  ' * The greatest increase in profits (date and amount) over the entire period

  ' * The greatest decrease in losses (date and amount) over the entire period

*' As an example, your analysis should look similar to the one below:

  ' text
  ' Financial Analysis
  ----------------------------
  ' Total Months: 86
  ' Total: $38382578
  ' Average  Change: $-2315.12
  ' Greatest Increase in Profits: Feb-2012 ($1926159)
  ' Greatest Decrease in Profits: Sep-2013 ($-2196167)
  

' In addition, your final script should both print the analysis to the terminal and export a text file with the results.
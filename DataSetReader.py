"""
Author: Apurva Patel
Date: 25th Sept, 2020
Description: Sample program that uses a Python for opening and printing records from the CSV dataset on screen by using a data structure
"""

import csv

print("")
print("Author: Apurva Patel")
print("")
'''
Print statements for better readability of the output and author's name 
'''



try:   
    '''
    Try Except used to for exception handeling if file not found or an I/O error
    '''


    f = open('C:/Python_Workspace/CST_8333_Workspace/Assignment_1/InternationalCovid19Cases.csv', 'r')
    '''
    File is opened with the path
    '''


    csv_file = csv.reader(f)
    '''
    .reader method is used to read the CSV file and is assigned to csv_file variable
    '''


    data_structure = []
    '''
    data_structure is a Data Structure which it is a list at it's core and
    it holds the CSV data in lists. It is a list of lists. 
    '''


    for row in csv_file:
        data_structure.append(row)
    '''
    For loop implemented to append each and every row of data into
    the data_structure
    '''

        
    number_of_records = input("How many records would you like to see?")
    '''
    number_pf_records takes the user input for the number of rows to be displayed
    '''


    counter = 0
    for each_list in data_structure: 
        if counter > int(number_of_records):
            break
        counter+=1     
        print(each_list)
    '''
    #For loop implemented to get the data out of the data_structure list and
     to print it onto screen
    #Counter assists in determining the number of records to be printed
    '''   


    f.close()
    '''
    File is closed
    '''


except IOError:
      print('File not found')


__author__ = 'smwilliams'

# Install necessary libraries for Confluence API integration, CURL request, and reading/writing files
import os
import sys
import json
import getpass
import requests
from requests.auth import HTTPBasicAuth
import csv
#global variable for login
basicauth = ()

# Ask user for credentials
# QUESTION - Does Confluence have any SAML/Domain AUTH I could use instead?
def login():
    username = getpass.getuser()
    password = getpass.getpass()
    basicauth = (username, password)
    return basicauth

# Define function for labeling pages
# Initial version just has the user select one page, will iterate to reading from a file next
def labelpages():
    print("\n Add a label to Confluence pages. \n")
    # calls the login function
    authorization = login()
    pageid = input("\n Enter a page ID: ")
    labelname = input("\n Enter a label: ")
    # Sets up the label addition per the Confluence API documentation
    payload = {'prefix': 'global', 'name': labelname}
    # sends an HTTP request to Confluence
    url = 'https://mytableausandbox.tableaucorp.com/rest/api/content/' + pageid + '/' + "label"
    r = requests.post(url, json=payload, auth=authorization, verify=False)
    if r.status_code == 200:
        print("\n Success!")
    else:
        print( "Error " + r.status_code)
    return None
# Define function for deleting pages
def deletepaeges():
    print("\n Delete Confluence pages. \n")
    # calls the login function
    authorization = login()
    #sets up CMD and asks user for CSV file
    myFilePath = input('Enter the file path for your CSV of Page IDs (EG: C:\pageids.csv): ')
    print('I will now read each Page ID in ' +myFilePath+ ' and delete each page.')
    with open(myFilePath, 'rt') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            print('Requesting deletion of {}'.format(line[0]))
            url = 'https://mytableausandbox.tableaucorp.com/rest/api/content/{}'.format(line[0])
            # deletes the page via HTTP request
            r = requests.delete(url, auth=authorization, verify=False)
            # checks response and informs user
            if r.status_code == 200 or r.status_code == 204:
                print("\n Succesfully deleted!")
            else:
                print( "Error " + str(r.status_code))
    return None

# Initialize menu and ask user for choice
print("\nWelcome to the Confluence cleanup tool. This tool is currently pointed at the sandbox. \n")
choiceloop = True
while choiceloop:
    choice = input("Choose one: (D)elete Pages or (L)abel Pages?: ")
    if choice.lower() == "d":
        deletepaeges()
        choiceloop = False
    elif choice.lower() == "l":
        labelpages()
        choiceloop = False
    else:
        print("\n Please enter a valid choice.")
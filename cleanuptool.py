__author__ = 'smwilliams'

# Install necessary libraries for Confluence API integration, CURL request, and reading/writing files
import os
import sys
import json
import getpass
from requests.auth import HTTPBasicAuth
import csv

# Initialize menu and ask user for choice
print("Welcome to the Confluence API tool. \n")

# Log into Confluence
choiceloop = True
while choiceloop:
    choice = input("Choose one: (D)elete Pages, (M)ove Pages, or (L)abel Pages: ")
    if choice.lower() == "d":
        deletepaeges()
        choiceloop = False
    elif choice.lower() == "m":
        movepages()
        choiceloop = False
    elif choice.lower() == "l":
        labelpages()
        choiceloop = False
    else:
        print("Please enter a valid choice.")

# Ask user for credentials
# QUESTION - Does Confluence have any SAML/Domain AUTH I could use instead?
def login():
    username = input("Enter your Confluence username: ")
    password = getpass.getpass("Enter your Confluence password: ")
    basicauth = (username, password)
    return basicauth

# Define function for labeling pages
# Initial version just has the user select one page, will iterate to reading from a file next
def labelpages():
    print("\n Time to label some pages! \n")
    login()
    pageid = input("Enter a page ID: ")
    label = input("Enter a label: ")
    url = 'https://mytableausandbox.tableaucorp.com/rest/api/content/' + pageid + '/' + label
    # add URL request here

# Define function for deleting pages
def deletepaeges():
    pass

# Define function for moving pages
def movepages():
    pass

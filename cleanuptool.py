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
    print("\n Add a label to a Confluence page. \n")
    # calls the login function
    authorization = login()
    pageid = input("Enter a page ID: ")
    labelname = input("Enter a label: ")
    # Sets up the label addition per the Confluence API documentation
    payload = {'prefix': 'global', 'name': labelname}
    # sends an HTTP request to Confluence
    url = 'https://mytableausandbox.tableaucorp.com/rest/api/content/' + pageid + '/' + "label"
    r = requests.post(url, json=payload, auth=authorization, verify=False)
    if r.status_code == 200:
        print("Success!")
        print(r.json())
    elif r.status_code == 404:
        print("Error")
    else:
        print(r.status_code)
    return None
# Define function for deleting pages
def deletepaeges():
    pass

# Define function for moving pages
def movepages():
    pass


# Initialize menu and ask user for choice
print("Welcome to the Confluence API tool. \n")
choiceloop = True
while choiceloop:
    choice = input("Choose one: (D)elete Pages, (M)ove Pages, or Find (L)abels on a page?: ")
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
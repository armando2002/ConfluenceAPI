__author__ = 'smwilliams'

# Install necessary libraries for Confluence API integration, CURL request, and reading/writing files
import os
import sys
import json
import getpass
import urllib.request
import csv

# Initialize menu and ask user for choice
print("Welcome to the Confluence tool. \n")

# Ask user for credentials
# QUESTION - Does Confluence have any SAML/Domain AUTH I could use instead?
def login():
    username = rawinput("Enter your Confluence username: ")
    password = getpass.getpass("Enter your Confluence password: ")
    basicauth = {'username': username, 'password': password}

# Log into Confluence
choice = raw_input("Choose one: (D)elete Pages, (M)ove Pages, or (L)abel Pages: ")
if choice == "D" or "d":
    deletepaeges()
elif choice == "M" or choice == "m":
    movepages()
elif choice == "L" or choice == "l":
    labelpages()
else:
    print("Please enter a valid choice.")
    # QUESTION - How do I loop back to the top if the user doesn't select a valid choice?

# Define function for labeling pages
# Initial version just has the user select one page, will iterate to reading from a file next
def labelpages():
    url = 'https://mytableausandbox.tableaucorp.com/rest/api/audit?
    print("\n Time to label some pages! \n")
    login()


# Define function for deleting pages
def deletepaeges():
    pass
# Define function for moving pages
def movepages():
    pass

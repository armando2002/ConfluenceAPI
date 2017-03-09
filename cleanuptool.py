__author__ = 'smwilliams'

# Install necessary libraries for Confluence API integration, CURL request, and reading/writing files
import getpass
import requests
import csv
#global variable for login

# Ask user for credentials
def login():
    username = getpass.getuser()
    password = getpass.getpass()
    basicauth = (username, password)
    return basicauth

# Define function for labeling pages
def labelpages():
    print("\n Add a label to Confluence pages. \n")
    # calls the login function
    authorization = login()
    labelname = input("\n Enter the label you'd like to add: ")
    myFilePath = input('Enter the file path for your CSV of Page IDs (EG: C:\pageids.csv): ')
    print('I will now read each Page ID in ' +myFilePath+ ' and add the ' + labelname + ' label to each page.')
    # Sets up the label addition per the Confluence API documentation
    with open(myFilePath, 'rt') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            print('Adding {} label to page with PageID {}'.format(labelname, line[0]))
            payload = {'prefix': 'global', 'name': labelname}
            # sends an HTTP request to Confluence
            url = 'https://mytableausandbox.tableaucorp.com/rest/api/content/{}/label'.format(line[0])
            try:
                r = requests.post(url, json=payload, auth=authorization, verify=False)
                # checks response and informs user
                if r.status_code == 200:
                    print("\n Success!")
                else:
                    print( "Error " + r.status_code)
            except Exception as e:
                print('Error Occurred {}'.format(e))
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
            try:
                # deletes the page via HTTP request
                r = requests.delete(url, auth=authorization, verify=False)
                # checks response and informs user
                if r.status_code == 200 or r.status_code == 204:
                    print("\n Succesfully deleted!")
                else:
                    print( "Error " + str(r.status_code))
            except Exception as e:
                print('Error Occurred {}'.format(e))
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
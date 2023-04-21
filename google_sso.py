import json
from google.oauth2.credentials import Credentials

# Load the JSON configuration object from a file or variable
with open('config.json') as f:
    config = json.load(f)

# Parse the client ID, client secret, and redirect URIs from the configuration object
client_id = config['installed']['client_id']
client_secret = config['installed']['client_secret']
redirect_uris = config['installed']['redirect_uris']

# Create a Credentials object with the client ID, client secret, and redirect URIs
creds = Credentials.from_client_info(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uris=redirect_uris
)

#******************************************************************************************************#

# Loading the JSON file (is it different that the one on line 4??)
with open('credentials.json', 'r') as f:
    creds_json = json.load(f)

# Creating a Credentials object
creds = Credentials.from_authorized_user_info(info=creds_json)


#*************************************************************************************************************#


# Use the creds object to authenticate and make API requests
# (example code for using the Google Drive API)
from googleapiclient.discovery import build

# Create a Resource object for the Sheets API (Google Sheets?)
service = build('sheets', 'v4', credentials=creds)



# temporary fix for speadsheet id error and range name error
SPREADSHEET_ID = 'Speadsheet ID Here'
RANGE_NAME = 'Range Here'

# Get the values from a range of cells
result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range = RANGE_NAME).execute()
values = result.get('values', [])



#*************************************************************************************************************#



# Below may just be an example?? But I am not too sure
service = build('drive', 'v3', credentials=creds)
results = service.files().list(
    pageSize=10, fields="nextPageToken, files(id, name)").execute()
items = results.get('files', [])

if not items:
    print('No files found.')
else:
    print('Files:')
    for item in items:
        print(f'{item["name"]} ({item["id"]})')


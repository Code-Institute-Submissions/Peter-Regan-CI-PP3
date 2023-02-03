from __future__ import print_function
import gspread 
from google.oauth2.service_account import Credentials
# The code on line 4 was taken from this url:
# https://stackoverflow.com/questions/67551298/using-python-to-create-a-new-google-sheet
from gspread_dataframe import set_with_dataframe
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("UT2 Tracker Spreadsheet")

print("Welcome to Unstoppable UT2, where you can keep track of your UT2 performance. In case you're unfamiliar with the term 'UT2', it refers to an aerobic workout at an intensity which can be held for the full workout duration. You should be comfortable enough to speak and be operating at 65-75% maximimum heart rate. The workout should last approximately 60 minutes.")


def type_username():
    """
    Here is where the user will enter
    their username.
    """
    username = input("Create your new username here. If you've visited us"
    "before, we will fetch your existing data!")
    return username


username = type_username()
    

def create_new_user_sheet():
    """
    Creates new spreadsheet in Google Sheets.
    """
    sh = GSPREAD_CLIENT.create(f"{username} UT2 Tracker Spreadsheet")
    sh.share('regan.peter.w@gmail.com', perm_type='user', role='writer')


create_new_user_sheet()


def search_file():
    """Search file in drive location

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    creds = CREDS
    username = type_username()

    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)
        files = []
        page_token = None
        while True:
            # pylint: disable=maybe-no-member
            response = service.files().list(q="name contains 'UT2 Spreadsheet Tracker'",
                                            spaces='drive',
                                            fields='nextPageToken,'
                                                   'files(id, name)',
                                            pageToken=page_token).execute()
            for file in response.get('files', []):
                # Process change
                print(F'Found file: {file.get("name")}, {file.get("id")}')
            files.extend(response.get('files', []))
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break

    except HttpError as error:
        print(F'An error occurred: {error}')
        files = None

    return files


if __name__ == '__main__':
    search_file()
    










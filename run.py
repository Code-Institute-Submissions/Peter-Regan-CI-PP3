from __future__ import print_function
import google.auth
import gspread 
import os
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials
# The code on line 4 was taken from this url:
# https://stackoverflow.com/questions/67551298/using-python-to-create-a-new-google-sheet
from gspread_dataframe import set_with_dataframe
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

load_dotenv(dotenv_path="envfile.env")

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("UT2 Tracker Spreadsheet")
email_address = os.getenv("EMAIL_ADDRESS")

print("Welcome to Unstoppable UT2, where you can keep track of your UT2 performance. In case you're unfamiliar with the term 'UT2', it refers to an aerobic workout at an intensity which can be held for the full workout duration. You should be comfortable enough to speak and be operating at 65-75% maximimum heart rate. The workout should last approximately 60 minutes.")


def type_username():
    """
    Here is where the user will enter
    their username.
    """
    username = input("Create your new username here. If you've visited us"
    " before, we will fetch your existing data!\n")
    return username


username = type_username()

    
def create_new_user_workbook():
    """
    Creates new spreadsheet in Google Sheets.
    """
    
    workbook = GSPREAD_CLIENT.create(f"{username} UT2 Tracker Spreadsheet")
    worksheet_names = ["Treadmill", "Rowing Ergometer", "Exercise Bike"]
    for worksheet in worksheet_names:
        workbook.add_worksheet(title=worksheet, rows=1000, cols=3)
    
    
    
    
    
    
    # cell_format = {
    #     "textFormat": {
    #         "bold": True
    #     }
    # }
    # cells_to_format = ['A1', 'B1', 'C1']
    # run_worksheet = sh.add_worksheet("Treadmill", rows=1000, cols=3)
    # for cell in cells_to_format:
    #     run_worksheet.format(cell, cell_format)
    # run_worksheet.update_cell(1, 1, "Date")
    # run_worksheet.update_cell(1, 2, "Duration")
    # run_worksheet.update_cell(1, 3, "Distance")
    if email_address:
        workbook.share(email_address, perm_type='user', role='writer')
    else:
        print("Email address not found in the environment variables.")


create_new_user_workbook()


def search_file():
    """Search file in drive location

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    creds = CREDS

    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)
        files = []
        page_token = None
        while True:
            # pylint: disable=maybe-no-member
            response = service.files().list(q=f"name='{username} UT2 Tracker Spreadsheet'",
                                            spaces='drive',
                                            fields='nextPageToken,'
                                                   'files(name)',
                                            pageToken=page_token).execute()
            for file in response.get('files', []):
                # Process change
                print(F'Found file: {file.get("name")}')
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
    










from __future__ import print_function
import google.auth
import gspread 
import os
import re
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


def type_username():
    """
    Here is where the user will enter
    their username.
    """
    username = input("Create your new username here. If you've visited us"
    " before, we will fetch your existing data!\n")
    return username


def create_new_user_workbook():
    """
    Creates new spreadsheet in Google Sheets.
    """
    # Create new workbook with three worksheets.
    # Workbook will include user's typed username.
    # Three worksheets have titles listed below.
    # Default "Sheet1" worksheet gets deleted.
    # Worksheet list object created to be referred to later when formatting.
    user_workbook = GSPREAD_CLIENT.create(f"{username} UT2 Tracker Spreadsheet")
    worksheet_names = ["Treadmill", "Rowing Ergometer", "Exercise Bike"]
    worksheets = []
    for worksheet_name in worksheet_names:
        worksheet = user_workbook.add_worksheet(title=worksheet_name, rows=1000, cols=3)
        worksheets.append(worksheet)
    user_workbook.del_worksheet(user_workbook.sheet1)
    # Add cell formatting rule to be applied to all worksheets.
    cell_format = {
        "textFormat": {
            "bold": True
        }
    }
    cells_to_format = ['A1', 'B1', 'C1']
    for cell in cells_to_format:
        for worksheet in worksheets:
            worksheet.format(cell, cell_format)
    # Created nested for loops to iterate cell headings
    # across all three of user's worksheets.
    all_worksheet_types = user_workbook.worksheets()
    worksheet_headings = ["Date", "Duration", "Distance"]
    for i, worksheet in enumerate(all_worksheet_types):
        for j in range (3):
            worksheet.update_cell(1, j+1, worksheet_headings[j])
    if email_address:
        user_workbook.share(email_address, perm_type='user', role='writer')
    else:
        print("Email address not found in the environment variables.")


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
                print(f"Welcome back {username}!\nWhat would you like to do today?")
            files.extend(response.get('files', []))
            page_token = response.get('nextPageToken', None)
            if not files:
                print(f"Thanks for signing up {username}!\nWhat would you like to do today?")
                create_new_user_workbook()
            if page_token is None:
                break
            

    except HttpError as error:
        print(F'An error occurred: {error}')
        files = None

    return files


def user_workout_choice():
    """
    This will allow user to select which workout they want to log
    and write their data to the appropriate worksheet.
    """
    print(f"What kind of workout would you like to log today?")
    print("1. Treadmill\n2. Rowing Ergometer\n3. Exercise Bike")
    workout_choice = None
    while workout_choice not in ['1', '2', '3']:
        workout_choice = input("Type 1, 2 or 3 to choose one of the above.")
    workout_choice = int(workout_choice)
    if workout_choice == 1:
        call data writing function to treadmill worksheet
    elif workout_choice == 2:
        call data writing function to rowing worksheet
    elif workout_choice == 3:
        call data writing function to bike worksheet


def validate_user_workout_duration_input(time_data):
    """
    This will ensure that the user may only
    input data in this format - 00:00:00 -
    where the first two digits correspond to hours,
    the second two digits correspond to minutes
    and the last two digist correspond to seconds.
    """
    format = re.compile(r'\d\d:\d\d:\d\d')
    while True:
        match = format.fullmatch(time_data)
        if match is not None:
            return True
        else:
            print(f"Your time has not been entered in the correct format.\n")
            print(f"Your time should be entered in this format - 00:00:00\n")
            print(f"E.g. if your workout was an hour and twenty minutes long, you would enter 01:20:00.\n")
            print(f"Please try again.")
            time_data = input("Please input your workout duration here: ")


def validate_user_workout_distance_input(distance_data):
    """
    This will ensure that the user may only
    input data in this format - 00.00 -
    the digits correspond to kilometers measured
    to two decimal places.
    """
    format = re.compile(r'\d\d.\d\d')
    while True:
        match = format.fullmatch(distance_data)
        if match is not None:
            return True
        else:
            print(f"Your distance has not been entered in the correct format.\n")
            print(f"Your distance should be entered in this format - 00.00\n")
            print(f"E.g. if you cycled 23.4km on the exercise bike, you would enter 23.40\n")
            print(f"Please try again.")
            time_data = input("Please input your workout distance here: ")


    


if __name__ == '__main__':
    # print("Welcome to Unstoppable UT2, where you can keep track of your UT2 performance. In case you're unfamiliar with the term 'UT2', it refers to an aerobic workout at an intensity which can be held for the full workout duration. You should be comfortable enough to speak and be operating at 65-75% maximimum heart rate. The workout should last approximately 60 minutes.")
    username = type_username()
    # search_file()
    new_user_first_user_choice()
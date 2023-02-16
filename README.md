## README Document for Code Institute Portfolio Project 3 "Unstoppable UT2"

## Purpose
"Unstoppable UT2" was constructed as a requirement for Code Institute's Diploma in Full Stack Software Development course. Its purpose is to show that I have achieved a basic command of Python and can use it to adapt and combine functions that can manipulate data to solve given problems within a possible real world context.

In its imagined context, Unstoppable UT2 would be used by people who are training at a high athletic level. In case you're unfamiliar with the term 'UT2', it refers to an aerobic workout at an intensity which can be held for the full workout duration. You should be comfortable enough to speak and be operating at 65-75% maximimum heart rate. The workout should last approximately 60 minutes. At this training level, UT2 workouts are not considered strenuous and so performance or average speed across the workout is not considered extremely important. However, if you're training at a very high level, it makes sense that at some point you might want to see what "not strenuous" or "relatively easy" feels like to you. This is why it could be a good idea to see what your UT2 fitness level looks like over time, even if you're not measuring performance very strictly.

## Imagined User Stories
One particular imagined story could be my own. As a newcomer to rowing, I and my teammates are encouraged to do two to three UT2 sessions per week. I'm not meant to be working particularly hard in these sessions, but the moderate intensity for a prolonged period encourages capillarisation around the muscles and over time drastically improves the cardiovascular fitness required to complete longer races at a high level. I enjoy the relaxed UT2 sessions, but sometimes feel they can be a bit aimless. While I'm working through these "easy" workouts, I've started to wonder if my threshold for what I consider easy has increased, and so that's why perhaps a log like this could be useful or at least entertaining.

## Value Provided to the User
Unstoppable UT2 is very easy to use. All the user needs to do is remember a username and password and they will then have easy access to their data. This app removes the need for a physical logbook which can be easily lost or damaged. Arithmetic operations required to look at average times and distances for workouts are handled by the app too, or data can be read in summary form in a dataframe if the user would like a general overview of how their performance is going over time.

## Technologies Used
For this project I used GitHub to both host my repository. Within the repository I used Code Institute's Python Essentials Template which set up the command line interface required for this project to work when deployed externally to Heroku. This left me free to focus on working with Python within GitHub's built in code editor. 
I used Google's Drive API and the gspread library to write data to, read data from and perform operations on data from spreadsheets belonging to would-be users of Unstoppable UT2.

## Logic Plan / Design for This Project

Below you can see my rough plan for the flow of logic in this project. It is not fully detailed in that it doesn't include the data validation functions or all the possible applications of some functions to different worksheets, but I still did largely stick to this plan.

View flowchart here: https://drive.google.com/file/d/1lZLYNeJ9SZiJ3miG6Gne_i8ZOmBKFm_7/view?usp=sharing


## Project Features
The features most important to this project are the its functions and they inter-relate. 

Here some of the functions are explained below. Bear in mind that I will not discuss every function, but highlight a few where the possibility of user error and/or external error has been considered:

def new_user_or_existing_user() -

This function welcomes the user to the program. It gives them an option to indicate whether they are a new user or an existing user.
If the user selects the "new user" option, the search_username(username) function is then called to check if the new user's chosen username exists already. This prevents duplication. If the user's chosen username does not exist, they will be prompted to write a password. Both the type_username() and type_password() function have validation built into them which will be discussed later. Provided the username and password are valid, they will be entered and stored in an external spreadsheet so they can be accessed in future. At this point the search_file(username) function will be called. If this function does not find a spreadsheet in the drive where this project's data is stored containing the user's chosen username, it will call the create_new_worksheet(username) function, create a new workbook for the user and prompt them to log their first workout.

If the user indicates that they are an existing user, the function will still check if their username exists or not in the external spreadsheet containing usernames and passwords. This is in case they user has accidentally misspelled their username or mistakenly chose the existing user option. The user will be given the option of trying again or of creating a new username entirely. If the user provides a name which does exist in the spreadsheet, they will be prompted to write the corresponding password. Again, an incorrect password will prompt an oppotunity to try again or create a new username. If the username and password match, the search_file(username) function should be able to find their already existing spreadsheet and the user will be asked what functions of Unstoppable UT2 they would like to access.

def type_new_password() and def type_username() -

These functions performs largely as you would expect from their names. Note however the use of regular expressions to stipulate certain conditions about password and username validity. These conditions are of course arbitrary but I made them more as a means of showing consideration for making user data manageable.

def search_file(username) -

I can't claim credit for this function as it has come from the Google Drive API documentation. However, it might be worth noting how I have been able to pass username which was a locally defined variable near the beginning of the script as an argument into this function and subsequently from this function as an argument into most of the other functions in the script. It also excepts an error in the case of the script not being able to interact with the Drive API in the expected way.


def display_all_previous_workout_entries(worksheet, username) -

Though perhaps not a particularly interesting function in itself, it was interesting at this level of learning at least to be able to use this opportunity to display data in a Pandas dataframe which allows the user's data to be displayed in a very easily digestible visual format, even if still only in a console rather than a fully styled webpage.

def validate_user_workout_duration_input(time_data) -

Note here the use of regular expressions so that time data cannot be inputted into the spreadsheet in a way that cannot be parsed correctly into seconds by the script. Note also the use of try and except blocks to manage error handling. The same can be said of the validate_user_distance_input(distance_data) function too.

def main() -

In main there is a while loop so that the user always has the option to run some other part of the program before closing it. This means the user could access several of the programs main functions in one sitting rather than having to refresh the page after each time they've completed an operation.

## Testing

***PEP8 Validation***
The run.py file for this project passes through the pycodestyle linter with no major issues.
Some small issues include some of the lines being too long or some extensions not being synced, however these are not required for the project to work.

***Manual Testing***

| Test        | Expected Outcome | Actual Outcome | Pass/Fail |
| ----------- | ---------------- | -------------- | --------- | 
| Does the program open by prompting the user to indicate whether they are a new user or existing user?    | Program should open with a welcome message and prompt user to indicate if they are new or existing user with an input. | Same as expected. | Pass |
| Will the program accept a username of less than 5 characters? | If username is less than 5 characters, user will receive message stating correct username format and be prompted to try again. | Same as expected. | Pass |
| Will program accept a username with any uppercase letters, numbers or symbols? |If username is contains uppercase letters, numbers or symbols, user will receive message stating correct username format and be prompted to try again.  | Same as expected. | Pass |
| Will program  accept a password of less than 5 characters? | If password is less than 5 characters, user will receive message stating correct password format and be prompted to try again.  | Same as expected. | Pass |
| Will program accept a username with any uppercase letters, numbers or symbols? | If password contains uppercase letters, numbers or symbols, user will receive message stating correct password format and be prompted to try again. | Same as expected. | Pass |
| Does write_username_and_password_to_data_sheet(username, password) work? | This should take username and password data from username and write it to "Unstoppable UT2 Username and Password Data" spreadsheet in my Google Drive. | Same as expected. | Pass |
| Does search_file(username) function call create_new_user_workbook(username) function for a new user? | If this username doesn't already exist on a spreadsheet in the google drive, create_new_user_workbook(username) should be called to create one. | Same as expected. | Pass |
|  If a new workbook is created within the search_file(username) function call, will the user be prompted to log a new workout afterwards? | User should be given option to log a workout after new user workbook has been created. | Same as expected. | Pass |
| Does user_workout_choice(username) function work correctly? | If the user chooses 1 they will be prompted to give data for their treadmill workout. If they choose 2 they will be prompted to input their rowing ergometer data. If they choose 3 they will be prompted to input their exercise bike data. | Same as expected. | Pass |
| Does the validate_user_workout_duration_input(time_data) function work? | The user may only input time data in hh:mm:ss format where hh < 24, mm < 60 and ss < 60. If these conditions are met they will be prompted to try again. | Same as expected. | Pass |
| Does the validate_user_workout_distance_input(distance_data) function work? | Distance input in kilometres will only be accepted as two digits followed by a decimal point and two more digits. If these conditions are not met user will be prompted to try again. | Same as expected. | Pass |
| Does the while loop within main() work? | After logging their first workout, a new user should be given the option to run the program again or exist the program. | Same as expected. | Pass |
| Does the search_username(username) function work? | If a new user chooses a username that already exists, they will be prompted to try again and pick another. If an existing user correctly types a username that exists they will be prompted to input their password. If an existing user types a username that doesn't exist, they will be prompted to try again or choose a new username.| Same as expected. | Pass |
| Does check_password(username, password) work? | This function should be able to find the corresponding usernames and passwords in the Unstoppable UT2 Username and Password Data spreadsheet. If so and the username and password match, existing_user_choice(username) will be called. If not, the user will be prompted to try and type their password again. | Same as expected. | Pass |
| Does existing_user_choice(username) work? | When called this function should give the user the option to log a new workout (by calling user_workout_choice(username)), see all their past data for a particular workout type in a dataframe by calling display_all_previous_workout_entries(worksheet, username) or view their average scores for a particular workout type by calling calculate_average_workout_scores(worksheet, username). | Same as expected. | Pass |
| Does display_all_previous_workout_entries(worksheet, username) work? | This should display all the user's past workout information from one of the given worksheets in a dataframe. | Same as expected. | Pass |
| Does calling calculate_average_workout_scores(worksheet, username) work? | User should be able to view their average time and distance scores from their last three workouts of a specified type. If they have not yet logged three workouts, they will be alerted to this but given the average for their existing data anyway. If they have not logged any workouts of the specified type yet, they will be alerted to this too. | Same as expected. | Pass |
| Does the while loop within main work the same way for an existing user as it does for a new user? | After completing their chosen action for the program, the user should be given the choice to run the program again or exit. | Same as expected. | Pass |

## Deployment

***How to Deploy the Project***

Log into or register a new account at Heroku.

Click on the button New in the top right corner of the dashboard.

From the drop-down menu then select Create new app.

Enter your app name in the first field, the names must be unique so it's a good idea to check if your app name is available on Heroku before building the project.

Select your region.

Click on Create App.

Once the app is created you will see the Overview panel of the application. 

Click on Settings.

Scroll down and click on Reveal Config Vars.

For KEY field, type CREDS and for VALUE, copy and paste in the contents of the creds.json file from the directory. Press the Add button.
For the next KEY field, type ENVFILE and copy and paste the contents of the envfile.env into the VALUE field. Press the Add button.
For the last KEY field, type in 'PORT' and for the value field type in '8000'. Press the Add button.

Scroll down to Buildpacks. Click the button Add buildpack and select 'python'. Do the same step and add 'node.js'. 
Python must be listed first in build packs. If this is not the case they can be rearranged.

Click on the the Deploy tab. From the deployment method, select 'Github' as the deployment.

You will be asked to connect your github account. Confirm and proceed.

Search for your repository name and connect.

Once your Github account is connected, select how you want to push updates by clicking Enable Automatic Deploys. This means your app will automatically update every time you push your changes from Github.


## Acknowledgment of Code From Other Sources

This is generally commented in the run.py file but here is a list of sources for code that came from elsewhere:

1. The code for the function at line 213 was taken from here: https://developers.google.com/drive/api/guides/search-files
def search_file(username):
2. The function at line 372 is heavily reliant on lines of code that were generated by ChatGPT.
3. The format of the functions at lines 419 and 446 was taken directly from the Code Institute Love Sandwiches Walkthrough Project.

## Issues With This Project That Could Be Improved

Currently the user is able to input into the console even while it is printing messages or before some messages have been printed. This doesn't actually interfere with how the program works but could be confusing for a user and cause the data to appear in a way that is visually misleading if they accidentally jump ahead of the program. I have not changed this for the time being however due to the time limitations on this project.
The username and password setup is very rudimentary. There is also no help offered to the user if they cannot remember their password. 
Due to my handling of the username variable, it is also necessary to go right back to the start of the program each time the user would like to complete a difference action, rather than returning to a function at a specific point. This means that if the user wants to complete several actions, they do have to enter their username and password several times.
Again, due to time constraints, these are issues I decided to leave in the project for now.

## Scope for Future Additions To Project

1. This app would benefit a lot from styling. As the purpose of this project is primarily about using Python and not visual styling, I haven't added this element yet due to time limitations. However, a tool like Textualise could be very useful in this context as suggested by my mentor Ronan McClelland.
2. The username/password set up could be developed a lot. The current conditions for valid usernames and passwords are very basic and arbitrary. There is also nothing a user can do at this point if they cannot remember their password - if this is the case they must restart the programme and choose a new username and password.
3. It would be useful to add a delete_last_entry() function. This could be used in case the user enters data mistakenly that is incorrect, even if it is valid by the program's standards.


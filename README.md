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

![Logic Flowchart](https://github.com/sonetto104/Peter-Regan-CI-PP3/blob/main/utflowchart.jpeg)


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

***HTML, CSS and Javascript Testing***
I tested the index.html file and style.css file with the W3C HTML and CSS validators. I tested the script.js file with Beautify Tools (https://beautifytools.com/javascript-validator.php). All files passed tests without errors.

![Validation for HTML file](https://github.com/sonetto104/Peter-Regan-CI-PP2/blob/main/assets/images/interval-master-second-html-validation.png)

![Validation for CSS file](https://github.com/sonetto104/Peter-Regan-CI-PP2/blob/main/assets/images/interval-master-css-validation.png)

![Validation for JS file](https://github.com/sonetto104/Peter-Regan-CI-PP2/blob/main/assets/images/interval-master-js-validation.png)

***Lighthouse Report***

Interval Master also scores well on a lighthouse report.

![Lighthouse report for Interval Master](https://github.com/sonetto104/Peter-Regan-CI-PP2/blob/main/assets/images/interval-master-lighthouse-report.png)

***Manual Testing***

| Test        | Expected Outcome | Actual Outcome | Pass/Fail |
| ----------- | ---------------- | -------------- | --------- | 
| Is the site readable with correct content?    | Site should have three welcome modals without spelling errors, heading, clearly legible select elements containing intervals with qualities major, minor, perfect, augmented and diminished, and number ranging from unison to octave.       | Same as expected. | Pass |
| Is the site responsive to varying screen sizes?  | Site should be legible with clear flow with screen widths as small as 150px.      | Same as expected  ![Screenshot 1](https://github.com/sonetto104/Peter-Regan-CI-PP2/blob/main/assets/images/interval-master-screen-size-screenshot1.png) ![Screenshot 2](https://github.com/sonetto104/Peter-Regan-CI-PP2/blob/main/assets/images/interval-master-screen-size-screenshot2.png) ![Screenshot 3](https://github.com/sonetto104/Peter-Regan-CI-PP2/blob/main/assets/images/interval-master-screen-size-screenshot3.png) ![Screenshot 4](https://github.com/sonetto104/Peter-Regan-CI-PP2/blob/main/assets/images/interval-master-screen-size-screenshot4.png) ![Screenshot 5](https://github.com/sonetto104/Peter-Regan-CI-PP2/blob/main/assets/images/interval-master-screen-size-screenshot5.png) ![Screenshot from mobile](https://github.com/sonetto104/Peter-Regan-CI-PP2/blob/main/assets/images/interval-master-mobile-screenshot.jpg) | Pass |
| Do three welcome modals appear in correct order when site loads? | Welcome modal should appear when user visits site. Second instruction modal appears after clicking "next". 3rd instruction modal appears after clicking "next" | Same as expected. | Pass |
| Do all "close modal" buttons work on all three welcome modals? | All modals should close after clicking "X" button. | Same as expected. | Pass |
| Does quaver icon button play an interval? | Two notes should sound after pressing quaver icon button | Same as expected. | Pass |
| Does quaver icon button repeat same interval if "submit" has not been pressed? | If user has not pressed "submit" and they press the quaver button again, they should be able to repeatedly hear the same interval. | Same as expected. | Pass |
| Does the "correct answer" modal appear if user submits correct answer? | If user correctly identifies interval and presses submit, a modal should appear letting them know they are correct and prompt them to generate the next interval. | Same as expected. | Pass |
| Does a new interval play after the submission of a correctly identified interval? | If user submits answer that is correct, the next interval they play should be a different randomly generated interval. | Same as expected. | Pass |
| Does "wrong answer" modal appear if user submits wrong answer? | If the user incorrectly identifies interval and presses submit, a modal should appear letting them know they are incorrect and prompt them to try again. | Same as expected. | Pass |
| Is the same interval still played after the submission of an incorrect answer? | If the user incorrectly identifies an interval and presses submit, the next interval they play should be the same as what they heard before. | Same as expected. | Pass |
| Does score incrementor increment the score by 1 each time user indentifies correct interval? | Score should increase by 1 after each correct interval submission. | Same as expected. | Pass |
| Does score return to 0 after each incorrect identification of an interval? | Score should return to 0 each time an interval is incorrectly identified. | Same as expected. | Pass |
| Is each interval number matched to correct interval description? | Interval number for perfect unison = 0 <br><br> Interval number for minor 2nd = 1 or -1 <br><br> Interval number for major 2nd = 2 or -2 <br><br> Interval number for minor 3rd = 3 or -3 <br><br> Interval number for major 3rd = 4 or -4 <br><br> Interval number for perfect 4th = 5 or -5 <br><br> Interval number for augmented 4th = 6 or -6 <br><br> Interval number for diminished 5th = 6 or -6 <br><br> Interval number for perfect 5th = 7 or -7 <br><br> Interval number for minor 6th = 8 or -8 <br><br> Interval number for major 6th = 9 or -9 <br><br> Interval number minor 7th = 10 or -10 <br><br> Interval number for major 7th = 11 or -11 <br><br> Interval number for perfect octave = 12 or -12 <br><br> This will mean that the user will always be alerted that they are correct as long as they have selected the correct interval i.e. the interval descriptions assigned to each interval number are actually correct. | Same as expected. | Pass |
| Is Interval Master compatible with browsers other than Chrome? E.g. Microsoft Edge, Mozilla Firefox, Samsung Internet Browser | Site should appear the same on a variety of browsers. | Same as expected. | Pass |

***Special Note Regarding Perfect Unison:*** When a perfect unison is played, only one note sounds as there is no note difference in a unison interval.

***Preview of Responsive Site According to https://ui.dev/amiresponsive***

![Screenshot of site at different screen sizes](https://github.com/sonetto104/Peter-Regan-CI-PP2/blob/main/assets/images/responsive-preview-screenshot.png)

## Deployment

***How I Deployed the Project***
I visited my repository and pressed on the settings button. This brought me to a new page. On this new page there is a menu on the left hand side of the page. I clicked on the "Pages" option from this menu. Under "Source", I selected "main" as the branch from which to deploy the project from. I then clicked "Save" which automatically refreshed the page. After the few minutes required for Github to build the website, a link for the website appeared on this page.

***How to Run This Project From a Browser***

1. Install Google Chrome or Mozilla Firefox.
2. Install the Gitpod browser extension for your chosen browser.
3. Create a GitHub account and log into it.
4. Visit the repository for this project. It is called sonetto104/Peter-Regan-CI-PP2. You can also use this link to visit it: https://github.com/sonetto104/Peter-Regan-CI-PP2
5. Open this repository in Gitpod by clicking the green Gitpod button at the top right of the repository.
6. This will open a new workspace with the current state of the main branch of this repository.

***How to Run This Project Locally***

***Cloning the Repository***
1. Visit the Interval Master repository: https://github.com/sonetto104/Peter-Regan-CI-PP2
2. Click the "Code" dropdown box above the repository's file explorer and select the "Local" heading.
3. Underneath this, click the HTTPS subheading if it's not already selected.
4. Copy the link presented in the text field below this HTTPS subheading.
5. Open your preferred IDE and make sure it has support for Git.
6. Open the terminal, and create a directory where you can store the repository.
7. Type git clone and paste the previously copied text and press enter.
8. The repository will then be cloned to your selected directory.

***Manually Downloading the Repository***
1. Visit Interval Master GitHub repository: https://github.com/sonetto104/Peter-Regan-CI-PP2
2. Click the "Code" dropdown box next to the green Gitpod icon.
3. Click the "Download ZIP" option; this will download a copy of the selected branch's repository as a zip file.
4. Find the downloaded file on your your computer, and extract the ZIP to the folder where you would like to store the repository.

After either cloning or downloading the repository, you can have offline access to it by navigating to the directory where it was stored in your IDE.


## Acknowledgment of Code From Other Sources

This is generally commented in the relevant files but here is a list of sources for code that came from elsewhere:

1. The HTML and CSS code related to the modals is heavily dependent on code from this source: https://www.freecodecamp.org/news/how-to-build-a-modal-with-javascript/
2. A lot of the code that styles the h1, h2 and some of the p elements, as well as the quaver icon button comes from this source: https://codepen.io/mireille1306/pen/BawdXzY
3. The CSS code that styles the submit button and the select elements comes from this source: https://www.w3schools.com/css/tryit.asp?filename=trycss_buttons_animate3
4. The code for the event listener that monitors the user's selection from the select elements comes from this source: https://bobbyhadz.com/blog/javascript-select-onchange-get-value
5. The code for the score incrementor was taken directly from the Code Institute Love Maths Walkthrough Project.
6. The piano sounds came from a library belonging to the University of Iowa: https://theremin.music.uiowa.edu/MISpiano.html. I converted them from their original aiff. format.

## Issues With This Project That Could Be Improved

I suspect there are more efficient ways to write some of the code I have written in my script.js file due to some blocks being repeated, however, I am not yet fluent enough with Javascript to be able to figure out what they are right now. Given the time frame for this project, I feel it is more likely that I would confuse and introduce problems to code that already works by trying to edit it at this stage. However, in future it would be worth exploring how I could make the script.js file more economical and easier to read.

## Scope for Future Additions To Project

1. This site could have varying difficulty levels. Giving the user the option to play the notes simultaneously would add a grade of difficulty. Offering the user three notes instead of a pair would require them to identify two intervals rather than one, again adding a grade of difficulty. These could also be played separately or simultaneously. This would involve the addition of further controls and Javascript in order to allow the user to choose the conditions of difficulty.
2. A wider range of notes could be added. Currently this site tests intervals only within the range of one octave. Expanding the range by one octave more would allow the user to also test their recognition of compound intervals. This would also increase the frequency of some intervals which are currently underrepresented. Having only a one octave range limits the likely frequency of 7th and octave intervals.
3. A leaderboard could be built and attached to the website, allowing users to record their scores by username.
Though I was aware of these possibilities in building the project, I decided that they were slightly too ambitious for my current Javascript abilities. However, I would enjoy adding them in future.

# FLOATING POINT REPRESENTATION OF NUMBERS
Webapp created using flask

## Usage
installing requirements for starting the app:  
```
sudo bash install.sh
```
 or install from requirements.txt (installs all requirements to run tests)
```bash
pip3 install -r requirements.txt
```

### Running the app : 
python3 app.py


## runing tests

### backend tests:
```bash
pytest
```

### frontend tests
run using the 

## CODEBASE:

## app.py
"app.py" is the main component of this application. 
"app.py" is a single python file (considering the size of the app, we found it easier to not modularize it and keep comments instead)
within app.py, each component starts with
/# COMPONENT_NAME
/# END OF COMPONENT_NAME

Rest of the app.py is mostly self explanatory considering the naming used here.

## STATIC FOLDER
This folder contains all the images and the third party JS and CSS files and some common css and js files.

## HTML templates
./templates folder contains all the html files and the template each file uses.

`Template.html` has the basic structure of the entire app, and has an empty block for additional data that I want to put into it.
All other files are blocks that get inserted into the Template

scripts are writen within the each html component page (all pages other than the template) inline in the `<script>` tags as to make it easier to modify. 

## ADMIN
Checking for user feedbacks
```bash
python3 showFeedbacks.py
```

## TESTING

### Backend tests:
These are written using pytest in test_app.py

### Frontend tests:
These are written in quizTest.py in selenium
(the only major interaction is the quiz, so the test is specific to the quiz)
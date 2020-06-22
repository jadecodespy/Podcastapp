# Podcast Scheduling App

## Content

*	Project Objective
* App Functionality 
*	Database Structure
* CI Pipeline
*	Trello Board
*	Testing 
* Risk Assessment 
*	Current Issues 
*	Improvements 
* Author

## Project Objective
The project objective was to:
 “To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.”

To complete this task, I created a podcast scheduling application that allows you to create, read, update, and delete a podcast episode. As well as meeting the CRUD requirements, the following were also required:
*	Kanban board
*	A relational database consisting of at least 2 tables, with a modelled relationship
* A functional CRUD application created in Python following best practices.
*	Test suites for the application, as well as automated tests for validation of the application
*	A functioning front-end website using Flask
*	Code integrated into a Version Control System to be built through a CI server and deployed to a cloud based VM.

## App Functionality
To use this app, you first need to click on the home page to see if any podcast episode has been scheduled (an episode is a podcast with a topic title).


If there is nothing on the home page, then you click the topics page.
When you click the topics nav bar, you should be directed to the page where you can fill out a form to add a topic to the database.
To create a podcast episode, you need to click on the page and fill out the forms there. Input a podcast title, detail, and fill in the topic title (from above).
When you create an episode, you are redirected to the home page, where you can see an update and delete button. When you click the update button, it should redirect you to an update page, where you can update your topic title and description.
If you click the delete button, it should remove the topic and detail under the podcast.

## Database Structure
The below image is an Entity relationship diagram (ERD) showing the structure of the database. The first image shows what should have been in the database and the second image shows what was implemented in the database.
The app model is a many to many relationships between the Podcast and Topics table using an association table. This allows for the topic to be inputted in the podcast and vice versa.

## CI Pipeline


## Trello Board
https://trello.com/b/GVEQ2GPc/podcast-scheduling
## Testing 

## Risk Assessment 
https://docs.google.com/spreadsheets/d/19RzC2ij48FtX0PMgEw-ZFwpwvsn1Fmm9NylZkVbob7Y/edit?usp=sharing

## Current Issues 

## Improvements 
The first improvement is to the front-end look. Id like to make them visually appealing and colourful. I want to make the schedule page so when a user creates a podcast episode, they can add a date and a time. Also, to customize it to users and make it more secure. 

## Author
Jadesola Kanimodo





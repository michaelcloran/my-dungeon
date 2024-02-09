![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!

# Single User Dungeon

This game is a Python terminal game. Which runs in a Game Institute mock terminal on Heroku.

Users can explore the game level by entering rooms and picking up weapons and health as they go.
They can also attack dragons 9 in total 3 big dragons and 6 little dragons.

## How to play

When the user enters the game they are shown a Room list and asked for a room number which they
have to type and press enter then once in the room the contents of the room is described
at the upper area of the room menu which has options to go north east west and south/door exit.

If the player wants to cheat they can scroll up to the level plan which shows all rooms and entities
within the game level. This is handy for finding weapons and health by looking at the room floor plan.

typical instructions once in a room are Attack dragon or pickup health etc by pressing a number
in the menu list and pressing enter.

## Features

## Existing Features

* Random level generation 
    * The game level is generated then a script to choose a random room and random position with random entity from the listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms combined to select a random entity from this list and in the random room the random entity is added to a random position north east west or center (remember south is the door) then this random entity is removed from the list created by appending lists listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms so 
    that entity of the 18 is used up and this algorithm continues till there is no more entities.
    * The player if the cheat sheet is not used then they have to roam the dungeon by entering rooms to get weapons and to kill dragons.

* Input validation and error checking
    * there is two validation script one for validating the room number on the dungeon rooms list and one for validating input once entered a room.
    * Both input screens show a list and a number to select an item in the list
    * Once an item is chosen the user inputs the number of the item and presses enter
    * the validation checks for valid number and a range of number for the appropiate menu and displays an error message if the number is out of range
    * Also if the user enters a character which is not a number the validation shows an error message and rerenders the options list  

## Future Features   



## Wireframes/ Mockups and specification for the Game

Spec for game

A Dungeon has a corridore and the corridore has rooms

The Dungeon has a Class Dungeon and a Room class

A Dungeon has 12 rooms

The level has 6 dragons and 3 big dragons
the big dragons require a big shield and a long sword to kill 
The dragons are randomly generated in the rooms North, South, East, West, Center

you need a long sword to kill a big dragon and a sword to kill a little dragon
there is 3 powerups for swords in the level a sword and a long sword
There is 3 powerups for shields a little shield ad a big shield
there is 3 health powerups.

if you attack a big dragon with a basic sword you are killed
if you attack a big dragon with a long sword and a small shield you win with 50% health loss
if you attack a big dragon with a long sword and you have a big shield you win with 100% health

if you attack a dragon with a basic sword you are killed
if you attack a dragon with a basic sword and a small shield you win with 50% health
if you attack a dragon with a basic sword and big shield you win with 75% health
if you attack dragon with with long sword and a basic shield you win with 85% health
if you attack dragon with long sword and big shield you win 100% health

The game has a normal mode which shows the plans of the building
and a cheat mode which shows the plans of the building and enemys and powerups by rooms

### User interface flowchart

![Screenshot of flow chart for game](assets/readme_images/main_flowchart.png)

### Dungeon Coordinates Map

![Screenshot of level with compass](assets/readme_images/levelDirections.png)

### Wireframes

From flow chart Choice 1
********************************************************************************************
*                               Welcome to my Dungeon
*                               May you conquer and reap the benefits
*                               Enter the Rooms and slay the dragons 
*                               Pickup health and weapons as you go
********************************************************************************************
*
*                               Menu
*                               Choose a Room to goto
********************************************************************************************
1. Room 1
2. Room 2
3. Room 3
4. Room 4
5. Room 5
6. Room 6
7. Room 7
8. Room 8
9. Room 9
10. Room 10
11. Room 11
12. Room 12
13. Exit game

******************************************************************************************
Choose: __
******************************************************************************************

From flowchart choice 2
if no powerups, weapons or dragons in the room
********************************************************************************************
*
*                           You have entered Room (number)
*                           choose an option
*
*********************************************************************************************
1. go north 
2. go south 
3. go east
4. go west
6. goto middle of the room
7. exit room
*********************************************************************************************
Choose: __
*********************************************************************************************

if dragon in the room at north wall
********************************************************************************************
*
*                           You have entered Room (number)
*                           choose an option
*
*********************************************************************************************
1. go north to attack dragon
2. go south 
3. go east
4. go west
6. goto middle of the room
7. exit room
*********************************************************************************************
Choose: __
*********************************************************************************************

if powerups at the east wall
********************************************************************************************
*
*                           You have entered Room (number)
*                           choose an option
*
*********************************************************************************************
1. go north 
2. go south 
3. go east to pickup powerups
4. go west
6. goto middle of the room
7. exit room
*********************************************************************************************
Choose: __
*********************************************************************************************

if weapons at west wall
********************************************************************************************
*
*                           You have entered Room (number)
*                           choose an option
*
*********************************************************************************************
1. go north 
2. go south 
3. go east
4. go west to pickup small shield
6. goto middle of the room
7. exit room
*********************************************************************************************
Choose: __
*********************************************************************************************

if a dragon and weapons in the same room
********************************************************************************************
*
*                           You have entered Room (number)
*                           choose an option
*
*********************************************************************************************
1. go north to attack dragon
2. go south 
3. go east to pickup long sword
4. go west
6. goto middle of the room
7. exit room
*********************************************************************************************
Choose: __
*********************************************************************************************

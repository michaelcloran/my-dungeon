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

## Wireframes/ Mockups and specification for the Game

Spec for game

A Dungeon has a corridore and the corridore has rooms
The dungeon is made up of 6 rooms to the north and 6 room to the south of the corridore

The Dungeon class has 1 inherited classs room

A Dungeon has 12 rooms
6 rooms have a south side door
6 rooms with north side door

The level has 6 dragons and 3 big dragons
the big dragons require a big shield and a long sword to kill 
The dragons are randomly generated in the rooms n,s,e,w,c

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

Wireframes

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




# Single User Dungeon

This game is a Python terminal game. Which runs in a Game Institute mock terminal on Heroku.

Users can explore the game level by entering rooms and picking up weapons and health as they go.
They can also attack dragons 9 in total 3 big dragons and 6 little dragons.

## How to play

When the user loads the game they are first given the introduction screen where you are given some
briefs of the game with 3 options. 1 to play the game, 2 to view the readme on how to play the
game and 3 to exit the game. when the user chooses to play the game they are shown a Room list
and asked for a room number which they have to type and press enter then once in the room the
contents of the room is described at the upper area of the room menu which has options to go north
east west and south/door exit.

If the player wants to cheat they can scroll up to the level plan which shows all rooms and entities
within the game level. This is handy for finding weapons and health by looking at the room floor plan.

typical instructions once in a room are Attack dragon or pickup health etc by pressing a number
in the menu list and pressing enter.

## Features

## Existing Features

* Random level generation
    * The game level is generated then a script to choose a random room and random position with random entity from the listof_dragons_inrooms, listof_weaponss_inrooms, listof_medipacks_inrooms combined to select a random entity from this list(listof_entities_inrooms) and in the random room the random entity is added to a random position north east west or center (remember south is the door) then this random entity is removed from the list listof_entities_inrooms so that entity of the 18 is used up and this algorithm continues till there is no more entities.
    * The player if the cheat sheet is not used then they have to roam the dungeon by entering rooms to get weapons and to kill dragons. A typical cheat sheet
    is shown below. It shows a floor plan and entities within it for easy viewing.

    ![Screenshot of floor plan typical cheat sheet](assets/readme_images/cheat_floor_plan.png)

* Input validation and error checking
    * There is three validation scripts. Firstly the introduction screen has to be validated with 3 options and then once you choose to play the game a menu with the room number of the dungeon rooms list is shown and then the system has to validate input once entered a room. Where you can choose a direction with go direction, Attack dragon at direction, pickup entity at direction would be typical generic commands executed by choosing the option number and pressing enter.
    * All input screens show a list and a number to select an item in the list
    * Once an item is chosen the user inputs the number of the item and presses enter
    * the validation checks for valid number and a range of number for the appropiate menu and displays an error message if the number is out of range
    * Also if the user enters a character which is not a number the validation shows an error message and rerenders the input string.

* Menus
    * Introduction menu used for an introduction to the game and the goals of the game with a how to play option when number 2 is chosen and enter returned a screen which describes howto play the game is shown and if you press enter the how to play game screen is exited and the introduction menu is displayed again. If while here you choose 1 and press enter then you can go into the play game menu but if you choose option number 3 and press enter then the game is exited.

    ![Screenshot of Introductory menu](assets/readme_images/introduction_menu.png)

    * Dungeon Room listing. This menu is used to select which room the user wants to enter there is 12 rooms thus 12 options and number 13 for exit game.

    ![Screenshot of Dungeon Rom menu](assets/readme_images/dungeon_room_menu.png)

    * Room listing. This menu is used once a user enters a room. It has some features for instance it has a message you have entered room (number) 1 for this case. It has a description of the room just under the line for the room numnber. In this case To the center of the room there is a little dragon. Directly under this it shows player health 100 and under this there is [] which shows you that the player has no weapons yet. When the player picks up a weapon the english description of the weapon is shown in this list. Under this is the menu options 1. go north, 2. go east, 3. go west, 4. attack little dragon to the center and 5. go south and exit room. if you enter a number and press enter a validation script is run and checks if its in range 1 to 5 and that the number is really a number otherwise a ValueError exception is thrown and you get a message say you have to enter a number between 1 and 5 please try again. This message and prompt for new input is shown directly under the current prompt.

        Note: That the description and the menu options vary dependant on the contents of the room.

    ![Screenshot of typical Room menu](assets/readme_images/typical_room_menu.png)

* A timer is used in this game in order to give some measure of play. When the player starts to play the game the timer is started and when the player is killed a Game Over the player was killed by DRagon message is displayed with the amount of time in seconds that the player lasted in the game and the play again message is displayed with the introduction menu options rendered again for the player to easily reenter the game.

* There is 9 dragons in this challenge dungeon 3 big dragons and 6 little dragons once the player kills all 9 then the game is over and a well done message is displayed and the time taken is shown in seconds and the introduction menu is rerendered for the option to play again.

## Future Features
    * I would have loved to make this game concept into an actual 2D game with a graphics library but that option was not feasible with Heroku.

## Data Model
I used 2 classes in this project Room and Dungeon. The Room class is used within the Dungeon class as there is a list of Room objects. 12 in this case.

When the Dungeon class instance is instantiated the Dungeon constructor is called which call the create_rooms(number_of_rooms) method which creates the level then 3 lists are created in main to initialise the netities (listof_dragons_inrooms, listof_weapons_inrooms, listof_medipacks_inrooms) then these lists are passed to the dungeon object and the dungeon add_objects_to_rooms method where the level is populated with entities in random rooms at random positions and where the entities are randomly accessed. In this particular instance there is 18 entities 9 dragons, 3 shields ,3 swords and 3 medi packs

![Screenshot of classes with methods](assets/readme_images/class_diagram.png)

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
There is 3 powerups for shields a little shield and a big shield
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

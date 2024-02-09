import random
import sys
import time
# PP3 project by Michael Cloran
# 1/2/2024
# This is a basic single user Dungeon game

#  Globals
player_weapons_list = []


class Room:
    """The Room class is to create and manage the Room
    Note when you walk into a room you are at the door
    and the door is south the far wall is north and to 
    the left and right west and east
    """

    door = 0
    wall = 1
    center = 2
    
    def __init__(self):
        self.north = Room.wall
        self.south = Room.door
        self.east = Room.wall
        self.west = Room.wall
        self.center = Room.center
        self.roomNumber = 0
        


class Dungeon:
    """ 
    The Dungeon class is to create and manage the dungeon
    """
    
    def create_rooms(self, number_of_rooms):
        """
        creates the rooms and stores a room object in the roomObjList
        """
        for x in range(number_of_rooms):
            roomObj = Room()
            roomObj.roomNumber = (x+1)
            self.roomObjList.append(roomObj)

    def get_random_position_in_random_room(self):
        """
        get a random room and random position (north, east, west, center)
        It tests for possible collisions where a position is already taken
        and thus does a recursive call to another random room and random 
        position
        """

        randomRoomValue = random.randint(0, (11))  # 12 rooms
        
        # 1 north, 2 east, 3 west, 4 center remember south is a door
        randomPosition = random.randint(1, 4) 
        
        if randomPosition == 1:  # north
            if self.roomObjList[randomRoomValue].north != Room.wall:
                self.get_random_position_in_random_room()
            else:
                return [randomRoomValue, randomPosition]
                
        elif randomPosition == 2:  # east
            if self.roomObjList[randomRoomValue].east != Room.wall:
                self.get_random_position_in_random_room()
            else:
                return [randomRoomValue, randomPosition]

        elif randomPosition == 3:  # west
            if self.roomObjList[randomRoomValue].west != Room.wall:
                self.get_random_position_in_random_room()
            else:
                return [randomRoomValue, randomPosition]

        elif randomPosition == 4:  # center
            if self.roomObjList[randomRoomValue].center != Room.center:
                self.get_random_position_in_random_room()
            else:
                return [randomRoomValue, randomPosition]

    def __init__(self, number_of_rooms):  # Dungeon class constructor
        self.number_of_rooms = number_of_rooms
        self.roomObjList = []
        self.create_rooms(number_of_rooms)
        self.listOfEntitiesInRooms = []
        self.player_health = 100
        self.numberOfDragons = 9
        self.startTime = time.time()

    def add_objects_to_rooms(self, listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms):
        """
        Goes through a for look to loop 18 times which is the amount of 
        entities to be added to the game level
        firstly get_random_position_in_random_room is called to get random
        room and random position the a random entity is got and based on 
        the random position and random room the entity is added
        to the random room at random position
        """

        # remember only 18 entities for this simulation so 
        # get_random_position_in_randon_room will be called 18 times
        for x in range((len(listOfDragonsInRooms)+len(listOfWeaponssInRooms)+len(listOfMediPacksInRooms))):
            randomValues = self.get_random_position_in_random_room()
            while randomValues is None:
                randomValues = self.get_random_position_in_random_room()

            randomRoomValue = randomValues[0]
            randomPosition = randomValues[1]
            
            randomEntity = self.get_random_entity(listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms)

            if randomPosition == 1:  # north
                self.roomObjList[randomRoomValue].north = randomEntity
            elif randomPosition == 2:  # east
                self.roomObjList[randomRoomValue].east = randomEntity
            elif randomPosition == 3:  # west
                self.roomObjList[randomRoomValue].west = randomEntity
            elif randomPosition == 4:  # center
                self.roomObjList[randomRoomValue].center = randomEntity

    def get_random_entity(self, listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms):
        """
        The listOfEntitiesInRooms contains a list of entities to be added
        to the game a random entity is picked from the list and that entity
        is removed from the listOfEntitiesInRooms the random entity is
        returned
        """

        # rememeber the dungeon only has 12 Rooms 18 entities
        if len(self.listOfEntitiesInRooms) == 0:
            self.listOfEntitiesInRooms = listOfDragonsInRooms + listOfWeaponssInRooms+ listOfMediPacksInRooms
        
        randomInteger = random.randint(0, (len(self.listOfEntitiesInRooms)-1))
        strToReturn = self.listOfEntitiesInRooms[randomInteger]

        del self.listOfEntitiesInRooms[randomInteger]
        
        return strToReturn

    def show_dungeon_plan(self):
        """
        Loops through a floor plan and displays the floor plan with
        room numbers
        """
        print("Dungeon Plan")
        str1 = '-'
        str2 = "|"
        str3 = "!"
        strMainWall = str1 * 19
        spce = ' '
        print(strMainWall)
        for x in range(6):  # number of rooms over 2
            for i in range(5):
                if i == 2:  # middle row
                    if x == 0:

                        print(str2 + spce*5 + str3 + "1" +spce*3+ "2" +str3 + spce*5 + str2)
                    elif x == 1:

                        print(str2 + spce*5 + str3 + "3" +spce*3+ "4" +str3 + spce*5 + str2)
                    elif x == 2:

                        print(str2 + spce*5 + str3 + "5" +spce*3+ "6" +str3 + spce*5 + str2)
                    elif x == 3:

                        print(str2 + spce*5 + str3 + "7" +spce*3+ "8" +str3 + spce*5 + str2)
                    elif x == 4:

                        print(str2 + spce*5 + str3 + "9" +spce*2+ "10" +str3 + spce*5 + str2)
                    elif x == 5:

                        print(str2 + spce*5 + str3 + "11" +spce*1+ "12" +str3 + spce*5 + str2)
                    
                else:
                    print(str2 + spce*5+ str2 + spce*5 + str2 +spce*5 + str2)

            print(strMainWall)

    def show_dungeon_plan_with_entities(self):
        """
        Loops through floor plan and shows the entities for the game
        level
        """

        print("\nCheat Dungeon plan\nThe ! is a door and d little dragon and D big Dragon\ns for little shield and S for big shield\nw for little sword and W for big sword\nH for medi pack\n")        
        print("Dungeon Plan")
        str1 = '-'
        str2 = "|"
        str3 = "!"
        strMainWall = str1 * 19
        spce = ' '
        print(strMainWall)

        for x in range(6):  # number of rooms over 2
            for i in range(5):
                floorPlanStr = ""
                if i == 0:
                    if x == 0:  # room 1 and 2
                        print(self.get_floor_plan_edges_string(0, 1, "east"))
                    elif x == 1:  # room 3 and 4
                        print(self.get_floor_plan_edges_string(2, 3, "east"))
                    elif x == 2:  # room 5 and 6
                        print(self.get_floor_plan_edges_string(4, 5, "east"))
                    elif x == 3:  # room 7 and 8
                        print(self.get_floor_plan_edges_string(6, 7, "east"))
                    elif x == 4:  # room 9 and 10
                        print(self.get_floor_plan_edges_string(8, 9, "east"))
                    elif x == 5:  # room 11 and 12
                        print(self.get_floor_plan_edges_string(10, 11, "east"))

                elif i == 2:
                    if x == 0:  # room 1 and 2 middle on door
                        print(self.get_floor_plan_middle_string(0, 1))
                    elif x == 1:  # room 3 and 4 middle on door
                        print(self.get_floor_plan_middle_string(2, 3))
                    elif x == 2:  # room 5 and 6 middle on door
                        print(self.get_floor_plan_middle_string(4, 5))
                    elif x == 3:  # room 7 and 8 middle on door
                        print(self.get_floor_plan_middle_string(6, 7))
                    elif x == 4:  # room 9 and 10 middle on door
                        print(self.get_floor_plan_middle_string(8, 9))
                    elif x == 5:  # room 11 and 12 middle on door
                        print(self.get_floor_plan_middle_string(10, 11))
                    
                elif i == 4:
                    if x == 0:  # room 1 and 2
                        print(self.get_floor_plan_edges_string(0, 1, "west"))
                    elif x == 1:  # room 3 and 4
                        print(self.get_floor_plan_edges_string(2, 3, "west"))
                    elif x == 2:  # room 5 and 6
                        print(self.get_floor_plan_edges_string(4, 5, "west"))
                    elif x == 3:  # room 7 and 8
                        print(self.get_floor_plan_edges_string(6, 7, "west"))
                    elif x == 4:  # room 9 and 10
                        print(self.get_floor_plan_edges_string(8, 9, "west"))
                    elif x == 5:  # room 11 and 12
                        print(self.get_floor_plan_edges_string(10, 11, "west"))
                else:
                    print(str2 + spce*5+ str2 + spce*5 + str2 +spce*5 + str2)
            
            print(strMainWall)

    def get_floor_plan_edges_string(self, roomIndex1, roomIndex2, direction):
        """
        This function gets the east and west wall and adds entities to it if needed
        """

        str2 = "|"
        str3 = "!"
        spce = ' '
        floorPlanStr = ""
        if direction == "east":
            # room1
            if self.roomObjList[roomIndex1].east != 1:
                floorPlanStr = floorPlanStr + str2 + spce*2 + self.roomObjList[roomIndex1].east + spce*2 + str2
            else:
                floorPlanStr = floorPlanStr + str2 + spce*5 + str2  
                
            # put in corridore 
            floorPlanStr = floorPlanStr + spce*5

            # room2
            if self.roomObjList[roomIndex2].west != 1:
                floorPlanStr = floorPlanStr + str2 + spce*2 + self.roomObjList[roomIndex2].west + spce*2 + str2 
            else:
                floorPlanStr = floorPlanStr + str2 + spce*5 + str2
        
        elif direction == "west":
            # room1
            if self.roomObjList[roomIndex1].west != 1:
                floorPlanStr = floorPlanStr + str2 + spce*2 + self.roomObjList[roomIndex1].west + spce*2 + str2
            else:
                floorPlanStr = floorPlanStr + str2 + spce*5 + str2 
                
            # put in corridore 
            floorPlanStr = floorPlanStr + spce*5

            # room2
            if self.roomObjList[roomIndex2].east != 1:
                floorPlanStr = floorPlanStr + str2 + spce*2 + self.roomObjList[roomIndex2].east + spce*2 + str2 
            else:
                floorPlanStr = floorPlanStr + str2 + spce*5 + str2
        
        return floorPlanStr

    def get_floor_plan_middle_string(self, roomIndex1, roomIndex2):
        """
        This function gets the floorplan for the lines dealing with doors
        and add room numbers
        """

        str1 = '-'
        str2 = "|"
        str3 = "!"
        strMainWall = str1 * 19
        spce = ' '
        floorPlanStr = ""
        # room 1
        if self.roomObjList[roomIndex1].north != 1:
            floorPlanStr = floorPlanStr + str2 + self.roomObjList[roomIndex1].north
        else:
            floorPlanStr = floorPlanStr + str2 +spce  
                            
        if self.roomObjList[roomIndex1].center != 2:
            floorPlanStr = floorPlanStr + spce*2+ self.roomObjList[roomIndex1].center + spce + str3 + str(roomIndex1+1)
        else:
            floorPlanStr = floorPlanStr + spce*4 + str3 + str(roomIndex1+1)

        # put in corridore 
        if roomIndex2 != 9 and roomIndex2 != 11 and roomIndex2 != 10:
            floorPlanStr = floorPlanStr + spce*3
        elif roomIndex2 == 11:
            floorPlanStr = floorPlanStr + spce
        else:
            floorPlanStr = floorPlanStr + spce*2

        # room2
        if self.roomObjList[roomIndex2].center != 2:
            floorPlanStr = floorPlanStr + str(roomIndex2+1) + str3 + spce*2 + self.roomObjList[roomIndex2].center
            
        else:
            floorPlanStr = floorPlanStr + str(roomIndex2+1) + str3 + spce*3

        if self.roomObjList[roomIndex2].north != 1:
            floorPlanStr = floorPlanStr + spce + self.roomObjList[roomIndex2].north + str2
        else:
            floorPlanStr = floorPlanStr + spce*2 + str2
            
        return floorPlanStr        

    def enter_dungeon_choice(self):
        """
        This function displays the dungeon room menu 
        asking to go to a room and validates the input 
        if you enter option 13 the game is ended
        """

        data_str = 0
        while data_str != 13 and self.player_health > 0:
            print("*"*40)
            print("* Welcome to my Dungeon")
            print("* May you conquer and reap the benefits")
            print("* Enter the rooms amd slay the dragons")
            print("* Pickup health and weapons as you go")
            print("*"*40)
            print("*")
            print("* Menu")
            print("* Choose a room to goto")
            print("*"*40)

            print("1. Room 1 \t\t 2. Room 2")
            print("3. Room 3 \t\t 4. Room 4")
            print("5. Room 5 \t\t 6. Room 6")
            print("7. Room 7 \t\t 8. Room 8")
            print("9. Room 9 \t\t 10. Room 10")
            print("11. Room 11 \t\t 12. Room 12")
            print("13. Exit Game")
            print("\nChoose an option 1 to 13")

            self.get_enter_dungeon_choice_menu()

    def get_enter_dungeon_choice_menu(self):
        """
        This function gets the user input and validates it 
        if the user enter 13 the game is ended. If the
        player health <= 0 the game is over
        """

        data_str = input("Enter option:\n")

        if validate_enter_dungeon_choice_data(data_str):
            # enter room and display options
            if int(data_str) == 13:  # Exit game
                sys.exit()
            self.enter_room_choice(int(data_str))
            if self.player_health <= 0:
                sys.exit()
        else:
            self.get_enter_dungeon_choice_menu()

    def enter_room_choice(self, room_number):
        """
        This function displays the options within a room
        There is 3 options to be displayed for each direction 
        either Attack if there is a dragon to that direction
        or pickup an entity if there is an entity in that direction
        or to just goto that direction
        """

        data_str = 0
        while data_str != 5 and self.player_health > 0:
            print("*"*40)
            print("*")
            print(f"* You have entered Room  {room_number}")

            self.show_entities_in_room(room_number)
            print("Player Health:"+str(self.player_health))

            message = "["
            for obj in player_weapons_list:
                message = message + self.parse_entity_string(obj)+ ","
            if len(message) > 3:
                message = message[:-1]
            print(message+"]")
            
            print("* Choose an option")
            print("*")
            print("*"*40)

            if self.roomObjList[(room_number-1)].north != Room.wall:
                if self.roomObjList[(room_number-1)].north == "d" or self.roomObjList[(room_number-1)].north == "D":
                    print(f"1. Attack {self.parse_entity_string(self.roomObjList[(room_number-1)].north)} to the north")
                else:
                    print(f"1. Pickup {self.parse_entity_string(self.roomObjList[(room_number-1)].north)} to the north")
            else:
                print("1. go north")

            if self.roomObjList[(room_number-1)].east != Room.wall:
                if self.roomObjList[(room_number-1)].east == "d" or self.roomObjList[(room_number-1)].east == "D":
                    print(f"2. Attack {self.parse_entity_string(self.roomObjList[(room_number-1)].east)} to the east")
                else:
                    print(f"2. Pickup {self.parse_entity_string(self.roomObjList[(room_number-1)].east)} to the east")
            else:
                print("2. go east")
           
            if self.roomObjList[(room_number-1)].west != Room.wall:
                if self.roomObjList[(room_number-1)].west == "d" or self.roomObjList[(room_number-1)].west == "D":
                    print(f"3. Attack {self.parse_entity_string(self.roomObjList[(room_number-1)].west)} to the west")
                else:
                    print(f"3. Pickup {self.parse_entity_string(self.roomObjList[(room_number-1)].west)} to the west")
            else:
                print("3. go west")

            if self.roomObjList[(room_number-1)].center != Room.center:
                if self.roomObjList[(room_number-1)].center == "d" or self.roomObjList[(room_number-1)].center == "D":
                    print(f"4. Attack {self.parse_entity_string(self.roomObjList[(room_number-1)].center)} to the center")
                else:
                    print(f"4. Pickup {self.parse_entity_string(self.roomObjList[(room_number-1)].center)} to the center")
            else:
                print("4. go center of the room")
            
            print("5. go south and exit room")

            data_str = input("Choose an option:\n")
            while not (validate_enter_room_choice_data(data_str)):
                data_str = input("Choose an option:\n")
                
                if (data_str) == 5:  # Exit Room
                    data_str = 5
                    break  # break out of inner while loop

            if int(data_str) == 5:  # Exit Room
                print("Exit room")
                break  # break out of outer while loop

            self.move_forward(int(data_str), room_number)

    def move_forward(self, option, room_number):
        """
        This function moves the player to the north, south, east or west if there is a dragon it does and attack_dragon function
        if there is a power up that that is picked up via the pickup_entity function
        """

        if option == 1:  # north
            if self.roomObjList[(room_number-1)].north != Room.wall:
                if self.roomObjList[(room_number-1)].north == "d" or self.roomObjList[(room_number-1)].north == "D":
                    self.attack_dragon(room_number, "north") 
                else:
                    self.pickup_entity(room_number, "north")    
        elif option == 2:  # east
            if self.roomObjList[(room_number-1)].east != Room.wall:
                if self.roomObjList[(room_number-1)].east == "d" or self.roomObjList[(room_number-1)].east == "D":
                    self.attack_dragon(room_number, "east")
                else:
                    self.pickup_entity(room_number, "east")      
        elif option == 3:  # west
            if self.roomObjList[(room_number-1)].west != Room.wall:
                if self.roomObjList[(room_number-1)].west == "d" or self.roomObjList[(room_number-1)].west == "D":
                    self.attack_dragon(room_number, "west")
                else:
                    self.pickup_entity(room_number, "west")   
        elif option == 4:  # center  
            if self.roomObjList[(room_number-1)].center != Room.center:
                if self.roomObjList[(room_number-1)].center == "d" or self.roomObjList[(room_number-1)].center == "D":
                    self.attack_dragon(room_number, "center")
                else:
                    self.pickup_entity(room_number, "center")  

    def pickup_entity(self, room_number, direction):
        """
        This function pickups the weapons and health based on direction
        """

        if direction == "north":
            if self.roomObjList[(room_number-1)].north == "H":

                self.player_health = 100
            else:
                player_weapons_list.append(self.roomObjList[(room_number-1)].north)
            print("Pickedup:"+ self.parse_entity_string(self.roomObjList[(room_number-1)].north))
            print("Contents of you weapons list:")
            print(player_weapons_list)
            self.remove_entity(room_number, direction)
        elif direction == "east":
            if self.roomObjList[(room_number-1)].east == "H":
                
                self.player_health = 100
            else:
                player_weapons_list.append(self.roomObjList[(room_number-1)].east)
            print("Pickedup:"+ self.parse_entity_string(self.roomObjList[(room_number-1)].east))
            print("Contents of you weapons list:")
            print(player_weapons_list)
            self.remove_entity(room_number, direction)
        elif direction == "west":
            if self.roomObjList[(room_number-1)].west == "H":
                self.player_health = 100
            else:
                player_weapons_list.append(self.roomObjList[(room_number-1)].west)
            print("Pickedup:"+ self.parse_entity_string(self.roomObjList[(room_number-1)].west))
            print("Contents of you weapons list:")
            print(player_weapons_list)
            self.remove_entity(room_number, direction)
        elif direction == "center":
            if self.roomObjList[(room_number-1)].center == "H":
                self.player_health = 100
            else:
                player_weapons_list.append(self.roomObjList[(room_number-1)].center)
            print("Pickedup:"+ self.parse_entity_string(self.roomObjList[(room_number-1)].center))
            print("Contents of you weapons list:")
            print(player_weapons_list)
            self.remove_entity(room_number, direction)

    def attack_dragon(self, room_number, direction):
        """
        This function acks as a finite state machine a basic one to attack a
        dragon and based on the weapons the player has the health is adjusted
        based on rules in the finite state machine
        """

        if "s" in player_weapons_list and "w" in player_weapons_list:
            self.player_health = self.player_health - 50
            if self.player_health > 0:
                print(f"Dragon slayed you have {self.player_health} health")
                self.numberOfDragons = self.numberOfDragons - 1
            else:
                print("Player killed by Dragon") 
            
            self.remove_entity(room_number, direction)

        elif "s" in player_weapons_list and "W" in player_weapons_list:
            self.player_health = self.player_health - 25
            if self.player_health > 0:
                print(f"Dragon slayed you have {self.player_health} health")
                self.numberOfDragons = self.numberOfDragons - 1
            else:
                print("Player killed by Dragon") 
            self.remove_entity(room_number, direction)

        elif "S" in player_weapons_list and "w" in player_weapons_list:
            self.player_health = self.player_health - 15
            if self.player_health > 0:
                print(f"Dragon slayed you have {self.player_health} health")
                self.numberOfDragons = self.numberOfDragons - 1
            else:
                print("Player killed by Dragon") 

            self.remove_entity(room_number, direction)

        elif "S" in player_weapons_list and "W" in player_weapons_list:
            
            print(f"Dragon slayed you have {self.player_health} health")
            self.numberOfDragons = self.numberOfDragons - 1

            self.remove_entity(room_number, direction)

        else:
            self.player_health = 0
            print("-"*40)
            print("Game Over the player was killed by Dragon")
            endTime = time.time()
            durationOfGame = endTime - self.startTime
            durationOfGame = format(durationOfGame, ".2f")
            print(f"You lasted:{durationOfGame}")
            print("Play Again?")
            print("-"*40)
            display_intro()
            get_intro_input()
        
        if self.player_health <= 0:
            print("-"*40)
            print("Game Over the player was killed by Dragon")
            endTime = time.time()
            durationOfGame = endTime - self.startTime
            durationOfGame = format(durationOfGame, ".2f")
            print(f"You lasted:{durationOfGame}")
            print("Play Again?")
            print("-"*40)
            display_intro()
            get_intro_input()

        if self.numberOfDragons == 0:
            print("-"*40)
            print("Game Over you killed all the Dragons")
            endTime = time.time()
            durationOfGame = endTime - self.startTime
            print(f"You took {durationOfGame} to play the game. Well done!!")
            print("Play Again?")
            print("-"*40)
            display_intro()
            get_intro_input()

    def remove_entity(self, room_number, direction):
        """
        This function sets the directions to room.wall and if
        the direction is center it is set to room.center
        """
        if direction == "north":
            self.roomObjList[(room_number-1)].north = Room.wall
        elif direction == "east":
            self.roomObjList[(room_number-1)].east = Room.wall
        elif direction == "west":
            self.roomObjList[(room_number-1)].west = Room.wall
        elif direction == "center":
            self.roomObjList[(room_number-1)].center = Room.center

    def show_entities_in_room(self, room_number):
        """
        This function detects if the room is empty and prints a room empty 
        message it also shows a message showing the entities in the room 
        based on direction
        """

        if self.roomObjList[(room_number-1)].north == Room.wall and self.roomObjList[(room_number-1)].east == Room.wall and self.roomObjList[(room_number-1)].west == Room.wall and self.roomObjList[(room_number-1)].center == Room.center:
            print("* Room is empty")
        else:
            if self.roomObjList[(room_number-1)].north != Room.wall:
                print(f"* To the north there is a {self.parse_entity_string(self.roomObjList[(room_number-1)].north)}")
            if self.roomObjList[(room_number-1)].east != Room.wall:
                print(f"* To the east there is a {self.parse_entity_string(self.roomObjList[(room_number-1)].east)}")
            if self.roomObjList[(room_number-1)].west != Room.wall:
                print(f"* To the west there is a {self.parse_entity_string(self.roomObjList[(room_number-1)].west)}")
            if self.roomObjList[(room_number-1)].center != Room.center:
                print(f"* To the center of the room there is a {self.parse_entity_string(self.roomObjList[(room_number-1)].center)}")

    def parse_entity_string(self, entity_string):
        """
        This function parses an entity string and returns a description 
        string in english
        """

        if entity_string.strip() == "d":
            return "little dragon"
        elif entity_string.strip() == "D":
            return "big dragon"
        elif entity_string.strip() == "s":
            return "little shield"
        elif entity_string.strip() == "S":
            return "big shield"
        elif entity_string.strip() == "w":
            return "little sword"
        elif entity_string.strip() == "W":
            return "long sword"
        elif entity_string.strip() == "H":
            return "meddiepack"
        else:
            print(f"Error:{entity_string}")

def validate_enter_dungeon_choice_data(value):
    """
    This function validates the user input for the dungeon room choice dialog
    if the value chosen is not between 1 and 13 then a message is displayed 
    also if the value is not an integer a message is displayed
    """

    #fix

    try:
        val = int(value)
        if not (val >= 1 and val <= 13):
            raise ValueError()  
    except ValueError:
        print("Invalid choice: You must enter a Number between 1 and 13, please try again.\n")
        return False

    return True


def validate_enter_room_choice_data(value):
    """
    This function validates the options when in a room
    if the value is not between 1 and 5 a message is diplayed
    also if the value is not an integer a message is displayed
    """

    try:
        val = int(value)
        if not (val >= 1 and val <= 5):
            raise ValueError()  
    except ValueError:
        print("Invalid choice:You must enter a number between 1 and 5, please try again.\n")
        return False

    return True   

def validate_intro_choice_data(value):
    """
    This function validates the intro input data
    if the value is not between 1 and 2 a error
    message is displayed and if the value is
    not a number an error message is displayed
    """

    try:
        val = int(value)
        if not (val >= 1 and val <= 2):
            raise ValueError()  
    except ValueError:
        print("Invalid choice: You mush enter a Number either 1 or 2!, please try again.\n")
        return False

    return True      


def display_intro():
    """
    This function displays the intro screen
    """

    print("Welcome to my Dungeon")
    print("You have entered an era of dragons")
    print("")
    print("To play the game use the numbers on the menu of items and when asked for a")
    print("choice enter one and press enter")
    print("The goal of this game is to kill all the dragons in the least amount of time")
    print("HINT: You need a sword and a shield to kill a dragon or you'll be toast!")
    print("\n\n\n")
    print("1. play Game \t 2. Exit Game")
    print("\n\n\n")
    print("To play the game choose 1 or 2 to exit")

def get_intro_input():

    data_str = input("Enter option:\n")

    if validate_intro_choice_data(data_str):
        if int(data_str) == 2:
            sys.exit()
        main()
    else:
        get_intro_input()


def main():
    dungeon = Dungeon(12)

    # global player_weapons_list
    # player_weapons_list = []
    

    """
    display an empty Dungeon
    """
    dungeon.show_dungeon_plan()

    # d is a small dragon a D is a big dragon
    listOfDragonsInRooms = ["d", "d", "d", "d", "d", "d", "D", "D", "D"]
    # s is a small shield and a S is a large shield, a w is a small sword
    # and a W is a large sword
    listOfWeaponssInRooms = ["s", "S", "S", "w", "W", "W"]
    # H is a medie pack when picked up restores the players health
    listOfMediPacksInRooms = ["H", "H", "H"]

    dungeon.add_objects_to_rooms(listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms)         

    dungeon.show_dungeon_plan_with_entities()
    
    dungeon.enter_dungeon_choice()

display_intro()
get_intro_input()

# main()
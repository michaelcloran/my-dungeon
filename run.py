"""
# PP3 project by Michael Cloran
# 1/2/2024
# This is a basic single user Dungeon game
# It was created for Code Institute project 3
"""
import random
import sys
import time


#  Globals
player_weapons_list = []


class Room:
    """The Room class is used to create and manage the Room
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
        self.room_number = 0


class Dungeon:
    """
    The Dungeon class is to create and manage the dungeon
    """

    def create_rooms(self, number_of_rooms):
        """
        creates the rooms and stores a room object in the room_obj_lst

        Args:
            number_of_rooms (int): accepts an integer value
        """

        for x in range(number_of_rooms):
            room_obj = Room()
            room_obj.room_number = x+1
            self.room_obj_lst.append(room_obj)

    def get_random_position_in_random_room(self):
        """
        Get a random room and random position (north, east, west, center)
        It tests for possible collisions where a position is already taken
        and thus does a recursive call to another random room and random
        position
        """

        random_room_val = random.randint(0, (11))  # 12 rooms

        # 1 north, 2 east, 3 west, 4 center remember south is a door
        random_pos = random.randint(1, 4)

        if random_pos == 1:  # north
            if self.room_obj_lst[random_room_val].north != Room.wall:
                self.get_random_position_in_random_room()
            else:
                return [random_room_val, random_pos]

        elif random_pos == 2:  # east
            if self.room_obj_lst[random_room_val].east != Room.wall:
                self.get_random_position_in_random_room()
            else:
                return [random_room_val, random_pos]

        elif random_pos == 3:  # west
            if self.room_obj_lst[random_room_val].west != Room.wall:
                self.get_random_position_in_random_room()
            else:
                return [random_room_val, random_pos]

        elif random_pos == 4:  # center
            if self.room_obj_lst[random_room_val].center != Room.center:
                self.get_random_position_in_random_room()
            else:
                return [random_room_val, random_pos]

    def __init__(self, number_of_rooms):  # Dungeon class constructor
        """
        The Dungeon class constructor

        Args: number_of_rooms (int): accepts an integer value
        """

        self.number_of_rooms = number_of_rooms
        self.room_obj_lst = []
        self.create_rooms(number_of_rooms)
        self.listof_entities_inrooms = []
        self.player_health = 100
        self.numberof_dragons = 9
        self.start_time = time.time()

    def add_objects_to_rooms(self, listof_dragons_inrooms,
                             listof_weapons_inrooms,
                             listof_medipacks_inrooms):
        """
        Goes through a for look to loop 18 times which is the amount of
        entities to be added to the game level
        firstly get_random_position_in_random_room is called to get random
        room and random position the a random entity is got and based on
        the random position and random room the entity is added
        to the random room at random position

        Args:
            listof_dragons_inrooms a list containing the dragons
            listof_weapons_inrooms a list containing the weapons
            listof_medipacks_inrooms a list containing medipacks
        """

        # remember only 18 entities for this simulation so
        # get_random_position_in_randon_room will be called 18 times
        numberof_entities = len(listof_dragons_inrooms) \
            + len(listof_weapons_inrooms) \
            + len(listof_medipacks_inrooms)

        for x in range(numberof_entities):
            random_vals = self.get_random_position_in_random_room()
            while random_vals is None:
                random_vals = self.get_random_position_in_random_room()

            random_room_val = random_vals[0]  # ramdom room number
            random_pos = random_vals[1]  # random position N,E,W,C (int)

            random_entity = self.get_random_entity(listof_dragons_inrooms,
                                                   listof_weapons_inrooms,
                                                   listof_medipacks_inrooms)

            if random_pos == 1:  # north
                self.room_obj_lst[random_room_val].north = random_entity
            elif random_pos == 2:  # east
                self.room_obj_lst[random_room_val].east = random_entity
            elif random_pos == 3:  # west
                self.room_obj_lst[random_room_val].west = random_entity
            elif random_pos == 4:  # center
                self.room_obj_lst[random_room_val].center = random_entity

    def get_random_entity(self,
                          listof_dragons_inrooms,
                          listof_weapons_inrooms,
                          listof_medipacks_inrooms):
        """
        The listof_entities_inrooms contains a list of entities to be added
        to the game a random entity is picked from the list and that entity
        is removed from the listof_entities_inrooms the random entity is
        returned

        Args:
            listof_dragons_inrooms (list)
            listof_weapons_inrooms (list)
            listof_medipacks_inrooms (list)
        """

        # rememeber the dungeon only has 12 Rooms 18 entities
        if len(self.listof_entities_inrooms) == 0:
            self.listof_entities_inrooms = listof_dragons_inrooms \
                + listof_weapons_inrooms + listof_medipacks_inrooms

        random_int = random.randint(0, (len(self.listof_entities_inrooms)-1))
        strto_ret = self.listof_entities_inrooms[random_int]

        del self.listof_entities_inrooms[random_int]

        return strto_ret

    def show_dungeon_plan(self):
        """
        Loops through a floor plan and displays the floor plan with
        room numbers
        """

        print("Dungeon floor Plan")
        str1 = '-'
        str2 = "|"
        str3 = "!"
        str_main_wall = str1 * 19
        spce = ' '
        print(str_main_wall)
        for x in range(6):  # number of rooms over 2 6 rows
            for i in range(5):  # with 5 characters to represtent (floor plan)
                if i == 2:  # middle row need to add the door str3
                    if x == 0:  # room 1 and room 2

                        print(str2 + spce * 5 + str3 + "1" + spce * 3 + "2" +
                              str3 + spce * 5 + str2)
                    elif x == 1:  # room 3 and 4

                        print(str2 + spce * 5 + str3 + "3" + spce * 3 + "4" +
                              str3 + spce * 5 + str2)
                    elif x == 2:  # room 5 and 6

                        print(str2 + spce * 5 + str3 + "5" + spce * 3 + "6" +
                              str3 + spce * 5 + str2)
                    elif x == 3:  # room 7 and 8

                        print(str2 + spce * 5 + str3 + "7" + spce * 3 + "8" +
                              str3 + spce * 5 + str2)
                    elif x == 4:  # room 9 and 10

                        print(str2 + spce * 5 + str3 + "9" + spce * 2 + "10" +
                              str3 + spce * 5 + str2)
                    elif x == 5:  # room 11 and 12

                        print(str2 + spce * 5 + str3 + "11" + spce * 1 + "12" +
                              str3 + spce * 5 + str2)

                else:
                    print(str2 + spce * 5 + str2 + spce * 5 + str2 +
                          spce * 5 + str2)

            print(str_main_wall)

    def show_dungeon_plan_with_entities(self):
        """
        Loops through floor plan and renders the entities for the game
        level and floor plan
        """

        print("\nCheat Dungeon plan\n" +
              "The ! is a door and d little dragon and D big Dragon\n" +
              "s for little shield and S for big shield\n" +
              "w for little sword and W for big sword\n" +
              "H for medi pack\n")

        print("Dungeon Plan")
        str1 = '-'
        str2 = "|"
        str_main_wall = str1 * 19
        spce = ' '
        print(str_main_wall)

        for x in range(6):  # number of rooms over 2
            for i in range(5):  # print 5 char to represnet room floor plan

                if i == 0:  # top
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

                elif i == 2:  # middle
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

                elif i == 4:  # bottom
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
                    print(str2 + spce * 5 + str2 + spce * 5 + str2 +
                          spce * 5 + str2)

            print(str_main_wall)

    def get_floor_plan_edges_string(self, room_indx1, room_indx2, direction):
        """
        This function gets the east and west wall and adds entities
        to it if needed

        Args:
            room_indx1 (int)
            room_indx2 (int)
            direction (string) E,W

        return:
            floor_plan_str
        """

        str2 = "|"
        spce = ' '
        floor_plan_str = ""
        if direction == "east":
            # room1
            if self.room_obj_lst[room_indx1].east != 1:
                floor_plan_str = floor_plan_str + str2 + spce*2 \
                    + self.room_obj_lst[room_indx1].east + spce*2 + str2
            else:
                floor_plan_str = floor_plan_str + str2 + spce*5 + str2

            # put in corridore
            floor_plan_str = floor_plan_str + spce*5

            # room2
            if self.room_obj_lst[room_indx2].west != 1:
                floor_plan_str = floor_plan_str + str2 + spce*2 \
                    + self.room_obj_lst[room_indx2].west + spce*2 + str2
            else:
                floor_plan_str = floor_plan_str + str2 + spce*5 + str2

        elif direction == "west":
            # room1
            if self.room_obj_lst[room_indx1].west != 1:
                floor_plan_str = floor_plan_str + str2 + spce*2 \
                    + self.room_obj_lst[room_indx1].west + spce*2 + str2
            else:
                floor_plan_str = floor_plan_str + str2 + spce*5 + str2

            # put in corridore
            floor_plan_str = floor_plan_str + spce*5

            # room2
            if self.room_obj_lst[room_indx2].east != 1:
                floor_plan_str = floor_plan_str + str2 + spce*2 + \
                                 self.room_obj_lst[room_indx2].east +  \
                                 spce*2 + str2
            else:
                floor_plan_str = floor_plan_str + str2 + spce*5 + str2

        return floor_plan_str

    def get_floor_plan_middle_string(self, room_indx1, room_indx2):
        """
        This function gets the floorplan for the lines dealing with doors
        and add room numbers

        Args:
            room_indx1 (int)
            room_indx2 (int)

        return:
            floor_plan_str (string)
        """

        str2 = "|"
        str3 = "!"
        spce = ' '
        floor_plan_str = ""
        # room 1
        if self.room_obj_lst[room_indx1].north != 1:
            floor_plan_str = floor_plan_str + str2 + \
                self.room_obj_lst[room_indx1].north
        else:
            floor_plan_str = floor_plan_str + str2 + spce

        if self.room_obj_lst[room_indx1].center != 2:
            floor_plan_str = floor_plan_str + spce * 2 +\
                 self.room_obj_lst[room_indx1].center +\
                 spce + str3 + str(room_indx1 + 1)
        else:
            floor_plan_str = floor_plan_str + spce * 4 + str3 \
                + str(room_indx1+1)

        # put in corridore
        if room_indx2 != 9 and room_indx2 != 11 and room_indx2 != 10:
            floor_plan_str = floor_plan_str + spce*3
        elif room_indx2 == 11:
            floor_plan_str = floor_plan_str + spce
        else:
            floor_plan_str = floor_plan_str + spce*2

        # room2
        if self.room_obj_lst[room_indx2].center != 2:
            floor_plan_str = floor_plan_str + str(room_indx2+1) + str3 +\
                             spce*2 + self.room_obj_lst[room_indx2].center

        else:
            floor_plan_str = floor_plan_str + str(room_indx2+1) + \
                str3 + spce*3

        if self.room_obj_lst[room_indx2].north != 1:
            floor_plan_str = floor_plan_str + spce + \
                            self.room_obj_lst[room_indx2].north + \
                            str2
        else:
            floor_plan_str = floor_plan_str + spce*2 + str2

        return floor_plan_str

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

        Args:
            room_number (int)
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
                message = message + self.parse_entity_string(obj) + ","
            if len(message) > 3:
                message = message[:-1]
            print(message+"]")

            print("* Choose an option")
            print("*")
            print("*"*40)

            n_str = self.room_obj_lst[(room_number-1)].north

            if self.room_obj_lst[(room_number-1)].north != Room.wall:
                if self.room_obj_lst[(room_number-1)].north == "d" or\
                   self.room_obj_lst[(room_number-1)].north == "D":

                    print(f"1. Attack {self.parse_entity_string({n_str})}"
                          + " to the north")
                else:
                    print(f"1. Pickup {self.parse_entity_string({n_str})}"
                          + " to the north")
            else:
                print("1. go north")

            e_str = self.room_obj_lst[(room_number-1)].east

            if self.room_obj_lst[(room_number-1)].east != Room.wall:
                if self.room_obj_lst[(room_number-1)].east == "d" or\
                   self.room_obj_lst[(room_number-1)].east == "D":

                    print(f"2. Attack {self.parse_entity_string({e_str})}"
                          + " to the east")
                else:
                    print(f"2. Pickup {self.parse_entity_string({e_str})}"
                          + " to the east")
            else:
                print("2. go east")

            w_str = self.room_obj_lst[(room_number-1)].west

            if self.room_obj_lst[(room_number-1)].west != Room.wall:
                if self.room_obj_lst[(room_number-1)].west == "d" or \
                   self.room_obj_lst[(room_number-1)].west == "D":

                    print(f"3. Attack {self.parse_entity_string({w_str})}"
                          + " to the west")
                else:
                    print(f"3. Pickup {self.parse_entity_string({w_str})}"
                          + " to the west")
            else:
                print("3. go west")

            c_str = self.room_obj_lst[(room_number-1)].center

            if self.room_obj_lst[(room_number-1)].center != Room.center:
                if self.room_obj_lst[(room_number-1)].center == "d" or \
                   self.room_obj_lst[(room_number-1)].center == "D":

                    print(f"4. Attack {self.parse_entity_string({c_str})}"
                          + " to the center")
                else:
                    print(f"4. Pickup {self.parse_entity_string({c_str})}"
                          + " to the center")
            else:
                print("4. go center of the room")

            print("5. go south and exit room")

            data_str = input("Choose an option:\n")
            while not validate_enter_room_choice_data(data_str):
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
        This function moves the player to the north, south, east
        or west if there is a dragon it does and attack_dragon
        function
        if there is a power up that that is picked up via the
        pickup_entity function

        Args:
            option (int) 1 to 4 N,E,W,C
            room_number (int)
        """

        if option == 1:  # north
            if self.room_obj_lst[(room_number-1)].north != Room.wall:
                if self.room_obj_lst[(room_number-1)].north == "d" or\
                   self.room_obj_lst[(room_number-1)].north == "D":

                    self.attack_dragon(room_number, "north")
                else:
                    self.pickup_entity(room_number, "north")
        elif option == 2:  # east
            if self.room_obj_lst[(room_number-1)].east != Room.wall:
                if self.room_obj_lst[(room_number-1)].east == "d" or\
                   self.room_obj_lst[(room_number-1)].east == "D":

                    self.attack_dragon(room_number, "east")
                else:
                    self.pickup_entity(room_number, "east")
        elif option == 3:  # west
            if self.room_obj_lst[(room_number-1)].west != Room.wall:
                if self.room_obj_lst[(room_number-1)].west == "d" or\
                   self.room_obj_lst[(room_number-1)].west == "D":

                    self.attack_dragon(room_number, "west")
                else:
                    self.pickup_entity(room_number, "west")
        elif option == 4:  # center
            if self.room_obj_lst[(room_number-1)].center != Room.center:
                if self.room_obj_lst[(room_number-1)].center == "d" or\
                   self.room_obj_lst[(room_number-1)].center == "D":

                    self.attack_dragon(room_number, "center")
                else:
                    self.pickup_entity(room_number, "center")

    def pickup_entity(self, room_number, direction):
        """
        This function pickups the weapons and health based on direction

        Args:
            room_number (int)
            direction (int) N,E,W,C
        """

        n_str = self.room_obj_lst[(room_number-1)].north
        e_str = self.room_obj_lst[(room_number-1)].east
        w_str = self.room_obj_lst[(room_number-1)].west
        c_str = self.room_obj_lst[(room_number-1)].center

        if direction == "north":
            if self.room_obj_lst[(room_number-1)].north == "H":

                self.player_health = 100
            else:
                player_weapons_list.append(n_str)
            print("Pickedup:" + self.parse_entity_string(n_str))

        elif direction == "east":
            if self.room_obj_lst[(room_number-1)].east == "H":

                self.player_health = 100
            else:
                player_weapons_list.append(e_str)
            print("Pickedup:" + self.parse_entity_string(e_str))

        elif direction == "west":
            if self.room_obj_lst[(room_number-1)].west == "H":
                self.player_health = 100
            else:
                player_weapons_list.append(w_str)
            print("Pickedup:" + self.parse_entity_string(w_str))

        elif direction == "center":
            if self.room_obj_lst[(room_number-1)].center == "H":
                self.player_health = 100
            else:
                player_weapons_list.append(c_str)
            print("Pickedup:" + self.parse_entity_string(c_str))

        print("Contents of you weapons list:")
        print(player_weapons_list)
        self.remove_entity(room_number, direction)

    def attack_dragon(self, room_number, direction):
        """
        This function acks as a finite state machine a basic one to attack a
        dragon and based on the weapons the player has the health is adjusted
        based on rules in the finite state machine

        Args:
            room_number (int)
            direction (string) north, east, west,center

        """

        if "S" in player_weapons_list and "W" in player_weapons_list:

            print(f"Dragon slayed you have {self.player_health} health")
            self.numberof_dragons = self.numberof_dragons - 1

            self.remove_entity(room_number, direction)

        elif "S" in player_weapons_list and "w" in player_weapons_list:
            self.player_health = self.player_health - 15
            if self.player_health > 0:
                print(f"Dragon slayed you have {self.player_health} health")
                self.numberof_dragons = self.numberof_dragons - 1
            else:
                print("Player killed by Dragon")

            self.remove_entity(room_number, direction)

        elif "s" in player_weapons_list and "W" in player_weapons_list:
            self.player_health = self.player_health - 25
            if self.player_health > 0:
                print(f"Dragon slayed you have {self.player_health} health")
                self.numberof_dragons = self.numberof_dragons - 1
            else:
                print("Player killed by Dragon")
            self.remove_entity(room_number, direction)

        elif "s" in player_weapons_list and "w" in player_weapons_list:
            self.player_health = self.player_health - 50
            if self.player_health > 0:
                print(f"Dragon slayed you have {self.player_health} health")
                self.numberof_dragons = self.numberof_dragons - 1
            else:
                print("Player killed by Dragon")

            self.remove_entity(room_number, direction)
        else:  # player dies
            self.player_health = 0
            print("-"*40)
            print("Game Over the player was killed by Dragon")
            end_time = time.time()
            durationof_game = end_time - self.start_time
            durationof_game = format(durationof_game, ".2f")
            print(f"You lasted:{durationof_game}")
            print("Play Again?")
            print("-"*40)
            get_enter_replay_choice_menu()

        if self.player_health <= 0:
            print("-"*40)
            print("Game Over the player was killed by Dragon")
            end_time = time.time()
            durationof_game = end_time - self.start_time
            durationof_game = format(durationof_game, ".2f")
            print(f"You lasted:{durationof_game}")
            print("Play Again?")
            print("-"*40)
            get_enter_replay_choice_menu()

        if self.numberof_dragons == 0:
            print("-"*40)
            print("Game Over you killed all the Dragons")
            end_time = time.time()
            durationof_game = end_time - self.start_time
            durationof_game = format(durationof_game, ".2f")
            print(f"You took {durationof_game} to play the game. Well done!!")
            print("Play Again?")
            print("-"*40)
            get_enter_replay_choice_menu()

    def remove_entity(self, room_number, direction):
        """
        This function sets the directions to room.wall and if
        the direction is center it is set to room.center

        Args:
            room_number (int)
            direction (string) north, east, west, center
        """

        if direction == "north":
            self.room_obj_lst[(room_number-1)].north = Room.wall
        elif direction == "east":
            self.room_obj_lst[(room_number-1)].east = Room.wall
        elif direction == "west":
            self.room_obj_lst[(room_number-1)].west = Room.wall
        elif direction == "center":
            self.room_obj_lst[(room_number-1)].center = Room.center

    def show_entities_in_room(self, room_number):
        """
        This function detects if the room is empty and prints a room empty
        message it also shows a message showing the entities in the room
        based on direction

        Args:
            room_number (int)
        """

        n_str = str(self.room_obj_lst[(room_number-1)].north)
        e_str = str(self.room_obj_lst[(room_number-1)].east)
        w_str = str(self.room_obj_lst[(room_number-1)].west)
        c_str = str(self.room_obj_lst[(room_number-1)].center)

        if self.room_obj_lst[(room_number-1)].north == Room.wall and\
           self.room_obj_lst[(room_number-1)].east == Room.wall and\
           self.room_obj_lst[(room_number-1)].west == Room.wall and\
           self.room_obj_lst[(room_number-1)].center == Room.center:

            print("* Room is empty")
        else:
            if self.room_obj_lst[(room_number-1)].north != Room.wall:
                print("* To the north there is a "
                      + f"{self.parse_entity_string({n_str})}")

            if self.room_obj_lst[(room_number-1)].east != Room.wall:
                print("* To the east there is a "
                      + f"{self.parse_entity_string({e_str})}")

            if self.room_obj_lst[(room_number-1)].west != Room.wall:
                print("* To the west there is a "
                      + f"{self.parse_entity_string({w_str})}")

            if self.room_obj_lst[(room_number-1)].center != Room.center:
                print("* To the center of the room there is a "
                      + f"{self.parse_entity_string({c_str})}")

    def parse_entity_string(self, entity_string):
        """
        This function parses an entity string and returns a description
        string in english

        Args:
            entity_string (string) a character to be translated to english
            entity_string can be a sinlge set item
        """

        if 'd' in entity_string:
            return "little dragon"
        elif 'D' in entity_string:
            return "big dragon"
        elif 's' in entity_string:
            return "little shield"
        elif 'S' in entity_string:
            return "big shield"
        elif 'w' in entity_string:
            return "little sword"
        elif 'W' in entity_string:
            return "long sword"
        elif 'H' in entity_string:
            return "meddiepack"
        elif entity_string == 'd':
            return "little dragon"
        elif entity_string == 'D':
            return "big dragon"
        elif entity_string == 's':
            return "little shield"
        elif entity_string == 'S':
            return "big shield"
        elif entity_string == 'w':
            return "little sword"
        elif entity_string == 'W':
            return "long sword"
        elif entity_string == 'H':
            return "meddiepack"
        else:
            print(f"Error:{entity_string}")


def get_enter_replay_choice_menu():
    """
    This function gets the user input and validates it
    if the user enter 2 the game is ended.
    """
    print("\n1. Play Again \t\t 2. Exit Game\n\n")
    data_str = input("Enter option:\n")

    if validate_enter_replay_choice_data(data_str):
        # enter room and display options
        if int(data_str) == 2:  # Exit game
            sys.exit()

        del player_weapons_list[:]
        main()

    else:
        get_enter_replay_choice_menu()


def validate_enter_dungeon_choice_data(value):
    """
    This function validates the user input for the dungeon room choice dialog
    if the value chosen is not between 1 and 13 then a message is displayed
    also if the value is not an integer a message is displayed

    Args:
        value (string)

    return:
         True if all goes well or False if there is exception thrown
    """

    try:
        val = int(value)
        if not (val >= 1 and val <= 13):
            raise ValueError()
    except ValueError:
        print("Invalid choice: You must enter a Number between 1 and 13,"
              + "please try again.\n")
        return False

    return True


def validate_enter_replay_choice_data(value):
    """
    This function validates the options
    if the value is not between 1 and 2 a message is diplayed
    also if the value is not an integer a message is displayed

    Args:
        value (string)

    return:
        True if all goes well or False if there is exception thrown
    """
    try:
        val = int(value)
        if not (val >= 1 and val <= 2):
            raise ValueError()
    except ValueError:
        print("Invalid choice:You must enter a number between 1 and 2, \
            please try again.\n")
        return False

    return True


def validate_enter_room_choice_data(value):
    """
    This function validates the options when in a room
    if the value is not between 1 and 5 a message is diplayed
    also if the value is not an integer a message is displayed

    Args:
        value (string)

    return:
        True if all goes well or False if there is exception thrown
    """

    try:
        val = int(value)
        if not (val >= 1 and val <= 5):
            raise ValueError()
    except ValueError:
        print("Invalid choice:You must enter a number between 1 and 5, \
            please try again.\n")
        return False

    return True


def validate_intro_choice_data(value):
    """
    This function validates the intro input data
    if the value is not between 1 and 3 a error
    message is displayed and if the value is
    not a number an error message is displayed

    Args:
        value (string)

    return:
        True if all goes well or False if there is exception thrown
    """

    try:
        val = int(value)
        if not (val >= 1 and val <= 3):
            raise ValueError()
    except ValueError:
        print("Invalid choice: You mush enter a Number either 1 or 3!, \
            please try again.\n")
        return False

    return True


def display_intro():
    """
    This function displays the intro screen
    """

    print("Welcome to my Dungeon")
    print("You have entered an era of dragons")
    print("")
    print("To play the game use the numbers on the menu of items and")
    print("when asked for a choice enter one and press enter")

    print("The goal of this game is to kill all the dragons in the")
    print("least amount of time")
    print("HINT: You need a sword and a shield to kill a dragon")
    print("or you'll be toast!")
    print("\n\n")
    print("1. play Game \t 2. How To Play Game")
    print("3. Exit Game")
    print("\n\n")
    print("To play the game choose 1 or 3 to exit")


def get_intro_input():
    """
    This function is to get the input from the introduction
    screen
    """

    data_str = input("Enter option:\n")

    if validate_intro_choice_data(data_str):
        if int(data_str) == 3:
            sys.exit()
        elif int(data_str) == 2:
            display_howto_play_game()
        else:
            main()
    else:
        get_intro_input()


def display_howto_play_game():
    """
    This function prints a message to the screen
    """

    output_str = """
    When the user enters the game they are given options via text based\n \
    forms where the options are shown via a output to the console you\n \
    choose a number type it and then press enter and the menu will take\n \
    you to that option When you play the game a list of Rooms is shown\n \
    where you have to chooose one via entering a number and pressing enter\n \
    based on your choice you will be taken to a Room with a Number and in\n \
    this Room you will have 5 options to go north or Pickup/Attack an\n \
    entity. To go east to pickup/Attack an entity. To go west and \n \
    Pickup/Attack an entity. To go to center of Room and Pickup/Attack\n \
    an entity. And lasly an option to go south and exit the Room. On each\n \
    option there is a number and the player will choose the option by \n \
    entering the number and pressing return.
    """

    print(output_str)

    input("Press Enter to continue:\n")
    display_intro()
    get_intro_input()


def main():
    """
    This is the main function it setsup the dungeon
    and adds entities to the dungeon rooms
    and starts the choice menuing
    """
    dungeon = Dungeon(12)

    # display an empty Dungeon
    dungeon.show_dungeon_plan()

    # d is a small dragon a D is a big dragon
    listof_dragons_inrooms = ["d", "d", "d", "d", "d", "d", "D", "D", "D"]
    # s is a small shield and a S is a large shield, a w is a small sword
    # and a W is a large sword
    listof_weapons_inrooms = ["s", "S", "S", "w", "W", "W"]
    # H is a medie pack when picked up restores the players health
    listof_medipacks_inrooms = ["H", "H", "H"]

    dungeon.add_objects_to_rooms(listof_dragons_inrooms,
                                 listof_weapons_inrooms,
                                 listof_medipacks_inrooms)

    dungeon.show_dungeon_plan_with_entities()

    dungeon.enter_dungeon_choice()


# These 2 functions display the introduction screen and get a choice
# the get_intro_input function can call main

display_intro()
get_intro_input()

import random
# PP3 project by Michael Cloran
#1/2/2024
"""
This is a basic single user Dungeon game
"""

class Room:
    """The Room class is to create and manage the Room
    Note when you walk into a room you are at the door
    and the door is south the far wall is north and to the left and right west and east"""
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
    """The Dungeon class is to create and manage the dungeon"""
    
    def create_rooms(self,number_of_rooms):
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
        and thus does a recursive call to another random room and random position
        """
        randomRoomValue = random.randint(0, (11))#12 rooms
        randomPosition = random.randint(1,4) # 1 north, 2 east, 3 west, 4 center remember south is a door
        
        if randomPosition == 1:#north
            if self.roomObjList[randomRoomValue].north != Room.wall:
                self.get_random_position_in_random_room()
            else:
                return [randomRoomValue, randomPosition]
                
        elif randomPosition == 2:#east
            if self.roomObjList[randomRoomValue].east != Room.wall:
                self.get_random_position_in_random_room()
            else:
                return [randomRoomValue, randomPosition]

        elif randomPosition == 3:#west
            if self.roomObjList[randomRoomValue].west != Room.wall:
                self.get_random_position_in_random_room()
            else:
                return [randomRoomValue, randomPosition]

        elif randomPosition == 4:#center
            if self.roomObjList[randomRoomValue].center != Room.center:
                self.get_random_position_in_random_room()
            else:
                return [randomRoomValue, randomPosition]

    def __init__(self,number_of_rooms):# Dungeon class constructor
        self.number_of_rooms = number_of_rooms
        self.roomObjList = []
        self.create_rooms(number_of_rooms)
        self.listOfEntitiesInRooms = []

    def add_objects_to_rooms(self, listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms):
        """
        Goes through a for look to loop 18 times which is the amount of entities to be added to the game level
        firstly get_random_position_in_random_room is called to get random room and random position
        the a random entity is got and based on the random position and random room the entity is added
        to the random room at random position
        """
        for x in range( (len(listOfDragonsInRooms)+len(listOfWeaponssInRooms)+len(listOfMediPacksInRooms))):#remember only 18 entities for this simulation so get_random_position_in_randon_room will be called 18 times
            randomValues = self.get_random_position_in_random_room()
            while randomValues == None:
                randomValues = self.get_random_position_in_random_room()

            randomRoomValue = randomValues[0]
            randomPosition = randomValues[1]
            
            randomEntity = self.get_random_entity(listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms)

            if randomPosition == 1: #north
                self.roomObjList[randomRoomValue].north = randomEntity
            elif randomPosition == 2:#east
                self.roomObjList[randomRoomValue].east = randomEntity
            elif randomPosition == 3: #west
                self.roomObjList[randomRoomValue].west = randomEntity
            elif randomPosition == 4: #center
                self.roomObjList[randomRoomValue].center = randomEntity

        
    def get_random_entity(self,listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms):
        """
        The listOfEntitiesInRooms contains a list of entities to be added to the game 
        a random entity is picked from the list and that entity is removed from the listOfEntitiesInRooms
        the random entity is returned
        """

        #rememeber the dungeon only has 12 Rooms 18 entities
        if len(self.listOfEntitiesInRooms) == 0:
            self.listOfEntitiesInRooms = listOfDragonsInRooms + listOfWeaponssInRooms+ listOfMediPacksInRooms
        
        randomInteger = random.randint(0, (len(self.listOfEntitiesInRooms)-1) )
        strToReturn = self.listOfEntitiesInRooms[randomInteger]

        del self.listOfEntitiesInRooms[randomInteger]
        #self.listOfEntitiesInRooms.pop(randomInteger)
        
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
        for x in range(6):# number of rooms over 2
            for i in range(5):
                if i == 2:
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
        Loops through floor plan and shows the entities for the game level
        """
        print("\nCheat Dungeon plan\nThe ! is a door and d little dragon and D big Dragon\ns for little shield and S for big shield\nw for little sword and W for big sword\nH for medi pack\n")        
        print("Dungeon Plan")
        str1 = '-'
        str2 = "|"
        str3 = "!"
        strMainWall = str1 * 19
        spce = ' '
        print(strMainWall)
        
        for x in range(6):# number of rooms over 2
            for i in range(5):
                floorPlanStr = ""
                if i == 0:
                    if x == 0:#room 1 and 2
                        print(self.get_floor_plan_edges_string(0, 1, "east"))
                    elif x == 1:#room 3 and 4
                        print(self.get_floor_plan_edges_string(2, 3, "east"))
                    elif x == 2:#room 5 and 6
                        print(self.get_floor_plan_edges_string(4, 5, "east"))
                    elif x == 3:#room 7 and 8
                        print(self.get_floor_plan_edges_string(6, 7, "east"))
                    elif x == 4:#room 9 and 10
                        print(self.get_floor_plan_edges_string(8, 9, "east"))
                    elif x == 5:#room 11 and 12
                        print(self.get_floor_plan_edges_string(10, 11, "east"))

                elif i == 2:
                    if x == 0:#room 1 and 2 middle on door
                        print(self.get_floor_plan_middle_string(0,1))
                    elif x == 1:#room 3 and 4 middle on door
                        print(self.get_floor_plan_middle_string(2,3))
                    elif x == 2:#room 5 and 6 middle on door
                        print(self.get_floor_plan_middle_string(4,5))
                    elif x == 3:#room 7 and 8 middle on door
                        print(self.get_floor_plan_middle_string(6,7))
                    elif x == 4:#room 9 and 10 middle on door
                        print(self.get_floor_plan_middle_string(8,9))
                    elif x == 5:# room 11 and 12 middle on door
                        print(self.get_floor_plan_middle_string(10,11))
                    
                elif i == 4:
                    if x == 0:#room 1 and 2
                        print(self.get_floor_plan_edges_string(0, 1, "west"))
                    elif x == 1:#room 3 and 4
                        print(self.get_floor_plan_edges_string(2, 3, "west"))
                    elif x == 2:#room 5 and 6
                        print(self.get_floor_plan_edges_string(4, 5, "west"))
                    elif x == 3:#room 7 and 8
                        print(self.get_floor_plan_edges_string(6, 7, "west"))
                    elif x == 4:#room 9 and 10
                        print(self.get_floor_plan_edges_string(8, 9, "west"))
                    elif x == 5:#room 11 and 12
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
            #room1
            if self.roomObjList[roomIndex1].east != 1:
                floorPlanStr = floorPlanStr + str2 + spce*2 + self.roomObjList[roomIndex1].east + spce*2 + str2
            else:
                floorPlanStr = floorPlanStr + str2 + spce*5 + str2  
                
            #put in corridore 
            floorPlanStr = floorPlanStr + spce*5

            #room2
            if self.roomObjList[roomIndex2].east != 1:
                floorPlanStr = floorPlanStr +  str2 + spce*2 + self.roomObjList[roomIndex2].east + spce*2 + str2
            else:
                floorPlanStr = floorPlanStr  + str2 + spce*5 + str2
        
        elif direction == "west":
            #room1
            if self.roomObjList[roomIndex1].west != 1:
                floorPlanStr = floorPlanStr + str2 + spce*2 + self.roomObjList[roomIndex1].west + spce*2 + str2
            else:
                floorPlanStr = floorPlanStr + str2 + spce*5 + str2 
                
            #put in corridore 
            floorPlanStr = floorPlanStr + spce*5

            #room2
            if self.roomObjList[roomIndex2].west != 1:
                floorPlanStr = floorPlanStr +  str2 + spce*2 + self.roomObjList[roomIndex2].west + spce*2 + str2
            else:
                floorPlanStr = floorPlanStr + str2 + spce*5 + str2
        
        return floorPlanStr

    def get_floor_plan_middle_string(self,roomIndex1, roomIndex2):
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
        #room 1
        if self.roomObjList[roomIndex1].north != 1:
            floorPlanStr = floorPlanStr + str2 + self.roomObjList[roomIndex1].north
        else:
            floorPlanStr = floorPlanStr + str2 +spce  
                            
        if self.roomObjList[roomIndex1].center != 2:
            floorPlanStr = floorPlanStr + spce*2+ self.roomObjList[roomIndex1].center +spce + str3 + str(roomIndex1+1)
        else:
            floorPlanStr = floorPlanStr  +spce*4 + str3 + str(roomIndex1+1)
            
            
        #put in corridore 
        if roomIndex2 != 9 and roomIndex2 != 11 and roomIndex2 != 10:
            floorPlanStr = floorPlanStr + spce*3
        elif roomIndex2 == 11:
            floorPlanStr = floorPlanStr + spce
        else:
            floorPlanStr = floorPlanStr + spce*2

        #room2
        if self.roomObjList[roomIndex2].center != 2:
            floorPlanStr = floorPlanStr + str(roomIndex2+1) + str3 + spce*2 + self.roomObjList[roomIndex2].center
            
        else:
            floorPlanStr = floorPlanStr + str(roomIndex2+1) + str3 + spce*3

        if self.roomObjList[roomIndex2].north != 1:
            floorPlanStr = floorPlanStr  +spce + self.roomObjList[roomIndex2].north   + str2
        else:
            floorPlanStr = floorPlanStr + spce*2 + str2
            
        return floorPlanStr        

def  enter_dungeon_choice():
    data_str = 0
    while data_str != 13:
        print("*"*30)
        print("* Welcome to my Dungeon")
        print("* May you conquer and reap the benefits")
        print("* Enter the rooms amd slay the dragons")
        print("* Pickup health and weapons as you go")
        print("*"*20)
        print("*")
        print("* Menu")
        print("* Choose a room to goto")
        print("*"*20)

        print("1. Room 1")
        print("2. Room 2")
        print("3. Room 3")
        print("4. Room 4")
        print("5. Room 5")

        print("6. Room 6")
        print("7. Room 7")
        print("8. Room 8")
        print("9. Room 9")
        print("10. Room 10")

        print("11. Room 11")
        print("12. Room 12")

        print("13. Exit Game")
        print("\nChoose an option 1 to 13")

        data_str = input("Choose an option:\n")

        if(validate_enter_dungeon_choice_data(data_str)):
            print("valid input")
            #enter room and display options
            if int(data_str) == 13:
                break
            

def validate_enter_dungeon_choice_data(value):

    try:
        val = int(value)
        if not (val >= 1 and val <= 13):
            raise ValueError(f"You must enter an Integer value 1 to 13 you entered {val}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

def main():
    dungeon = Dungeon(12)

    """
    display an empty Dungeon
    """
    dungeon.show_dungeon_plan()

    # d is a small dragon a D is a big dragon
    listOfDragonsInRooms = ["d","d","d","d","d","d","D","D","D"]
    # s is a small shield and a S is a large shield, a w is a small sword
    # and a W is a large sword
    listOfWeaponssInRooms = ["s","S","S","w","W","W"]
    # H is a medie pack when picked up restores the players health
    listOfMediPacksInRooms = ["H","H","H"]

    dungeon.add_objects_to_rooms(listOfDragonsInRooms,listOfWeaponssInRooms,listOfMediPacksInRooms)         

    dungeon.show_dungeon_plan_with_entities()
    
    enter_dungeon_choice()


print("Welcome to my Dungeon")
main()
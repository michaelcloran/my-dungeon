import random
# PP3 project by Michael Cloran
#1/2/2024
"""
This si a basic single user Dungeon game
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

    def add_entity(self,randomPosition, listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms):
        if randomPosition == 1:#north
            self.north == Dungeon.get_random_entity(listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms)
        elif randomPosition == 2:#east
            self.east == Dungeon.get_random_entity(listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms)
        elif randomPosition == 3:#west
            self.west == Dungeon.get_random_entity(listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms)
        elif randomPosition == 4:#center
            self.center == Dungeon.get_random_entity(listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms)

class Dungeon:
    """The Dungeon class is to create and manage the dungeon"""
    roomObjList = []
    listOfEntitiesInRooms = []

    def create_rooms(self,number_of_rooms):
    
        for x in range(number_of_rooms):
            roomObj = Room()
            Dungeon.roomObjList.append(roomObj)

    def __init__(self,number_of_rooms):
        self.number_of_rooms = number_of_rooms
        self.create_rooms(number_of_rooms)

    

    def add_objects_to_rooms(self, listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms):

        for x in range( (len(listOfDragonsInRooms)+len(listOfWeaponssInRooms)+len(listOfMediPacksInRooms))-1):#remember only 18 entities for this simulation so get_random_position_in_randon_room will be called 18 times
            randomRoomValue, randomPosition = Dungeon.get_random_position_in_random_room()
            
            Dungeon.roomObjList[randomRoomValue].add_entity(randomPosition, listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms)


    def get_random_entity(listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms):
        #rememeber the dungeon only has 12 Rooms
        if(len(Dungeon.listOfEntitiesInRooms) == 0):
            Dungeon.listOfEntitiesInRooms = listOfDragonsInRooms + listOfWeaponssInRooms+ listOfMediPacksInRooms
        
        randomInteger = random.randint(0, (len(Dungeon.listOfEntitiesInRooms)-1) )
        strToReturn = Dungeon.listOfEntitiesInRooms[randomInteger]
        Dungeon.listOfEntitiesInRooms.pop(randomInteger)
        return strToReturn
    
    def get_random_position_in_random_room():
        randomRoomValue = random.randint(0, (len(Dungeon.roomObjList)-1))
        randomPosition = random.randint(1,4) # 1 north, 2 east, 3 west, 4 center remember south is a door
        
        if randomPosition == 1:#north
            if Dungeon.roomObjList[randomRoomValue].north != Room.wall:
                get_random_position_in_random_room()
            else:
                return randomRoomValue, randomPosition
                
        elif randomPosition == 2:#east
            if Dungeon.roomObjList[randomRoomValue].east != Room.wall:
                get_random_position_in_random_room()
            else:
                return randomRoomValue, randomPosition

        elif randomPosition == 3:#west
            if Dungeon.roomObjList[randomRoomValue].west != Room.wall:
                get_random_position_in_random_room()
            else:
                return randomRoomValue, randomPosition

        elif randomPosition == 4:#center
            if Dungeon.roomObjList[randomRoomValue].center != Room.center:
                get_random_position_in_randon_room()
            else:
                return randomRoomValue, randomPosition

    def show_dungeon_plan(self):
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



print("Welcome to my Dungeon")
main()
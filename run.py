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
        self.north = wall
        self.south = door
        self.east = wall
        self.west = wall
        self.center = center

    def add_entity(self,randomPosition, listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms):
        if randomPosition == 1:#north
            self.north == get_random_entity(listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms)
        elif randomPosition == 2:#east
            self.east == get_random_entity(listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms)
        elif randomPosition == 3:#west
            self.west == get_random_entity(listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms)
        elif randomPosition == 4:#center
            self.center == get_random_entity(listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms)

class Dungeon:
    """The Dungeon class is to create and manage the dungeon"""
    roomObjList = []
    listOfEntitiesInRooms = []

    def __init__(self,number_of_rooms):
        self.number_of_rooms = number_of_rooms
        create_rooms(self.number_of_rooms)

    def create_rooms(number_of_rooms):

        for x in range(number_of_rooms):
            roomObj = Room()
            roomObjList.append(roomObj)

    def add_objects_to_rooms(self, listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms):

        for x in range(len(self.listOfEntitiesInRooms)):#remember only 18 entities for this simulation so get_random_position_in_randon_room will be called 18 times
            randomRoomValue, randomPosition = get_random_position_in_randon_room()
            
            roomObjList[randomRoomValue].add_entity(randomPosition, listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms)


    def get_random_entity(listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms):
        #rememeber the dungeon only has 12 Rooms
        if(len(self.listOfEntitiesInRooms) == 0):
            self.listOfEntitiesInRooms = listOfDragonsInRooms + listOfWeaponssInRooms+ listOfMediPacksInRooms
        
        randomInteger = random.randint(0, (len(listOfEntitiesInRooms)-1) )
        strToReturn = self.listOfEntitiesInRooms[randomInteger]
        self.listOfEntitiesInRooms.pop(randomInteger)
        return strToReturn
    
    def get_random_position_in_randon_room():
        randomRoomValue = random.randint(0, (len(roomObjList)-1))
        randomPosition = random.randint(1,4) # 1 north, 2 east, 3 west, 4 center remember south is a door
        
        if randomPosition == 1:#north
            if roomObjList[randomRoomValue].north != Room.wall:
                get_random_position_in_randon_room()
            else:
                return randomRoomValue, randomPosition
                
        elif randomPosition == 2:#east
            if roomObjList[randomRoomValue].east != Room.wall:
                get_random_position_in_randon_room()
            else:
                return randomRoomValue, randomPosition

        elif randomPosition == 3:#west
            if roomObjList[randomRoomValue].west != Room.wall:
                get_random_position_in_randon_room()
            else:
                return randomRoomValue, randomPosition

        elif randomPosition == 4:#center
            if roomObjList[randomRoomValue].center != Room.center:
                get_random_position_in_randon_room()
            else:
                return randomRoomValue, randomPosition
                
def main():
    dungeon = Dungeon(12)

    # a d is a small dragon a D is a big dragon
    listOfDragonsInRooms = ["d","d","d","d","d","d","D","D","D"]
    # a s is a small shield and a S is a large shield, a w is a small sword
    # and a W is a large sword
    listOfWeaponssInRooms = ["s","S","S","w","W","W"]
    #a H is a medie pack when picked up restores the players health
    listOfMediPacksInRooms = ["H","H","H"]

    dungeon.add_objects_to_rooms(listOfDragonsInRooms,listOfWeaponssInRooms,listOfMediPacksInRooms)         



print("Welcome to my Dungeon")
main()
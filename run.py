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
        self.listOfEntitiesInRooms = []
        self.roomNumber = 0

    def add_entity(self,randomPosition, listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms):
        randomEntity = ""
        print("randomPosition:"+str(randomPosition))
        if randomPosition == 1: #north
            randomEntity = self.get_random_entity(listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms)
            return  randomEntity
        elif randomPosition == 2:#east
            randomEntity = self.get_random_entity(listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms)
            return  randomEntity
        elif randomPosition == 3:#west
            randomEntity = self.get_random_entity(listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms)
            return  randomEntity
        elif randomPosition == 4:#center
            randomEntity = self.get_random_entity(listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms)
            return  randomEntity

    def get_random_entity(self,listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms):
        #rememeber the dungeon only has 12 Rooms
        if(len(self.listOfEntitiesInRooms) == 0):
            self.listOfEntitiesInRooms = listOfDragonsInRooms + listOfWeaponssInRooms+ listOfMediPacksInRooms
        
        randomInteger = random.randint(0, (len(self.listOfEntitiesInRooms)-1) )
        strToReturn = self.listOfEntitiesInRooms[randomInteger]
        self.listOfEntitiesInRooms.pop(randomInteger)
        print("strToReturn:"+strToReturn)
        return strToReturn

class Dungeon:
    """The Dungeon class is to create and manage the dungeon"""
    #roomObjList = []
    #listOfEntitiesInRooms = []

    def create_rooms(self,number_of_rooms):
    
        for x in range(number_of_rooms):
            roomObj = Room()
            roomObj.roomNumber = (x+1)
            self.roomObjList.append(roomObj)

    def get_random_position_in_random_room(self):
        
        randomRoomValue = random.randint(0, (12-1))#12 rooms
        randomPosition = random.randint(1,4) # 1 north, 2 east, 3 west, 4 center remember south is a door
        
        print("randomRoomValue:"+str(randomRoomValue)+" randomPosition:"+str(randomPosition))

        if randomPosition == 1:#north
            if self.roomObjList[randomRoomValue].north != Room.wall:
                print("already entity at north")
                self.get_random_position_in_random_room()
            else:
                print("north randomRoomValue:"+str(randomRoomValue)+" randomPosition:"+str(randomPosition))
                return randomRoomValue, randomPosition
                
        elif randomPosition == 2:#east
            if self.roomObjList[randomRoomValue].east != Room.wall:
                print("already entity at east")
                self.get_random_position_in_random_room()
            else:
                print("east randomRoomValue:"+str(randomRoomValue)+" randomPosition:"+str(randomPosition))
                return randomRoomValue, randomPosition

        elif randomPosition == 3:#west
            if self.roomObjList[randomRoomValue].west != Room.wall:
                print("already entity at west")
                self.get_random_position_in_random_room()
            else:
                print("west randomRoomValue:"+str(randomRoomValue)+" randomPosition:"+str(randomPosition))
                return randomRoomValue, randomPosition

        elif randomPosition == 4:#center
            if self.roomObjList[randomRoomValue].center != Room.center:
                print("already entity at center")
                self.get_random_position_in_random_room()
            else:
                print("center randomRoomValue:"+str(randomRoomValue)+" randomPosition:"+str(randomPosition))
                return randomRoomValue, randomPosition

    def get_random_position(self,randomRoomValue):
                
        randomPosition = random.randint(1,4) # 1 north, 2 east, 3 west, 4 center remember south is a door
        
        print("randomRoomValue:"+str(randomRoomValue)+" randomPosition:"+str(randomPosition))

        if randomPosition == 1:#north
            if self.roomObjList[randomRoomValue].north != Room.wall:
                print("already entity at north")
                self.get_random_position_in_random_room()
            else:
                print("north randomRoomValue:"+str(randomRoomValue)+" randomPosition:"+str(randomPosition))
                return randomPosition
                
        elif randomPosition == 2:#east
            if self.roomObjList[randomRoomValue].east != Room.wall:
                print("already entity at east")
                self.get_random_position_in_random_room()
            else:
                print("east randomRoomValue:"+str(randomRoomValue)+" randomPosition:"+str(randomPosition))
                return randomPosition

        elif randomPosition == 3:#west
            if self.roomObjList[randomRoomValue].west != Room.wall:
                print("already entity at west")
                self.get_random_position_in_random_room()
            else:
                print("west randomRoomValue:"+str(randomRoomValue)+" randomPosition:"+str(randomPosition))
                return randomPosition

        elif randomPosition == 4:#center
            if self.roomObjList[randomRoomValue].center != Room.center:
                print("already entity at center")
                self.get_random_position_in_random_room()
            else:
                print("center randomRoomValue:"+str(randomRoomValue)+" randomPosition:"+str(randomPosition))
                return randomPosition


    def __init__(self,number_of_rooms):
        self.number_of_rooms = number_of_rooms
        self.roomObjList = []
        self.create_rooms(number_of_rooms)
        self.listOfEntitiesInRooms = []

    def add_objects_to_rooms(self, listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms):

        for x in range( (len(listOfDragonsInRooms)+len(listOfWeaponssInRooms)+len(listOfMediPacksInRooms))-1):#remember only 18 entities for this simulation so get_random_position_in_randon_room will be called 18 times
            #print("RV:RP:"+str(self.get_random_position_in_random_room()))
            randomRoomValue = random.randint(0, (12-1))#12 rooms
            randomPosition = self.get_random_position(randomRoomValue)
            while randomPosition == None:
                randomPosition = self.get_random_position(randomRoomValue)
            
            print("add_objects_to_roomms randomPosition:"+str(randomPosition))

            #self.roomObjList[randomRoomValue].add_entity(randomPosition, listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms)
            randomEntity = self.roomObjList[randomRoomValue].add_entity(randomPosition, listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms)
            print("randomEntity:"+randomEntity)
            if randomPosition == 1: #north
                self.roomObjList[randomRoomValue].north = randomEntity
            elif randomPosition == 2:#east
                self.roomObjList[randomRoomValue].east = randomEntity
            elif randomPosition == 3: #west
                self.roomObjList[randomRoomValue].west = randomEntity
            elif randomPosition == 4: #center
                self.roomObjList[randomRoomValue].center = randomEntity

    def get_random_entity(self,listOfDragonsInRooms, listOfWeaponssInRooms, listOfMediPacksInRooms):
        #rememeber the dungeon only has 12 Rooms
        if(len(self.listOfEntitiesInRooms) == 0):
            self.listOfEntitiesInRooms = listOfDragonsInRooms + listOfWeaponssInRooms+ listOfMediPacksInRooms
        
        randomInteger = random.randint(0, (len(self.listOfEntitiesInRooms)-1) )
        strToReturn = self.listOfEntitiesInRooms[randomInteger]
        self.listOfEntitiesInRooms.pop(randomInteger)
        return strToReturn
    
    

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

    def show_dungeon_plan_with_entities(self):
        print("Cheat Dungeon planan\nThe ! is a door and d little dragon and D big Dragon\ns for little shield and S for big shield\nw for little sword and W for big sword\nH for medi pack\n")        
        print("Dungeon Plan")
        str1 = '-'
        str2 = "|"
        str3 = "!"
        strMainWall = str1 * 19
        spce = ' '
        print(strMainWall)

        for obj in self.roomObjList:
            print("RoomObjList")
            print("N:"+str(obj.north))
            print("E:"+str(obj.east))
            print("W:"+str(obj.west))
            print("C:"+str(obj.center))
            
        print("End RoomObjList")

        for x in range(6):# number of rooms over 2
            for i in range(5):
                floorPlanStr = ""
                if i == 2:
                    if x == 0:
                        #room 1
                        if self.roomObjList[0].north != 1:
                            floorPlanStr = floorPlanStr + str2 + self.roomObjList[0].north
                        else:
                            floorPlanStr = floorPlanStr + str2 + spce*5 + str3 + "1" 
                        
                        if self.roomObjList[0].center != 2:
                            floorPlanStr = floorPlanStr + self.roomObjList[0].center + spce*2 + str3
                        else:
                            floorPlanStr = floorPlanStr + spce*3


                        #put in corridore 
                        floorPlanStr = floorPlanStr + spce*5
                        #room2
                        if self.roomObjList[1].center != 2:
                            floorPlanStr = floorPlanStr + str3 + spce + self.roomObjList[1].center + spce
                        else:
                            floorPlanStr = floorPlanStr + "2" + str3 + spce*3

                        if self.roomObjList[1].north != 1:
                            floorPlanStr = floorPlanStr + self.roomObjList[1].north + str2
                        else:
                            floorPlanStr = floorPlanStr + spce + str2

                        print(floorPlanStr)
                        #print(str2 + spce*5 + str3 + "1" +spce*3+ "2" +str3 + spce*5 + str2)
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

    dungeon.show_dungeon_plan_with_entities()


print("Welcome to my Dungeon")
main()
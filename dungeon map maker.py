import random
smallRooms=[[2,2,4],[2,3,6],[2,4,8],[2,5,10],[3,3,9],[3,4,12],[3,5,15]]
rooms=[[4,4,16],[4,5,20],[4,6,24],[4,7,28],[5,5,25],[3,6,18],[3,7,21],[3,8,24]]
largeRooms=[[6,6,36],[6,7,42],[6,8,48],[6,9,54],[7,7,49],[5,6,30],[5,7,35],[5,8,40],[5,9,45],[5,10,50]]
tileTotal=0
class grid():
    def __init__(self, size, mapName):
        self.size = size
        self.mapName = mapName
        self.gridRooms=[]
        self.mapGrid=[]

    def getSize(self):
        return self.size

    def imageGen(self):
        print('comming soon')

    def textDisplay(self, gRooms, size):
        for i in range(0,size):
            row=[]
            for j in range(0,size):
                change=False
                for room in gRooms:
                    for tile in room:
                        if j==tile[0] and i==tile[1]:
                            row.append(1)
                            change=True
                if change==False:
                    row.append(0)
            self.mapGrid.append(row)
        for i in range(0,size):
            print(self.mapGrid[i])

               

    def gridRoomsUpdate(self, room):
        self.gridRooms.append(room)

    def getGridRooms(self):
        return self.gridRooms

class roomTile(grid):
    def __init__(self, size, mapName, smallRooms, rooms, largeRooms, fullSize):
        grid.__init__(self, size, mapName)
        self.smallRooms = smallRooms
        self.rooms = rooms
        self.largeRooms = largeRooms
        self.fullSize = fullSize
        self.tileTotal=0
        self.roomBorders=[]
        self.roomList=[]

    def getRoomList(self):
        return self.roomList

    def roomListUpdate(self, currentRoom):
        self.roomList.append(currentRoom)

    def roomSelect(self):
        if self.fullSize>300:
            roomSize=random.randrange(0,3)
        elif self.fullSize>100:
            roomSize=random.randrange(0,2)
        elif self.fullSize<=100:
            roomSize=(0)
        
        if roomSize==0:
            currentRoom=random.choice(self.smallRooms)
        elif roomSize==1:
            currentRoom=random.choice(self.rooms)
        elif roomSize==2:
            currentRoom=random.choice(self.largeRooms)
        return(currentRoom)

    def perimeter(self):
        perim=[]
        for topTile in range(0,self.size):
            perim.append([topTile,0])
        for botTile in range(0,self.size):
            perim.append([botTile,self.size-1])
        for rightTile in range(1,self.size-1):
            perim.append([self.size-1,rightTile])
        for leftTile in range(1,self.size-1):
            perim.append([0,leftTile])
        return perim

    def roomPlacment(self, currentRoom):
        firstX=random.randint(0,self.size-1)
        firstY=random.randint(0,self.size-1)
        room=[]
        cord=[]
        for tileX in range(0,currentRoom[0]):
            for tileY in range(0,currentRoom[1]):
                cord=[firstX+tileX,firstY+tileY]
                room.append(cord)
        return room

    def perimeterCheck(self, perim, room):
        overlap=False
        for tile in room:
            for tileP in perim:
                if tile == tileP:
                    overlap=True
        if overlap==False:
            return True
        else:
            return False

    def roomOverlapCheck(self, gRooms, room):
        overlap=False
        for rooms in gRooms:
            for tile in rooms:
                for tileR in room:
                    if tileR == tile:
                        overlap=True
        if overlap==False:
            return True
        else:
            return False

    def roomBorder(self, room, currentRoom):
        #top
        for i in range(-1,currentRoom[0]+1):
            self.roomBorders.append([room[0][0]+i,room[0][1]-1])
        #bot
        for i in range(-1,currentRoom[0]+1):
            self.roomBorders.append([room[currentRoom[1]-1][0]+i,room[currentRoom[1]-1][1]+1])
        #right
        for i in range(0,currentRoom[1]):
            room1=(currentRoom[1]*currentRoom[0]-currentRoom[1])
            self.roomBorders.append([room[room1][0]+1,room[room1][1]+i])
        #left
        for i in range(0,currentRoom[1]):
            self.roomBorders.append([room[0][0]-1,room[0][1]+i])

    def roomBorderCheck(self, room):
        overlap=False
        for tile in room:
            for tileB in self.roomBorders:
                if tileB == tile:
                    overlap=True
        if overlap==False:
            return True
        else:
            return False

    def tileTotalUpdate(self, currentRoom):
        self.tileTotal+=currentRoom[2]

    def getTileTotal(self):
        return self.tileTotal
    
class corridor(grid):
    def __init__(self, size, mapName):
        grid.__init__(self, size, mapName)

    def roomSelect(self, gRooms, roomList, offset):
        room1=gRooms[offset]
        room1Details=roomList[offset]
        room2=gRooms[offset+1]
        room2Details=roomList[offset+1]
        return room1, room1Details, room2, room2Details

    def doorSelect(self, room1, room1D, room2, room2D):
        compare1=room1[0]
        compare2=room2[0]
        doorChoices=[]
        bot1=[]
        right1=[]
        left1=[]
        top1=[]
        bot2=[]
        right2=[]
        left2=[]
        top2=[]

        #this compares which sides of the rooms are facing each-other and sets those sides as options for doors
#note to self add an boolean to say which sides to pick from in the next step
        def top(room, details):
            top=[]
            for i in range(0,details[0]):
                top.append(room[0+((details[1])*i)])
            return top

        def bot(room, details):
            bot=[]
            for i in range(0,details[0]):
                bot.append(room[(details[1]-1)+(details[1]*i)])
            return bot

        def right(room, details):
            right=[]
            for i in range(0,details[1]):
                right.append(room[(details[2]-details[1])+i])
            return right

        def left(room, details):
            left=[]
            for i in range(0,details[1]):
                left.append(room[0+i])
            return left
        
    #----------------------#
        
        if compare1[0]<compare2[0] and compare1[1]<compare2[1]:
            bot1=bot(room1, room1D )
            right1=right(room1, room1D)
                #---------#
            top2=top(room2, room2D)
            left2=left(room2, room2D)
        #--------#
        elif compare1[0]<compare2[0] and compare1[1]>compare2[1]:
            right1=right(room1, room1D)
            top1=top(room1, room1D)
                #---------#
            left2=left(room2, room2D)
            bot2=bot(room2, room2D)
        #--------#       
        elif compare1[0]>compare2[0] and compare1[1]<compare2[1]:
            bot1=bot(room1, room1D)
            left1=left(room1, room1D)
                #---------#
            top2=(room2, room2D)
            right2=right(room2, room2D)
        #--------#       
        elif compare1[0]>compare2[0] and compare1[1]>compare2[1]:
            top1=top(room1, room1D)
            left1=left(room1, room1D)
                #--------#
            bot2=bot(room2, room2D)
            right2=right(room2, room2D)
        #--------#    
        elif compare1[0]==compare2[0] and compare1[1]>compare2[1]:
            top1=top(room1, room1D)
                #--------#
            bot2=bot(room2, room2D)
        #--------#    
        elif compare1[0]==compare2[0] and compare1[1]<compare2[1]:
            bot1=bot(room1, room1D)
                #----------#
            top2=top(room2, room2D)
        #----------#        
        elif compare1[0]>compare2[0] and compare1[1]==compare2[1]:
            left1=left(room1, room1D)
                #--------#
            right1=right(room2, room2D)
        #---------#    
        elif compare1[0]<compare2[0] and compare1[1]==compare2[1]:
            right1=right(room1, room1D)
                #-------#
            left2=left(room2, room2D)
        
        
    
        
def run(size, name, smallRooms, rooms, largeRooms):
    mapG = grid(size, name)
    fullSize = size*size
    rooms = roomTile(size, name, smallRooms, rooms, largeRooms, fullSize)
    perim=rooms.perimeter()
    gRooms = mapG.getGridRooms()
    tileTotal = rooms.getTileTotal()
    
    while tileTotal<(fullSize*0.27):
        perimCheck=False
        roomLapCheck=False
        borderCheck=False
        while perimCheck==False or roomLapCheck==False or borderCheck==False:
            currentRoom = rooms.roomSelect()
            room = rooms.roomPlacment(currentRoom)
            perimCheck = rooms.perimeterCheck(perim, room)
            roomLapCheck = rooms.roomOverlapCheck(gRooms, room)
            borderCheck = rooms.roomBorderCheck(room)
        rooms.roomListUpdate(currentRoom)
        rooms.roomBorder(room, currentRoom)
        rooms.tileTotalUpdate(currentRoom)
        tileTotal = rooms.getTileTotal()
        mapG.gridRoomsUpdate(room)
        gRooms = mapG.getGridRooms()

    roomList=rooms.getRoomList()
    #corridor
    cor = corridor(size, name)
    numOfRooms=len(roomList)
    for i in range(0,numOfRooms-1):
        room1, room1Details, room2, room2Details = cor.roomSelect(gRooms, roomList, i)
        cor.doorSelect(room1, room1Details, room2, room2Details)
    
    print(roomList)   
    mapG.textDisplay(gRooms, size)
    

run(20, 'test', smallRooms, rooms, largeRooms)


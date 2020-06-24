#!/usr/bin/env python3.3.2
import random
from PIL import Image, ImageDraw
#room sizes by x and y cords, with tiles taken up for a easy to add up total
smallRooms=[[2,2,4],[2,3,6],[2,4,8],[2,5,10],[3,3,9],[3,4,12],[3,5,15]]
rooms=[[4,4,16],[4,5,20],[4,6,24],[4,7,28],[5,5,25],[3,6,18],[3,7,21],[3,8,24]]
largeRooms=[[6,6],[6,7],[6,8],[6,9],[7,7],[5,6],[5,7],[5,8],[5,9],[5,10]]
dung=[0]
#dungAlpha=[[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1],[8,1],[9,1],[10,1],[11,1],[12,1],[13,1],[14,1],[15,1],[1,2],[2,2],[3,2],[4,2],[5,2],[6,2],[7,2],[8,2],[9,2],[10,2],[11,2],[12,2],[13,2],[14,2],[15,2],[1,3],[2,3],[3,3],[4,3],[5,3],[6,3],[7,3],[8,3],[9,3],[10,3],[11,3],[12,3],[13,3],[14,3],[15,3],[1,4],[2,4],[3,4],[4,4],[5,4],[6,4],[7,4],[8,4],[9,4],[10,4],[11,4],[12,4],[13,4],[14,4],[15,4],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5],[8,5],[9,5],[10,5],[11,5],[12,5],[13,5],[14,5],[15,5],[1,6],[2,6],[3,6],[4,6],[5,6],[6,6],[7,6],[8,6],[9,6],[10,6],[11,6],[12,6],[13,6],[14,6],[15,6],[1,7],[2,7],[3,7],[4,7],[5,7],[6,7],[7,7],[8,7],[9,7],[10,7],[11,7],[12,7],[13,7],[14,7],[15,7],[1,8],[2,8],[3,8],[4,8],[5,8],[6,8],[7,8],[8,8],[9,8],[10,8],[11,8],[12,8],[13,8],[14,8],[15,8],[1,9],[2,9],[3,9],[4,9],[5,9],[6,9],[7,9],[8,9],[9,9],[10,9],[11,9],[12,9],[13,9],[14,9],[15,9],[1,10],[2,10],[3,10],[4,10],[5,10],[6,10],[7,10],[8,10],[9,10],[10,10],[11,10],[12,10],[13,10],[14,10],[15,10],[1,11],[2,11],[3,11],[4,11],[5,11],[6,11],[7,11],[8,11],[9,11],[10,11],[11,11],[12,11],[13,11],[14,11],[15,11],[1,12],[2,12],[3,12],[4,12],[5,12],[6,12],[7,12],[8,12],[9,12],[10,12],[11,12],[12,12],[13,12],[14,12],[15,12],[1,13],[2,13],[3,13],[4,13],[5,13],[6,13],[7,13],[8,13],[9,13],[10,13],[11,13],[12,13],[13,13],[14,13],[15,13],[1,14],[2,14],[3,14],[4,14],[5,14],[6,14],[7,14],[8,14],[9,14],[10,14],[11,14],[12,14],[13,14],[14,14],[15,14],[1,15],[2,15],[3,15],[4,15],[5,15],[6,15],[7,15],[8,15],[9,15],[10,15],[11,15],[12,15],[13,15],[14,15],[15,15]]
dungAlpha=[[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0],[13,0],[14,0],[0,1],[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1],[8,1],[9,1],[10,1],[11,1],[12,1],[13,1],[14,1],[0,2],[1,2],[2,2],[3,2],[4,2],[5,2],[6,2],[7,2],[8,2],[9,2],[10,2],[11,2],[12,2],[13,2],[14,2],[0,3],[1,3],[2,3],[3,3],[4,3],[5,3],[6,3],[7,3],[8,3],[9,3],[10,3],[11,3],[12,3],[13,3],[14,3],[0,4],[1,4],[2,4],[3,4],[4,4],[5,4],[6,4],[7,4],[8,4],[9,4],[10,4],[11,4],[12,4],[13,4],[14,4],[0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5],[8,5],[9,5],[10,5],[11,5],[12,5],[13,5],[14,5],[0,6],[1,6],[2,6],[3,6],[4,6],[5,6],[6,6],[7,6],[8,6],[9,6],[10,6],[11,6],[12,6],[13,6],[14,6],[0,7],[1,7],[2,7],[3,7],[4,7],[5,7],[6,7],[7,7],[8,7],[9,7],[10,7],[11,7],[12,7],[13,7],[14,7],[0,8],[1,8],[2,8],[3,8],[4,8],[5,8],[6,8],[7,8],[8,8],[9,8],[10,8],[11,8],[12,8],[13,8],[14,8],[0,9],[1,9],[2,9],[3,9],[4,9],[5,9],[6,9],[7,9],[8,9],[9,9],[10,9],[11,9],[12,9],[13,9],[14,9],[0,10],[1,10],[2,10],[3,10],[4,10],[5,10],[6,10],[7,10],[8,10],[9,10],[10,10],[11,10],[12,10],[13,10],[14,10],[0,11],[1,11],[2,11],[3,11],[4,11],[5,11],[6,11],[7,11],[8,11],[9,11],[10,11],[11,11],[12,11],[13,11],[14,11],[0,12],[1,12],[2,12],[3,12],[4,12],[5,12],[6,12],[7,12],[8,12],[9,12],[10,12],[11,12],[12,12],[13,12],[14,12],[0,13],[1,13],[2,13],[3,13],[4,13],[5,13],[6,13],[7,13],[8,13],[9,13],[10,13],[11,13],[12,13],[13,13],[14,13],[0,14],[1,14],[2,14],[3,14],[4,14],[5,14],[6,14],[7,14],[8,14],[9,14],[10,14],[11,14],[12,14],[13,14],[14,14]]
roomTiles=(0)
roomInfo=[]
perim=[]
#--------------------------------------------------------------------------------------#
class grid():
    def __init__(self, smallRooms, rooms, largeRooms, dung):
        self.small=smallRooms
        self.medium=rooms
        self.large=largeRooms
        self.dung=dung
    def dungSize(self, dung):
        #creating apropriete size array for dungeon
        for i in range(1,225):
            dung.append(0)
    def display(self, tiles, dung, roomInfo, rooms, corridor, dungAlpha, doors):
        xyTile=[]
        xyTiles=[]
        roomsC=[]
        door=[]
        doorsGrid=[]
        v=len(dungAlpha)
        for i in range(0,v):
            for x in corridor:
                if x==dungAlpha[i]:
                    xyTile.append(i)
        xyTiles.append(xyTile)
        xyTile=[]
        for i in range(0,v):
            for x in doors:
                for c in x:
                    if c==dungAlpha[i]:
                        door.append(i)
        for x in rooms:
            l=len(x)
            for i in range(0,l):
                for k in range(0,224):
                    if k==x[i]:
                        dung[k]=(8)
        for x in door:
            for k in range(0,224):
                if k==x:
                    dung[k]=(4)
        for x in xyTiles:
            roomsC.append(x)
        j=len(rooms)
        for x in roomsC:
            l=len(x)
            for i in range(0,l):
                for k in range(0,224):
                    if k==x[i]:
                        dung[k]=(1)
        for i in range(0,15):
            l=(i*15)
            print(dung[0+l],dung[1+l],dung[2+l],dung[3+l],dung[4+l],dung[5+l],dung[6+l],dung[7+l],dung[8+l],dung[9+l],dung[10+l],dung[11+l],dung[12+l],dung[13+l],dung[14+l])
        im=Image.new("RGB",(600,600),(0,255,0))
        idraw=ImageDraw.Draw(im)
        l=len(dung)
        brown=[[140,70,0],[144,72,0],[148,74,0],[153,76,0],[184,92,0],[188,94,0],[192,96,0],[196,98,0],[200,100,0],[204,102,0],[208,104,0],[212,106,0]]
        grey=[[200,200,200]]
        for i in range(0,l):
            if dung[i]==8:
                for k in range(0,20):
                    for v in range(0,20):
                        color=random.choice(grey)
                        idraw.rectangle([(dungAlpha[i][0]*40+v,dungAlpha[i][1]*40+k),(dungAlpha[i][0]*40+20+v,dungAlpha[i][1]*40+20+k)],fill=(255,255,255))
            elif dung[i]==1:
                for k in range(0,20):
                    for v in range(0,20):
                        color=random.choice(grey)
                        idraw.rectangle([(dungAlpha[i][0]*40+v,dungAlpha[i][1]*40+k),(dungAlpha[i][0]*40+20+v,dungAlpha[i][1]*40+20+k)],fill=(255,255,255))
            else:
                for k in range(0,40):
                    for v in range(0,40):
                        color=random.choice(brown)
                        idraw.rectangle([(dungAlpha[i][0]*40+v,dungAlpha[i][1]*40+k),(dungAlpha[i][0]*40+v,dungAlpha[i][1]*40+k)],fill=(0,0,0))
        for i in range(0,60):
            idraw.line([(0,i*20),(600,i*20)],width=1,fill=(0,0,0))
            idraw.line([(i*20,0),(i*20,600)],width=1,fill=(0,0,0))
        im.save("exampleMap.png")

#--------------------------------------------------------------------------------------#       
class roomPlacement(grid):
    def __init__(self, smallRooms, rooms, largeRooms, dung, roomTiles):
        self.roomTiles=roomTiles
    def firstRoom(self, roomTiles):
        #places first room
        valid=False
        change=False
        #array containing all gird cords on the edges
        edges=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,29,44,59,74,89,104,119,134,149,164,179,194,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,15,30,45,60,75,90,105,120,135,150,165,180,195]
        #check to make sure no rooms already exist before starting
        if roomTiles==(0):
            #chooses a room dimensions from the medium size array
            first=[]
            first=random.choice(rooms)
            #selects a starting coordinate
            firstCord=[]
            firstCord=random.randint(0,224)
            #declares variables used to generate tiles used up on the grid by the room
            tiles=[]
            xTiles=[]
            yTiles=[]
            tempTiles=[]
            prim=[]
            yCount=1
            #runs a for loop for how long the room spreads out on the x axel
            for i in range(0,first[0]):
                xTiles.append(firstCord+i)
            tempTiles=xTiles
            tiles.append(xTiles)
            #shifts x coordinates by 15 to calculate the y coordinates
            while yCount<first[1]:
                if yCount<first[1]:
                    for j in range(0,first[0]):
                        yTiles.append(tempTiles[j]+15)
                    tiles.append(yTiles)
                    tempTiles=[]
                    yCount=yCount+1
                else:
                    break
                if yCount<first[1]:
                    for j in range(0,first[0]):
                        tempTiles.append(yTiles[j]+15)
                    tiles.append(tempTiles)
                    yTiles=[]
                    yCount=yCount+1
                else:
                    break
            #primeter stuff
            #top row
            topLen=len(tiles[0])
            for i in range(0,topLen):
                prim.append(tiles[0][i]-15)
            prim.append(prim[0]-1)
            prim.append(prim[topLen-1]+1)
            #bottom row
            tileLen=len(tiles)
            botLen=len(tiles[tileLen-1])
            for i in range(0,botLen):
                prim.append(tiles[tileLen-1][i]+15)
            primLen=len(prim)
            prim.append(prim[primLen-1]+1)
            prim.append(prim[topLen+2]-1)
            #right side
            right=first[0]
            for i in range(0,tileLen):
                prim.append(tiles[i][right-1]+1)
            #left side
            for i in range(0,tileLen):
                prim.append(tiles[i][0]-1)
            #check if any tiles hit an edge
            for x in tiles:
                j=len(x)
                for i in range(0,j):     
                    if x[i] in edges:
                        valid=False
                        change=True
            if change==False:
                valid=True
                    
            #adds number of tiles used to roomTiles
            roomTiles=first[2]
            #returns need variables 
            return tiles, valid, roomTiles, first, prim
#----------------------------------------------------------------------------------------------#
    def placeRoom(self, roomTiles, tiles, roomList, perim):
        #places room till it hits its max 30% of the dungeon size(small)
        if roomTiles<60:
            edge=False
            overlap=False
            change=False
            change1=False
            #array containing all gird cords on the edges
            edges=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,29,44,59,74,89,104,119,134,149,164,179,194,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,15,30,45,60,75,90,105,120,135,150,165,180,195]
            #chooses a room dimensions from the medium size array
            start=[]
            start=random.choice(roomList)
            #selects a starting coordinate
            startCord=[]
            startCord=random.randint(0,224)
            #declares variables used to generate tiles used up on the grid by the room
            tilesNext=[]
            xTiles=[]
            yTiles=[]
            tempTiles=[]
            yCount=1
            prim2=[]
            #runs a for loop for how long the room spreads out on the x axel
            for i in range(0,start[0]):
                xTiles.append(startCord+i)
            tempTiles=xTiles
            tilesNext.append(xTiles)
            #shifts x coordinates by 15 to calculate the y coordinates
            while yCount<start[1]:
                if yCount<start[1]:
                    for j in range(0,start[0]):
                        yTiles.append(tempTiles[j]+15)
                    tilesNext.append(yTiles)
                    tempTiles=[]
                    yCount=yCount+1
                else:
                    break
                if yCount<start[1]:
                    for j in range(0,start[0]):
                        tempTiles.append(yTiles[j]+15)
                    tilesNext.append(tempTiles)
                    yTiles=[]
                    yCount=yCount+1
                else:
                    break
            #primeter stuff
            #top row
            topLen=len(tilesNext[0])
            for i in range(0,topLen):
                prim2.append(tilesNext[0][i]-15)
            prim2.append(prim2[0]-1)
            prim2.append(prim2[topLen-1]+1)
            #bottom row
            tileLen=len(tilesNext)
            botLen=len(tilesNext[tileLen-1])
            for i in range(0,botLen):
                prim2.append(tilesNext[tileLen-1][i]+15)
            primLen=len(prim2)
            prim2.append(prim2[primLen-1]+1)
            prim2.append(prim2[topLen+2]-1)
            #right side
            right=start[0]
            for i in range(0,tileLen):
                prim2.append(tilesNext[i][right-1]+1)
            #left side
            for i in range(0,tileLen):
                prim2.append(tilesNext[i][0]-1)
            #check if any tiles hit an edge
            for x in tilesNext:
                j=len(x)
                for i in range(0,j):    
                    if x[i] in edges:
                            edge=False
                            change=True
            if change==False:
                edge=True
            #checks if any tiles overlap
            for x in tilesNext:
                j=len(x)
                for i in range(0,j):
                    for v in tiles:
                        if x[i] in v:
                            overlap=False
                            change1=True
            #perimeter check
            for x in tilesNext:
                j=len(x)
                for i in range(0,j):
                    for v in perim:
                        if x[i] in v:
                            #print("d", tilesNext, "d")
                            overlap=False
                            change1=True
            if change1==False:
                overlap=True
            #adds number of tiles used to roomTiles                 
            roomTilesTemp=start[2]
            #returns need variables
            return tilesNext, edge, overlap, roomTilesTemp, start, prim2
#----------------------------------------------------------------------------------#
class corridorPlacement(grid):
    def __init__(self, smallRooms, rooms, largeRooms, dung):
        print("hi")
    def placeCorridor(self, tiles, roomInfo, dungAlpha):
        print(roomInfo)
        #2d array that will hold all room
        rooms=[]
        #tempory array to hold room tiles to be moved into rooms
        room=[]
        #marks where to start in the array tiles
        count=0
        #number of rooms in tiles
        numOfRooms=len(roomInfo)
        #loops for the number of rooms
        for i in range(0,numOfRooms):
            distance=count+roomInfo[i][1]
            #loops from last point
            for j in range(count,distance):
                #loops for indivual x axis sections in tiles
                for l in range(0,roomInfo[i][0]):
                    #appends each tile in the x axis to room
                    room.append(tiles[j][l])
            #moves room tiles to rooms array
            rooms.append(room) 
            #resets room array
            room=[]
            #adjusts counter
            count=count+roomInfo[i][1]
        #-------------------------------------------------#
        j=len(rooms)
        wallTop=[]
        wallBot=[]
        wallLeft=[]
        wallRight=[]
        walls=[]
        corridors=[]
        r=[]
        for x in range(0,j):
            #top row
            for i in range(0,roomInfo[x][0]):
                wallTop.append(rooms[x][i])
            #bottom row
            roomLen=len(rooms[x])
            botLen=(roomLen-roomInfo[x][0])
            for i in range(botLen,roomLen):
                wallBot.append(rooms[x][i])
            #right side
            right=roomInfo[x][0]
            count=0
            for i in range(0,roomInfo[x][1]):
                wallRight.append(rooms[x][right-1]+count)
                count=count+15
            #left side
            left=roomInfo[x][0]
            count=-15
            for i in range(0,roomInfo[x][1]):
                wallLeft.append(rooms[x][right]+count)
                count=count+15
            r.append(wallTop)
            r.append(wallBot)
            r.append(wallLeft)
            r.append(wallRight)
            walls.append(r)
            wallTop=[]
            wallBot=[]
            wallLeft=[]
            wallRight=[]
            r=[]
            start=[]
        
        #-------------------------------------------------#
        #convertd to x and y
        xyTile=[]
        xyTiles=[]
        outLine=False
        corridor=[]
        doors=[]
        for v in walls:
            for x in v:
                for i in x:
                    xyTile.append(dungAlpha[i])
                xyTiles.append(xyTile)
                xyTile=[]
        for t in range(0,len(roomInfo)-1):
            count=(t*4)
            room1Top=xyTiles[0+count]
            room1Bot=xyTiles[1+count]
            room1Left=xyTiles[2+count]
            room1Right=xyTiles[3+count]
            for y in range(0,len(roomInfo)-1):
                corridor=[]
                overlap=False
                outLine=False
                change=False
                count2=(y*4)
                if count!=count2:
                    room2Top=xyTiles[4+count2]
                    room2Bot=xyTiles[5+count2]
                    room2Left=xyTiles[6+count2]
                    room2Right=xyTiles[7+count2]
                    #checks if and corrdinates are in line
                    inLine=[]
                    room1=room1Top[0]
                    room2=room2Top[0]
                    #print("d",len(roomInfo))
                    if room1[0]>room2[0]:
                        #room1 left room2 right
                        for i in room1Left:
                            for x in room2Right:
                                if i[0]==x[0]:
                                    inLine.append([i,x])
                                elif i[1]==x[1]:
                                    inLine.append([i,x])
                    elif room2[0]>room1[0]:
                        #room1 right room2 left
                        for i in room1Right:
                            for x in room2Left:
                                if i[0]==x[0]:
                                    inLine.append([i,x])
                                elif i[1]==x[1]:
                                    inLine.append([i,x])
                    elif room1[1]>room2[1]:
                        #room1 top room2 bot
                        for i in room1Top:
                            for x in room2Bot:
                                if i[0]==x[0]:
                                    inLine.append([i,x])
                                elif i[1]==x[1]:
                                    inLine.append([i,x])
                    elif room2[1]>room1[1]:
                        #room1 bot room2 top
                        for i in room1Bot:
                            for x in room2Top:
                                if i[0]==x[0]:
                                    inLine.append([i,x])
                                elif i[1]==x[1]:
                                    inLine.append([i,x])
                    if inLine==[]:
                        outLine=True
                #-------------------------------------------------#
                    if outLine==False:
                        start=random.choice(inLine)
                        if start[0][0]==start[1][0]:
                            if start[0][1]>start[1][1]:
                                for i in range(start[1][1]+1,start[0][1]):
                                    corridor.append([start[0][0],i])
                            else:
                                for i in range(start[0][1]+1,start[1][1]):
                                    corridor.append([start[0][0],i])
                        else:
                            if start[0][0]>start[1][0]:
                                for i in range(start[1][0]+1,start[0][0]):
                                    corridor.append([i,start[0][1]])
                            else:
                                for i in range(start[0][0]+1,start[1][0]):
                                    corridor.append([i,start[0][1]])
                        print("d",corridor)
                v=len(dungAlpha)
                xyTile2=[]
                xyTiles2=[]
                for i in range(0,v):
                    for x in corridor:
                        if x==dungAlpha[i]:
                            xyTile2.append(i)
                for x in xyTile2:
                    for v in tiles:
                        for i in v:
                            if x==i:
                                overlap=True
                                change=True
                if change==False:
                    overlap=False
                if overlap==False:
                    for x in corridor:
                        corridors.append(x)                    
        return rooms, corridors, doors
#----------------------------------------------------------------------------------#
dungeon=grid(smallRooms, rooms, largeRooms, dung)
dungeon.dungSize(dung)
dungeonRooms=roomPlacement(smallRooms, rooms, largeRooms, dung, roomTiles)
dungeonCorridors=corridorPlacement(smallRooms, rooms, largeRooms, dung)

tiles, valid, roomTiles, roomInfoTemp, prim=dungeonRooms.firstRoom(roomTiles)
while valid==False:
    del tiles[:]
    del roomInfoTemp[:]
    del prim[:]
    roomTiles=0
    tiles, valid, roomTiles, roomInfoTemp, prim=dungeonRooms.firstRoom(roomTiles)
roomInfo.append(roomInfoTemp)
perim.append(prim)
while roomTiles<60:
    size=random.randint(0,2)
    if size==0 or 1:
        roomList=smallRooms
    else:
        roomList=rooms
    tilesNext, edge, overlap, roomTilesTemp, roomInfoTemp, prim2=dungeonRooms.placeRoom(roomTiles, tiles, roomList, perim)
    #loops if hits an edge or other room
    while edge==False or overlap==False:
        del tilesNext[:]
        del prim2[:]
        tilesNext, edge, overlap, roomTilesTemp, roomInfoTemp, prim2=dungeonRooms.placeRoom(roomTiles, tiles, roomList, perim)
    #adds changes to permanent variables
    roomTiles=(roomTiles+roomTilesTemp)
    tiles=tiles+tilesNext
    roomInfo.append(roomInfoTemp)
    perim.append(prim2)
    
rooms, corridor, doors=dungeonCorridors.placeCorridor(tiles, roomInfo, dungAlpha)
dungeon.display(tiles, dung, roomInfo, rooms, corridor, dungAlpha, doors)
print("Hello World!")

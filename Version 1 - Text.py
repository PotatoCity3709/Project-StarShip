#Get the desired modules
import random as ra
import time as ti

shipName = input('Name of ship: ') #Get the name of the ship

#Define the instructions and display it
instructions = '''
Project: StarShip v0.0 CLOSED Dev

How to play:
When the program begins, you will be told where
you are on the ship, the actions you can follow,
the situation of the ship, fuel level and the current
speed of the ship in Miles per Hour.

When that has been displayed, you will be prompted what
you would like to do.
Your actions always have a reaction!

'''
print(instructions)

#Variables
shipType = '0.0'

roomNames = ['Bridge', 'Your Living Quarters', 'Elevator'] #Corresponds to roomLocations
roomLocations = ['Top Level', 'Top Level', 'Top Level' + 'Middle Level']

roomCurrent = roomNames[0]

possibleAction = []
situationCurrent = 'Normal'

situations = []
fuel = 1000.0

speed = 100
shipDirection = 0
speedMin = -200
speedMax = 1000

warp = 0
warpSpeedMin = 1
warpSpeedMax = 5

shipPositionX = 0
shipPositionY = 0

#Definitions and classes
def shipSpecs(): #Used for showing how the ship can be used
    global shipName, shipType, speedMin, speedMax, warpSpeedMin, warpSpeedMax, fuel

    print('Your ship name & type: ' + shipName + ' ' + shipType + '.\n')
    ti.sleep(0.5)
    print('Your ship\'s maximum speed is: ' + str(speedMax) + '.')
    print('Your ship\'s minimum speed is: ' + str(speedMin) + '.\n')
    ti.sleep(0.5)
    print('Your ship\'s maximum warp speed is: ' + str(warpSpeedMax) + '.')
    print('Your ship\'s minimum warp speed is: ' + str(warpSpeedMin) + '.\n')
    ti.sleep(5)

def fillAction(): #Fills up the list of actions
    global possibleAction

    possibleAction.append('Increase Speed')
    possibleAction.append('Decrease Speed')

    possibleAction.append('Set Warp Speed')

    possibleAction.append('Ship Specs')
    
    possibleAction.append('Move Room')

def updateActionList():
    global possibleAction
    possibleAction.clear()
    
    if roomCurrent == 'Bridge': 
        possibleAction.append('Increase Speed')
        possibleAction.append('Decrease Speed')

        possibleAction.append('Set Warp Speed')

        possibleAction.append('Ship Specs')
    
        possibleAction.append('Move Room')   
        
    return possibleAction

def systemMessage(): #Default message
    global roomCurrent, possibleAction, situationCurrent, fuel, speed

    print('\n\n')

    print('Current Room: ' + str(roomCurrent))
    print('Ship Situation: ' + situationCurrent + '\n')
    ti.sleep(0.4)
    print('Actions you could perform: ' + str(possibleAction) + '\n')
    ti.sleep(0.4)
    print('Fuel: ' + str(fuel))
    print('Speed: ' + str(speed) + '\n')
    ti.sleep(0.3)
    print('...Collecting Position...')
    ti.sleep(0.5)
    print('...SXL Distribution unit found position. Displaying...')
    ti.sleep(0.2)
    print('Position X: ' + str(shipPositionX))
    ti.sleep(0.1)
    print('Position Y: ' + str(shipPositionY))

class checkActions: #Checking if the actions can work.
    
    def checkSpeed():
        global speed, speedMin, speedMax
    
        if speed <= speedMin:
            ti.sleep(0.3)
            print('\n\nEngine Burnt. Game Over')
            exit()
        
        if speed >= speedMax:
            ti.sleep(0.3)
            print('\n\nEngine Burnt. Game Over')
            exit()
    
    def speed(action):
        global possibleAction, speed
        
        if action == 'Increase Speed':
            amount = input('Choose Speed Increase: ')
            ti.sleep(.2)
            print('Speed Increased')
            speed += int(amount)
            checkActions.checkSpeed()
        
        if action == 'Decrease Speed':
            amount = input('Choose Speed Decrease: ')
            ti.sleep(.2)
            print('Speed Decreased')
            
            speed -= int(amount)
            checkActions.checkSpeed()            

        if action == 'Set Warp Speed':
            warpAmount = input('Warp Speed: ')

            ti.sleep(.2)
            if warpAmount >= '-1':
                print('Engines Will Overload. Please Re-Enter Warp Amount')
            elif warpAmount <= '5':
                print('Engines Will Overload. Please Re-Enter Warp Amount')

            ti.sleep(.1)
            print('Warp Aim: ' + str(warpAmount))
            ti.sleep(0.05)
            print('Current Warp Speed:' + str(warp))

    def displayShipSpecs(action):
        global possibleAction

        if action == 'Ship Specs':
            print('Displaying Ship Specs:\n')
            shipSpecs()
            
    def tryMoveRoom(action):
        global roomCurrent
        
        if action == 'Move Room':
            ti.sleep(1)
            print('Current Room: ' + str(roomCurrent))
            print('You can travel to rooms:\n')
            ti.sleep(0.4)
            if roomCurrent == 'Bridge':
                print(roomNames[1])
            elif roomCurrent == 'Your Living Quarters':
                print(roomNames[0])
                
            newRoom = input('Enter Room Name: ')
            
            newRoomCaps = newRoom.upper()
            
            if newRoomCaps == 'BRIDGE' or 'YOUR LIVING QUARTERS':
                print('Traveling to room: ' + newRoom)
                roomCurrent = newRoom

def deteriorateFuel(speed): #Slowly reducing the fuel
    global fuel
    fuel -= (speed + ra.randint(1, 3) + speed)
    return fuel

def moveShipX(): #Moves the ship on a relative coordinate
    global shipDirection, shipPositionX

def moveShipY(): #Moves the ship on a relative coordinate
    global shipDirection, shipPositionY

fillAction() #Fills up the action list

#Initialise the class
def checkAction(action):
    checkActions.speed(action)
    checkActions.displayShipSpecs(action)
    checkActions.tryMoveRoom(action)
    return action

#Main Game Loop
while True:
    updateActionList()
    ti.sleep(0.5)
    systemMessage()
    ti.sleep(1)
    action = input('What action would you like to perform: ')
    #getAction()
    deteriorateFuel(2.5)
    ti.sleep(1)
    checkAction(action)
    

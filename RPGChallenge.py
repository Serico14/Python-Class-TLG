#!/usr/bin/python3
"""Purpose of RPG Code"""

import random

# Replace RPG starter project with this code when new instructions are live
def main()

    def showInstructions():
      #print a main menu and the commands
      print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    ''')

    def showStatus():
      #print the player's current status
      print('---------------------------')
      print('You are in the ' + currentRoom)
      #print the current inventory
      print('Inventory : ' + str(inventory))
      #print an item if there is one
      if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
      print("---------------------------")

    #an inventory, which is initially empty
    inventory = []

    #a dictionary linking a room to other rooms
    #round count
    round= 0

    #random integer generator

    ## A dictionary linking a room to other rooms
    rooms = {

                'Hall' : {
                      'south' : 'Kitchen',
                      'east'  : 'Dining Room',
                      'item'  : 'key'
                    },

                'Kitchen' : {
                      'north' : 'Hall',
                      'item'  : 'monster',
                    },
                'Dining Room' : {
                      'west' : 'Hall',
                      'south': 'Garden',
                      'item' : 'potion',
                      'north' : 'Pantry',
                   },
                'Garden' : {
                      'north' : 'Dining Room'
                   },
                'Pantry' : {
                      'south' : 'Dining Room',
                      'item' : 'cookie',
                }
             }

    #start the player in the Hall
    currentRoom = 'Hall'

    showInstructions()

    player = {
        "attack":10,
        "health":30,
        
        }
    monster = {
        "attack":10,
        "health":30,
        }


    #loop forever
    while True:

      showStatus()

      #get the player's next 'move'
      #.split() breaks it up into an list array
      #eg typing 'go east' would give the list:
      #['go','east']
      move = ''
      while move == '':
        move = input('>')

      # split allows an items to have a space on them
      # get golden key is returned ["get", "golden key"]          
      move = move.lower().split(" ", 1)

      #if they type 'go' first
      if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
          #set the current room to the new room
          currentRoom = rooms[currentRoom][move[1]]
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

      #if they type 'get' first
      if move[0] == 'get' :
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
          #add the item to their inventory
          inventory += [move[1]]
          #display a helpful message
          print(move[1] + ' got!')
          #delete the item from the room
          del rooms[currentRoom]['item']
        #otherwise, if the item isn't there to get
        else:
          #tell them they can't get it
          print('Can\'t get ' + move[1] + '!')
          
      ## Define how a player can win
      if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

      # If a player enters a room with a monster
      """Purpose of function: Activate Monster Battle"""

      elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('You see a monster devouring a corpse in the center of the room. The door behind you is about to close, what do you do?')
        response = input("Attack / Protect / Flee\n")
       
        if response == 'Attack':
            print("You tackle the monster and catch it off guard, hitting it's head on a table.!")
            monster["health"] = monster["health"] - player["attack"]
            print("The monster sounds injured and in pain.(Health decrease from 30 to", monster["health"],"!")
            
        elif response == 'Protect':
            print("You raise your arms to the side to protect your organs. Your clothing makes the slightest sound.")
            player["health"] = player["health"] - monster["attack"]
            print("The monster turns to you and slices your body right where you protected.Player health = ", player["health"])
            
        else:
            print("The monster hears you clamor the door and rushes behind you with quiet speed and everything goes black.")
            quit() 

        while round < 10:      
            
            response = input("Select your next action: \nAttack / Block / Flee\n")
           
            if response == 'Attack':
                 print("You strike the monster with all your might!")
                 monster["health"] = monster["health"] - player["attack"]
                 print("The monster's health has decreased from 30 to ", monster["health"], "!" )

            elif response == 'Block':
                 #print("The monster turns around swipes at you with its fist.\nPlayer health now at",  player["health"] , "out of 30")
                 player["health"] = player["health"] - monster["attack"]
                 print("The monster turns around swipes at your with its fist. \nPlayer health now at", player["health"], "out of 30")      
            else:
                 print("The monster pounces onto you as you turn around and vescirates your body. You commited, stick with it.")
                 quit()   
            
            if monster["health"] <= 0:
                 print("Congratulations, you have defeated the monster. The world around you begins to dissipate and you come to realize this was all a dream.")
                 quit()
            if player["health"] <= 0:
                 print("You took too much damage and fall to the ground, fading out of existence.")
                 quit()

            #    else:
            #    print("Command not recogize. Choose again.\n")
            round += 1

if __name__ == "__main__"

main()


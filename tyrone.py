#Tyrone's Quest
#Text Adventure
#Khalil Lindsey, Ian Harker

state = "intro"
def blank():
  a
def help():
  print("")
  print("Commands")
  print("")
  print("Inspect - Look around a room")
  print("Fight - Fight in a battle")
  print("Run - Flee from a battle")
  print("Use - Use an item in a room")
  print("Type help at any time to have the commands displayed to you agan")
  print("")
def intro():
  print("")
  print("Tyrone's Quest")
  print("")
  print("You are a young man named Tyrone, on a quest in the medieval ages to avenge his father and take his throne to carry on the family name.")
  print("")
  print("")
  print("In this dungeon, you will have to solve puzzles and fight dangerous creatures in order to retrieve your father's necklace, which will allow you to take the throne as king of Landfriedtown.")
  print("")
  print("")
  global state
  state = "ReadyToStart"
def ReadyToStart():
  global state
  ReadyToStart = input("Are you ready to start? y=yes, n= no:")
  print("")
  if ReadyToStart == 'y' or ReadyToStart == 'Y' :
    print("The adventure begins...")
    state = "ButtonRoom"
  elif ReadyToStart == 'n' or ReadyToStart == 'N':
    print("Game Over") 
    state = "intro"
def ButtonRoom():
  global state
  print("")
  print("As you enter the room of the worn down cobblestone dungeon, you notice nothing but a lever on the wall by the locked door.")
  print("")
  ButtonRoom = input("Are you going to pull the lever? y=yes, n= no:")
  print("")
  if ButtonRoom == 'y' or ButtonRoom == 'Y' :
    state = "SlimeFight"
  elif ButtonRoom == 'n' or ButtonRoom == 'N':
    print("")
    print("There doesn't seem to be any other way out of this room...")
    print("")
    print("")
def SlimeFight():
  global state
  print("")
  fightslime = input("A slime appears behind a moving wall, what do you do? (fight or run):")
  print("")
  if fightslime == "fight":
    print("")
    print("You slash your sword towards the slime, killing it. You pick up slime a chunk of slime, which seems to be useful for binding materials together. In the remains of the slime, you find a key with the number 1 on it. The door opens up and you enter the forked hallway")
    state = "Hallway1" 
  elif fightslime == "run":
    print("")
    print("You try to run away but the door is closed behind you...")
    print("")
def Hallway1():
  global state
  print("")
  print("As you enter the forked hallway, there are two paths to take, both labeled in an unknown language. The only unlocked room is the left one, which you enter prepared for a fight")
  print("")
  print("")
  print("However, as you enter, you realized no combat will be necessary. In fact, the room seems to be empty except for a mirror on the other side of the room.")
  state = "MirrorRoom"
def MirrorRoom():
  global state
  print("")
  print("The mirror seems suspicous looking, you know this isn't the end of you journey.")
  print("")
  MirrorRoom = input("Type a command:")
  print("")
  if MirrorRoom == 'Inspect' or MirrorRoom == "inspect" :
    print("When you look in the mirror, you notice a button on the other side of the wall, which would otherwise be invisible.")
    state = "MirrorOpen"
  elif MirrorRoom == 'n' or MirrorRoom == 'N':
    print("")
    print("There doesn't seem to be any other way out of this room...")
    print("")
  elif MirrorRoom == 'help':
    help()
  else:
    print("Invalid Command")
def MirrorOpen():
  global state
  print("")
  MirrorOpen = input("Will you press the button? Y or N:")
  if MirrorOpen == 'Y' or MirrorOpen == 'y':
    print("When you press the button, the mirror slides to the right, revealing a small enterance to the next room.")
    state = "Chest1"
  elif MirrorOpen == 'N' or MirrorOpen == 'n':
    print ("") 
    print("The only other way is to leave")
    print("")
def Chest1():
  global state
  print("")
  print("")
  print("After the mirror moves, part of the wall to the left collapses to reveal a wooden chest with faded gold trimmings.")
  print("")
  Chest1 = input("Will you open the chest? Y or N:")
  if Chest1 == 'Y' or Chest1 == 'y':
    print("")
    print("You found a can of Sprite Cranberry and a small wooden sheild, it seems sturdy enough.")
    Drink1 = input("Do you want to drink the can of Sprite Cranberry? Y or N:")
    if Drink1 == 'Y' or Drink1 == 'y':
      print("")
      Drink2 = input("Are you sure? It smells kind of funky...:")
      if Drink1 == 'Y' or Drink1 == 'y':
        state = "Pineapple1"
    elif Drink1 == 'N' or Drink1 == 'n':
      print("")
      print("Good choice...it's probably best not to.")
      state = "Skeleton"
  elif Chest1 == 'N' or Chest1 == 'n':
    print("")
    print("It probably has pretty useful gear...")
    print("")
def Pineapple1():
  global state
  name1 = input("What's your name?:")
  if name1 == 'Tyrone' or name1 == 'tyrone':
    print("Who'd name their child that?")
  else:
    seafries = input("My name is Dustin Seafries, I need your help on my quest. Do you accept?:")
    if seafries == 'Y' or seafries == 'y':
      pineinspect = input("We need to find the source of the evil sprite cranberries.:")
      if pineinspect == 'help':
        help()
      elif pineinspect == 'inspect':
        gonorth = input("There's a trail of cranberries going north, will you follow it?:")
        if gonorth == 'Y' or gonorth == 'y':
          state = "Pineapple2"
        if gonorth == 'N' or gonorth == 'n':
          print("There's no other direction to go...")
      else:
        print("Invalid Command.")
    if seafries == 'N' or seafries == 'n':
      print("Dustin Seafries's face swells up, revealing a pineapple.")
      print("")
      print("GAME OVER")
      state = "intro"
def Pineapple2():
  global state
  print("There's a berry with legs, I'm not sure what a cranberry looks like but this guy looks the type.")
  print("")
  fightcran = input("Do you wish to fight this cranberry? Y or N:")
  if fightcran == 'Y' or fightcran == 'y':
    state = "Fightcranman"
  elif fightcran == 'N' or fightcran == 'n':
    print("An earthquake closes the entrance of the cave behind you, this isn't looking good...")
def Fightcranman():
  global state
  print("Dustin swings his Pine-sword™ at Cranman, killing it's legs")
  print("")
  cranblow = input("Cranman is on the ground, do you swing your sword while he's weak? Y or N:")
  if cranblow == 'Y' or cranblow == 'y':
    print("")
    print("Cranman is actually dead, I can't believe this... says Dustin Seafries.")
    print("")
    print("PEACE IS RESTORED TO PINEAPPLE LAND")
    state = "intro"
  elif cranblow == 'N' or cranblow == 'n':
    print("")
    print("Cranman gets up, despite his dead legs and stomps on you.")
    print("")
    print("GAME OVER")
    state = "intro"
def Skeleton():
  global state
  print("As you enter the next room, you notice a skeleton guarding the enterance of what seems to be the last room of the hallway.")
  print("")
  print("Skeleton: Wandering traveler, I command you to leave this dungeon or face severe onsequences.")
  print("")
  Skeleton = input("Leave or Stay?:") 
  if Skeleton == 'Leave' or Skeleton == "leave":
    print("You gave up on your quest. GAME OVER ")
    state = "ReadyToStart"
  elif Skeleton == 'Stay' or Skeleton == 'stay':
    print("")
    print("Then you will need to get past me! The skeleton attacks you with a spear, barely missing you.")
    print("")
    Skeleton = input("Attack or run?:")
    if Skeleton == 'Attack' or Skeleton == "attack" :
      print("You swing your sword, but the skeleton dodges your attack, and counters by pushing you with the dull end of his spear.")
      state = "Battle2"
    elif Skeleton == 'Run' or Skeleton == 'run':
      print("You leave the dungeon, never to return. GAME OVER")
      state == "ReadyToStart"
def Battle2():
  global state
  print("")
  print("The skeleton seems weakened ...")
  Battle2 = input("Attack or Spare?:")
  if Battle2 == "Attack" or Battle2 == "attack":
    print("You swing at the skeleton with your sword, shattering his bones and making him fall to the floor")
    print("")
    print("Skeleton: I tried to warn you...") 
  elif Battle2 == "Spare" or Battle2 == "spare":
    print("")
    print("Skeleton: I can't allow you to pass, I'm actually trying to help you. Please, turn around...") 
    state = "Battle3"
def Battle3():
  global state
  print("")
  Battle3 = input("You're going to have to defeat him to pass...make the final blow or end you journey...Attack him:")
  if Battle3 == "Attack" or Battle3 == "attack":
    print("")
    print("You use your sword to deliver one last swing to the skeleton, destroying him.") 
    state ="rat"
def rat():
  global state
  print("")
  print("You enter the third, and presumably last room of the hallway, to discover hundreds of rats, with one large rat with a crown on his head. It immediately lunges at you.") 
  state = "rat2"
def rat2():
  global state
  print("")
  rat2 = input("Attack the rat:")
  if rat2 == "Attack" or rat2 == "attack":
    print("You swing at the the rat with your sword, only to have him dodge your attack, and then whip you with his tail.")
    state = "rat3"
  elif rat2 == "Run" or rat2 == "run":
    print("")
    print("You ran away, never to return. GAME OVER") 
    state = "ReadyToStart"
def rat3():
  global state
  print("")
  rat3 = input("Attack or run?:")
  if rat3 == "Attack" or rat3 == "attack":
    print("You swing at the the rat again with your sword, and it strikes him in the side,heavily damaging him.")
    print("")
    state = "rat4"
    print("") 
  elif rat3 == "Run" or rat3 == "run":
    print("")
    print("You ran away, never to return. GAME OVER") 
    state = "ReadyToStart"
def rat4():
  global state
  print("")
  rat3 = input("Attack or run?:")
  if rat3 == "Attack" or rat3 == "attack":
    print("You swing at the the rat for one final time, and it strikes him in the side,leaving him unable to fight. You take the key hanging off his tail. And proceed to the locked door in the main hallway")
    print("")
    state = "hallway2"
  elif rat3 == "Run" or rat3 == "run":
    print("")
    print("You ran away, never to return. GAME OVER") 
    state = "ReadyToStart"
def hallway2():
  global state
  print("")
  print("You unlock the previously locked door using the key you just got. In the center of the room, there is a knight made of obsidian with a steel longsword, wearing your fathers necklace. Which do you reach for first?")
  print("")
  hallway2 = input("Take the necklace or reach for the sword? N or S:  ")
  if hallway2 == "N" or hallway2 == "n":
    print("")
    print("You reach for the necklace, but the Knight springs to life, shoving you back.")
    state = "knight"
    print("") 
  elif hallway2 == "S" or hallway2 == "s":
    print("")
    print("You reach for the sword and take it out of his grip. The knight then slowly rises, drawing another sword from his side.") 
    state = "knight"   
def knight():
  global state
  print("")
  print("The knight prepares to swing it's sword at you, that armor of his looks pretty durable.")
  print("")
  knight = input("Do you dodge or attack? D or A:")
  if knight == "d" or knight == "D":
    print("You roll out of the way of his attack, you spot a chance to attack it in the back while he's turned away.")
    print("")
    state = "knight2"
  elif knight == "a" or knight == "A":
    print("You try to attack, but your sword breaks under the resistance of it's armor. It then swings his sword at you.")
    print("")
    print("GAME OVER")
    print("")
    state = "intro"
def knight2():
  global state
  knight2 = input("Do you attack or run while his back it turned?:")
  if knight2 == "attack":
    print("")
    print("You stab your sword onto it's weakpoint, killing it.")
    print("YOU WIN")
    state = "intro"
  elif knight2 == "run":
    print("")
    print("You ran away, never to return. GAME OVER") 
    state = "intro"

while(1):
  if state == "intro":
    intro()
  elif state == "ReadyToStart":
    ReadyToStart()
  elif state == "ButtonRoom":
    ButtonRoom()
  elif state == "SlimeFight":
    SlimeFight()
  elif state == "Hallway1":
    Hallway1()
  elif state == "MirrorRoom":
    MirrorRoom()
  elif state == "MirrorOpen":
    MirrorOpen()
  elif state == "Chest1":
    Chest1()
  elif state == "Pineapple1":
    Pineapple1()
  elif state == "Pineapple2":
    Pineapple2()
  elif state == "Skeleton":
    Skeleton()
  elif state == "Battle2":
    Battle2()
  elif state == "Fightcranman":
    Fightcranman()
  elif state == "Battle3":
    Battle3()
  elif state == "rat":
    rat()
  elif state == "rat2":
    rat2()
  elif state =="rat3":
    rat3()
  elif state == "rat4":
    rat4()
  elif state == "hallway2":
    hallway2()
  elif state == "knight":
    knight()
  elif state =="knight2":
    knight2()
idcount = 0
loginid = 0
def helptext():
  print("Hello, you can use the following commands to check your balance, make a deposit, a withdraw, or quit the program.")
  print("balance - Displays your balance.")
  print("deposit - Asks you the amount you would like to deposit.")
  print("withdraw - Asks you the amount you would like to withdrawal.")
  print("quit - Quits the program.")
  print("help - Explains the scenarios.")
def login():
  global loginid
  global idcount
  global accbalance
  while idcount != 4:
    print("There are currently 4 accounts: 1111, 2222, 3333, and 4444")
    try:
      loginid = float(input("Hello. Please enter your 4-digit code:"))
    except:
      print("Invalid Input, dummy")
      loginid = 0
    if loginid == 1111:
      accbalance = 10000
      idcount = 4
    elif loginid == 2222:
      accbalance = 5
      idcount = 4
    elif loginid == 3333:
      accbalance = 20
      idcount = 4
    elif loginid == 4444:
      accbalance = 46
      idcount = 4
    else:
      print("Unknown account, dummy")
def atm():
  global action
  global accbalance
  while action != 'quit':
    action = input("What would you like to do?:")
    if action == 'balance':
      print("Your balance is... $", accbalance, '!')
    elif action == 'deposit':
      print("Please enter the amount you would like to deposit.")
      try:
        depositammount = float(input("$ "))
      except:
        print("Invalid Input.")
        depositamount = 0
      accbalance = accbalance + depositammount
    elif action == 'withdraw':
      print("Please enter the amount you would like to withdraw.")
      try:
        withdrawammount = float(input("$ "))
      except:
        print("Invalid Input.")
        withdrawammount = 0
      accbalance = accbalance - withdrawammount
    elif action == 'help':
      helptext()
    elif action == 'quit':
      print("Goodbye!")
    else:
      print("Invalid Command.")
action = ''
login()
helptext()
atm()
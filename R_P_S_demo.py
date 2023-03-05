# ounter = 0
# sump = 0
# while True:
 #   number = input("please enter an integer number")
  #  if number.lower() == 'q' or number.lower() == 'quit':
   #     break
    #if not number.isdigit():
     #   continue
    #else:
     #   counter = counter + 1
      #  sump = sump + int(number)
#print(f'the average = {sump / counter}')

Listgameforuser = ['rock','paper','scissor','r','p','s']
Listgameforpc = ['rock','paper','scissor']
wingametuple_for_pc = (['rock','scissor'],['rock','s'],
                       ['paper','rock'],['paper','r'],
                       ['scissor','paper'],['scissor','p'])
wingametuple_for_user = (['scissor','rock'],['scissor','r'],
                         ['rock','paper'],['rock','p'],
                         ['paper','scissor'], ['paper','s'])
import random
while True:
    number = input("please enter your round game")
    if number.lower() == 'q' or number.lower() == 'quit':
        print('thanks for playing')
        break
    if not number.isdigit():
        print('please enter an integer number')
        continue

    else:
        computerscore = 0
        userscore = 0
        for i in range(1, int(number)):
                userchoice = input('please enter your choice:')
                if userchoice.lower == 'q' or userchoice.lower == 'quit':
                    print('thanks for playing')
                    break
                else:
                    for word in userchoice.split(" "):
                        if word.lower() in Listgameforuser:
                            print(f'your choice is:{word}')
                            break
                        else:
                            print('please enter an appropriate answer')
                            continue
                    computerchoice = random.choice(Listgameforpc)
                    if [computerchoice,userchoice.lower()] in wingametuple_for_user:
                        userscore = userscore + 1
                    elif [computerchoice, userchoice.lower()] in wingametuple_for_pc:
                        computerscore = computerscore + 1

        print(f'Congradulation you win:{userscore}' if userscore > computerscore else
              f"I'm so sorry you loose:{userscore}" if computerscore > userscore else
              f"you'r both win:{userscore}" if computerscore == userscore else "")





































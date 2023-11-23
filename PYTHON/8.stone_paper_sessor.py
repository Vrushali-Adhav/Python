'''
   Program Name           : STONE - PAPER - SCISSOR GAME with Computer
   Programming Language   : Python
   Programmer's Name      : Adhav Vrushali Abasaheb
   Date                   : 9 Aug 2022

   Rules of game:
        1.same-same choises =game drop
        2.stone-paper=paper
        3.stone-scissor=stone
        4.paper-stone=paper
        5.paper-scissor=scisssoe
        6.scissor-paper=scissor
        7.scissor-stone=stone

   
   
'''



#ask user how many time to play

times=int(input("how many times you want to play"))
#use for loop till user want to play game will play

for i in range(times):
    
    #show choise to user
    
    print("0 for Stone")
    print("1 for paper")
    print("2 for sissor")
    print("3 for exit")
    
    user=int(input("please enter your choise in numbers"))
    
    #take choise of computer so use random package
    
    import random
    computer= random.randint(0,3)
    
    #print computer choise
    
    print("computer {}".format(computer))
    
    #if two choises are same game will stop
    
    if user==computer:
        
        print("Sorry Game Drop Play again")
        
    #scissor pair start

        
   #user=scissor computer=stone
        
    elif((user==2)and(computer==0)):
        print("computer won the GAME")
        stone = '''
             _______
          ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
                 '''
        print("stone=\n {}".format(stone))
        
     #user=scissor computer=paper
        
    elif (user==2)and(computer==1):
        print("user won the game")
        scissors = '''
                    _______
                ---'   ____)____
                          ______)
                       __________)
                      (____)
                ---.__(___)
            '''



















        
        print(" scissor=\n{}".format(scissors))
        
           
     #user=paper computer=scissors
        
    elif (user==1)and(computer==2):
        print("computer won the GAME")
        scissors = '''
                    _______
                ---'   ____)____
                          ______)
                       __________)
                      (____)
                ---.__(___)
            '''
        print("scissor=\n {}".format(scissors))
        
     #user=stone computer=scissor
        
    elif((user==0)and(computer==2)):
        print("user won the GAME")
        stone = '''
             _______
          ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
                 '''
        print("stone=\n {}".format(stone))
        
        #end with scissor pair
        
     #starting of stone pairs
        
    #user=stone computer=scissor
        
    elif ((user==0)and(computer==2)):
        print("user won the game")
        stone = '''
             _______
          ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
                 '''

        print("stone=\n {}".format(stone))


     #user=stone computer=paper
        
    elif((user==0)and(computer==1)):
        print("computer won the game")
        paper = '''
              _______
    ---'            )  _ ____
                      ____ __)
                      _____ __)
                      ______ _)
           ---.  _________ _)

           '''
        print("paper=\n {}".format(paper))
        
       #user=scissor computer =stone
        
    elif ((user==2)and(computer==0)):
        print("computer won the game")

        stone = '''
             _______
          ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
                 '''
        print("stone= \n{}".format(stone))
        
                                       
    #user=paper computer=stone
        
    elif(user==1)and(computer==0):
        
        print("user won the game")
        paper = '''
              _______
    ---'            )  _ ____
                      ____ __)
                      _____ __)
                      ______ _)
           ---.  _________ _)

           '''
        print(" paper=\n{}".format(paper))
        
        #end of stone pair
        
        #staring of scissor pair
        
        #user=scissor computer=paper
        
    elif(user==2)and (computer==1):
        scissors = '''
                    _______
                ---'   ____)____
                          ______)
                       __________)
                      (____)
                ---.__(___)
            '''
        print(" scissor=\n{}".format(scissors))
        print("user won the game")
        
      #user =scissor computer=stone
        
    elif(user ==2)and (computer==0):
        print("computer won the game")
        stone = '''
             _______
          ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
                 '''
        print("stone= \n{}".format(stone))
        
     #user=paper computer=scissor
        
    elif(user==1)and (computer==2):
        print("computer won the game")
        scissors = '''
                    _______
                ---'   ____)____
                          ______)
                       __________)
                      (____)
                ---.__(___)
            '''
        print("scissor= \n{}".format(scissors))
        
    #user =stone computer=scissor
        
    elif(user==0)and (computer==2):
        print("user won the game")
        stone = '''
             _______
          ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
                 '''
        print(" stone=\n{}".format(stone))
        
        #end of scissor pair
        
        #start of paper pair
        
        #user=stone computer=paper
        
    elif(user==0)and(user==1):
        print("computer won the game")
        paper = '''
              _______
    ---'            )  _ ____
                      ____ __)
                      _____ __)
                      ______ _)
           ---.  _________ _)

           '''
        print(" paper=\n{}".format(paper))
        
    #user=scissor computer=paper
        
    elif(user==2)and(user==1):
        print("user  won the game")
        scissors = '''
                    _______
                ---'   ____)____
                          ______)
                       __________)
                      (____)
                ---.__(___)
            '''
        print("scissor= \n{}".format(scissors))
        
        #user=paper computer=scissor
        
    elif(user==1)and (computer==2):
        print("computer won the game")
        scissors = '''
                    _______
                ---'   ____)____
                          ______)
                       __________)
                      (____)
                ---.__(___)
            '''
        print("scissor=\n {}".format(scissors))
        
    #user=paper computer=stone
        
    elif(user==1)and (computer==0):
        print("user won the game")
        paper = '''
              _______
    ---'            )  _ ____
                      ____ __)
                      _____ __)
                      ______ _)
           ---.  _________ _)

           '''
        print(" paper=\n{}".format(paper))    
    else:
        
        #print("sorry invalid choise")
        
        print("Thanks for Playing")
        continue
print("\n\n ")  
    
        
                                       

        
    




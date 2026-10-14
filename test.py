# HW, MM, CK, 7, Final Game
# Caleb King
start = input("Would you like to start the game? ").strip().capitalize().lower()
if start == "yes":
    first_choice = input("You start at ucas.\nWould you like to enter the AC, or UVU: ").strip().upper()
elif start == "no":
    print("Okay, Bye.")
else:
     print("Invalid Answer.\nYour not the alpha") # Marco


if first_choice == "UVU":
    print("As you walk to UVU, you see Marco sprint past.") # Caleb King
    user = input("You walk up to the front desk and see Marco. You ask him why he is there.\nHe says that he works there and asks what your name is: ").strip().capitalize() # Hazel West
    bowling = input(f"Nice to meet you {user}\nWould you like to go bowling?\nYes(y) or No(n): ").strip().lower()
    if bowling == "y":
        print("Marco asks for your UVU ID, but you don't have one.")
        to_ucas = input("Do you go back to ucas(u), or do you stay at UVU(v)").strip().lower()
        if to_ucas == "v":
             stay = input("As you walk around UVU you hear Marco's scream\nDo you go back to try and help(h), or keep walking(w)").strip().lower()
             if stay == "h":
                  print("You go back to help Marco, but you see a spider monster turn the corner and eat you.\nYou Died!")
             elif stay == "w":
                  print("You keep walking, but then you see a spider monster turn the corner\nThe monster starts chasing you until it gets to you\nYou Died!")
             else:
                  print("Invalid Answer.\nYour not the alpha") # Marco
        elif to_ucas == "u":
            leave_uvu = input("As you leave UVU you hear Marco's scream\nYou made it to Ucas\nWould you like to go to the therapy tree(t) or the AC(a)").strip().lower()
            if leave_uvu == "a":
                 print("You go to the AC\nBut you fell like you've been followed\nWhen you turn around a giant spider monster lunges at you\nYou Died!")
            elif leave_uvu == "t":
                 distract_guarde = input("You go to check on the therapy tree, but a weird spider monster is there guarding it.\nDo you charge(c) the spider monster or do you tuant(t) it.").strip().lower()
                 if distract_guarde == "c":
                      print("You start to charge the spider monster\nIt also starts to charge at you\nWhen you two clash the monster instantly defeats you\nYou Died!")
                 elif distract_guarde == "t":
                      taunt = input("You taunt the monster\nThe monster notices and starts to chase you\nYou go around the AC and to the tree\nAs the monster comes around and charges at you, you climb the tree.\nYou find a UVU card in the tree\nAfter waiting...\nAnd waiting...\nAnd more waiting...\n The monster leaves you alone and starts to wander off\nDo you follow(f) the monster, or do you sprint to UVU(u)").strip().lower()
                      if taunt == "v":
                           print("You sprint to the UVU building\nRight before you get there the spider monster jumps out from its hiding place and catches you\nYou Died!")
                      elif taunt == "f":
                           follow = input("You follow the spider to UVU\nAfter a while you lose track of the spider\nBut you find Marco\nMarco said that he barely survived the spider attacking him\nHe asks if you want to go bowling no that you have a UVU card\nDo you say yes(y), or no(n)").strip().lower()
                           if follow == "n":
                                print("Marco gets really mad at you for saying now\nHe picks up something heavy and throws it at you\nYou Died!")
                           elif follow == "y":
                                final_choice1 = input("Marco gets super excited and you go to the bowling area\nAfter you win a couple rounds you can't find Marco\nHe vanished\nAfter waiting a while, you see the spider monster\nWill you try to negotiate(n) with the spider, or try to fight(f) it")
                                if final_choice1 == "n":
                                     print("After trying to negotiate, the spider looks confused\nThe spider lunges at you\nYou Died!")
                                elif final_choice1 == "f":
                                     print(f"You pick up a bowling ball and chuck it\nIt hits the spider right in its head\nThe spider Monster falls to the ground, but it starts to change\nIts body transformed into Marco!\nMarco says,\nNow look what you've done now {user}\nYou Win!\nbut at what cost.")
                                else:
                                     print("Invalid Answer.\nYour not the alpha") # Marco
                           else:
                                print("Invalid Answer.\nYour not the alpha") # Marco
                      else:
                           print("Invalid Answer.\nYour not the alpha") # Marco
                 else:
                      print("Invalid Answer.\nYour not the alpha") # Marco
            else:
                 print("Invalid Answer.\nYour not the alpha") # Marco
        else:
             print("Invalid Answer.\nYour not the alpha") # Marco
    elif bowling == "n":
         print("Marco gets so mad at you that he picks up the nearest heavy object and throws it at you\nYou Died!")
# Caleb King all above         
#AC Pathway -> Hazel West
elif first_choice == "AC":
    print("You walk into the AC\nEverything seems quiet...\nToo quiet...\nYou listen closely and you hear a faint hiss above you.") # Caleb King
    drop_down = input("Do you look(l) up or do you keep walking(w): ").strip().lower() # Caleb King
    if drop_down == "l": # Caleb King
        user2 = input("As soon as you look up you see a giant spider fall on you...\nYou wake up and see your friend Marco sitting in the corner of the AC\nHe asks what your name is.\nWhat do you tell him: ").strip().capitalize() # Caleb King
        print(f"Well Hiya {user2}")
        story = input("Marco talks about how he saved you from that spider monster\nHe tells you all about his heroic fight and did not stop until his story was finished perfectly.\nHe tells you that he knows a place where we can hide from that hideous monster.\nDo you follow(f) him, or don't(d) follow him?")
        if story == "d":
            outside = input("You kindly decline Marco and instead walk outside. You see the spider coming towards you! Do you want to fight(f) the spider of run(r)?")
            if outside == "r":
                tree = input("You run from the spider all the way over to the Therapy tree and climb up before the spider can get you.\nYou are going to be stuck up there if you don't do something...\nDo you want to jump on to the spider and tackle(t) it or grab a tree branch(b) to hit with?")
                if tree == "b":
                    print("You grab the nearest branch and jump out of the tree onto the spider and start hitting it over and over.\nThe spider slowly backs away, swaying from dizziness and calapses to the ground. You then realize that the spider transforms into.....\nMARCO?!?!\nThe End! You win!!!")
                elif tree == "t":
                    print("You jump out of the tree and try to tackle the spider, only ending up flopped on your back and squashed by the spider. Game over!!!")
                else:
                    print("Invalid Answer.\nYou are not the alpha.") # Marco
            elif outside == "f":
                print("You run at the spider, throw a few punches, and the spider laughs at you!\n He knocks you out with one of his hairy legs. Game over!!! ")
            else:
                print("Invalid Answer.\nYou are not the alpha.") # Marco
                
        elif story == "f":
                print("You follow Marco behind the building and the spider drops on your head. Game over!!!")
        else:
            print("Invalid Answer.\nYou are not the alpha.") # Marco
    elif drop_down == "w":
        reflection = input("You keep walking and see a giant creepy spider in the window's reflection! Do you choose to run(r) or fight(f)? ")
        if reflection == "r":
            print("You start running and the spider catches you! Game over!!!")
        elif reflection == "f":
            print ("You turn around and the spider is there, but before you can attack it, you get bit. Game over!!!")
        else:
            print("Invalid Answer.\nYou are not the alpha.") # Marco
    else:
        print("Invalid Answer.\nYou are not the alpha.") # Marco
else:
    print("Invalid Answer.\nYou are not the alpha.") # Marco

    # Caleb debugged Hazel's side
    # Marco chose who the spider was
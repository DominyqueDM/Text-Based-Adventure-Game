bag = []
gamePrompt = input("Do you choose to accept the mission (though you have no idea what it is yet) y/n?").lower().strip()

if gamePrompt == "n":
    print("Then don't run the program dude")

else:
    print("Amazing! Let's set the scene")
    print()
    print("You are in an enchanted forest- my excuse if things don't make sense. Your mission is to defeat the "
          "leader of the Trolls so that you can cross the bridge to get those brownies from your favourite shop over "
          "the lake. "
          "Don't judge me, I was hungry while writing this. You will have the chance to pick up objects along the way"
          "that will either aid (or not) you for the battle. You will have to make many decisions throughout the game "
          "so choose carefully. Certain paths will either bring harm/ necessities. Good luck")
    print()

    firstItem = input("You look around you and are allowed to pick 1 item to place in your bag. Do you choose the: "
                      "apple, rock or stick?").lower().strip()
    bag.insert(0, firstItem)

    print()
    print("Item stored!:", firstItem)
    print()
    direction1 = input("You come across a fork in the footpath, do you want to go right or left?").lower().strip()

    if direction1 == "right":
        print("Up ahead you spot a dagger stuck in a rock (classic). Do you want to give it a shot at pulling it out?")
        answer = input("yes/no?").lower().strip()
        if answer == "no":
            print("Could you be anymore of a wimp?")
        else:
            print("Nice going! After falling on your ass about twice, you've managed to free the sword!")
            print("The sword has been added to your bag!")
            bag.insert(0, "sword")
            print()

    else:
        print("There's a rubber band on the ground. You place it in your bag- who knows, might come in handy")
        bag.insert(0, "rubber band")
        print()
        answer = input(
            "You see a shrub of delicious berries and you're so hungry! Do you eat the berries? yes/no").lower().strip()
        if answer == "yes":
            print("Nice going- you're dead")
            exit()
        else:
            print("Finally! You've made a great decision and you'll live to tell the tale")
        print()
    print("Reminder of what's in your bag:", bag)

    print()
    print("You've reached the bridge. Everything seems normal until you hear a grumbling noise and the "
          "floor begins shaking under you. You look up only to meet the eyes of the Troll you ill have to "
          "defeat if you wanna get those delicious treats.")
    print()
    choice = input("The beast growls and demands a fight. What do you want to do: charge at the beast or use something "
                   "in your bag? (1/2)")
    if choice == 1:
        print("My dude... did you really think that was a good idea. You dead.")
        exit()
    else:
        print("Great choice my dude.")
        print()
        bagChoice1 = input("What would you like to use?")
        if bagChoice1 == "apple":
            print("Instead of offering the Troll the apple- you ate it. Great going. Death.")
            exit()
        if bagChoice1 == "rock":
            print("You've got a great throwing arm! You've hit the beast right on the noggin and he goes down for the "
                  "count. "
                  "Enjoy those brownies!")
            exit()
        if bagChoice1 == "stick":
            print("Like an Olympic champ, you use the stick to do a pole vault move jumping right over"
                  "the beast! Well done! Enjoy those brownies.")
            exit()
        if bagChoice1 == "rubber band":
            print("You aim to shoot the band at the beast but you've somehow managed to hit yourself"
                  "with it. You go down for the count. The beast has eaten you. Can you blame him? "
                  "You were just lying there. Death. ")
            exit()
        if bagChoice1 == "sword":
            print("You charge at the beast armed with your sword stabbing hit right in the gut! He falls"
                  "to the floor yelling in pain. You've beasted the beast! Enjoy your brownies")
            exit()

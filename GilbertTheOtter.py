brains = 5
brawn = 5
bolsh = 5

has_sword = False
has_stick = False
has_power = False

fav_food = "fish"
fav_animal = "otter"
fav_colour = "ble"

choice = 0

### Choices template ####
###blah blah
#choice = input()
#    if choice == "1":
#        print("placeholder text 1")
#    elif choice == "2":
#        print("placeholder text 2")
#    elif choice == "3":
#        print("placeholder text 3")
#    elif choice == "4":
#        print("placeholder text 4")
#    else:
#        print("\nPlease select from either choice 1, 2, 3 or 4")
# placeholder comment

#Forest walk
def forest_walk():
    print("As you walk through the woods toward home, your hackles raise across your neck.")
    print("Something is approaching.")
    

#Third choice
def third_choice():
            print("\nWhat will you do?")
            print("1. Bravely stay and answer the questions.")
            print("2. Run away as fast as you can.")
            choice = input()
            if choice == "1":
                print("\"I will answer your questions!\" you proclaim to the voice")
                print("Its booming laughter quietens a little and it speaks out to you.")
                print("\"What is your favourite food?\"", end=" ")
                global fav_food
                fav_food = input()
                print("\"Good, good. Now, tell me, what is your favourite animal?\"", end=" ")
                global fav_animal
                fav_animal = input()
                print("\"Yes, very good, Now, finally, tell me. What is your favourite colour?\"", end=" ")
                global fav_colour
                fav_colour = input()
                print("\"Aha! fantastic! You will make a fine vessel!\"")
                print("With burst of luminous " + fav_colour + " coloured light, the sword floats out of the ground before you.")
                print("Shining ever brighter, you have no choice but to close your little otter eyes lest they are blinded.")
                print("You feel yourself rising from the ground as well, as a warmth that smells of " + fav_food + " radiates out,")
                print("permeating the forest.")
                print("\nIn your mind and in the air, faint animal noises, distinctly similar to " + fav_animal + " can be heard.")
                print("Eventually, the bright light and sensations subside and you are lowered to the floor.")
                print("The sword is gone, and you can tell that some aspect of its magic is infused with your body.")
                print("Stunned, you wait some time in quiet reflection before continuing your journey home through the forest")
                global has_power
                has_power = True
                global bolsh
                bolsh += 1
                forest_walk()
            elif choice == "2":
                print("\nYou run away as fast as you can, leaving the loud scary voice behind you!")
                print("You run and run, heading towards home, until you're all puffed out, and have to")
                print("slow to a normal walking pace.")
                forest_walk()
            else: 
                print("please select either choice 1 or 2.")  
                third_choice()  


#Second choice
def second_choice():
    print("\nWhat will you do?")
    print("(Brains) 1. Poke at the sword with a nearby stick, to see how stuck it is.")
    print("(Brawn)  2. Reach out and grab the sword, pulling on it as hard as you can. ")
    print("(Bolsh)  3. Shout aloud \"I am going to take this sword!\" to see if the owner is nearby.")
    choice = input()
    if choice == "1":
        print("\nYou poke at the sword with a sturdy looking stick.")
        print("Initially, nothing happens, but as your confidence grows and you tap it a second time,")
        print("you feel a jolt as a magical crackle of lightning leaps from the sword to the stick.")
        print("Unable to let go you, you are overcome with wonder as the mysterious glimmering leaves the sword")
        print("and encases the stick. All over its surface you can see mysterious lettering and mystical runes,")
        print("lapping against each other in a watery ethereal dance.")
        print("The sword in the ground crumbles into dust.")
        global has_stick
        has_stick = True
        global brains
        brains += 1
        forest_walk()
    elif choice == "2":
        print("\nYou stride boldly forward and grasp the hilt of the sword.")
        print("As you grasp it, you can feel a sudden lightness shift in its weight.")
        print("Seemingly of its own volition, the sword shakes in the earth and leaps from its resting place!")
        print("Your arm, which has never wielded a sword before, has a sense of familiarity with the weapon,")
        print("and, as you give it a few test swings in the air, the certain knowledge that if you are defending")
        print("the innocent, your aim will always strike true!")
        global has_sword
        has_sword = True
        global brawn
        brawn += 1
        forest_walk()
    elif choice == "3":
        print("\nWith a deep intake of breath, you bellow at the top of your lungs \"I am Gilbert the Otter\"!")
        print("If no-one should claim this weapon, I would have its power for mine own!\"")
        print("Almost immediately, you hear an answering voice, seeming to come from everywhere, nowhere, but")
        print("also from within your own head!")
        print("IF YOU LITTLE OTTER WOULDST CHALLENGE ME, THEN ANSWER ME THESE QUESTIONS THREE!")
        third_choice()
        forest_walk()
    else:
        print("\nPlease select from either choice 1, 2 or 3.")
        second_choice()


#First choice
def first_choice():
    print("\nWhat will you do?")
    print("1. Investigate the sparkle.")
    print("2. Ignore the sparkle and carry on past.")
    choice = input()
    if choice == "1":
        print("\nYou move through the foliage, closer to the glimmering light.")
        print("Once you are within a few feet, you can see that the glimmer and shimmer")
        print("is coming from a sword buried almost the full depth of its blade into the dirt.")
        second_choice()
    elif choice == "2":
        print("\nYou are in a rush to get home. You leave the shimmering light behind you and focus")
        print("on much more important tasks, such as tonight's dinner and weatherproofing your cottage.")
        print("You are a good little otter. Enjoy your dinner and safe warm house.")
        print("\nCongratulations, you have unlocked 'The Good Little Otter' ending!")
    else:
        print("\nPlease select from either choice 1 or choice 2.")
        first_choice()

#Introduction
def game_start():
    print("\nOnce upon a time, there was a little otter named Gilbert. That is you.")
    print("You are wandering along in the forest, your green coat tails swishing this way and that,")
    print("whipping into ripe dandelions and casting their seeds all about the rough path behind you.")
    print("As the sun streams down through the trees, you catch a glint of something bright in the underbrush.")
    first_choice()
    
   

game_start()
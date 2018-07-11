import random


# DAMAGE GIVEN TO ANY ENEMY WITH WEAPON
def weaponDamage(W):
    crit = random.randint(1, 5) #CHANCE OF A CRITICAL STRIKE
    if (W == "Sword"):
        Damage = random.randint(80, 95)
    elif (W == "Bow"):
        Damage = random.randint(65, 80)
    elif (W == "Axe"):
        Damage = random.randint(95, 120)
    if (crit == 3):
        print "CRITICAL HIT!"
        return (int)(Damage * 1.25)
    else:
        return Damage

# DAMAGE GIVEN TO ANY ENEMY WITH MAGIC
def magicDamage(M):
    if (M == 'Ice'):
        Damage = random.randint(73, 77)
    elif (M == 'Lightning'):
        Damage = random.randint(82, 89)
    elif (M == 'Fire'):
        Damage = random.randint(95, 120)
    return Damage

# ENEMY STATUS
def status(M):
    mCrit = random.randint(1,3) #CHANCE OF INFLICTING A STATUS ON AN ENEMY
    if (mCrit == 2):
        print "CRITICAL STRIKE"
        if (M == 'Ice'):
            print "You have cast a Freeze curse onto the creature"
            return 'FREEZE'
        elif (M == 'Lightning'):
            print "You have cast a stun curse onto the creature"
            return 'STUN'
        elif (M == 'Fire'):
            print "You have cast a burn curse onto the creature"
            return 'BURN'
    else:
        return "Normal"

def bossReturns(bossStatus):
    if (bossStatus != 'FREEZE'):
        return 'Normal'

# FIGHT WITH ANYTHING
def bossFight(BossHealth, PlayerHealth, Mana, W, M, DR, bossName, a, b, c, d):
    bossStatus = 'Normal'
    pStatus = 'Normal'
    heal = True
    while (PlayerHealth > 0 and BossHealth > 0):
        question = raw_input("How will you attack the creature (W M HEAL): ")
        dodge = random.randint(1,DR)
        if (pStatus == 'STUN'):
            print "You are under a stun curse. You cannot do anything."
        else:
            while (question != 30202012):
                if (question == 'W' or question == 'w'):
                    break
                elif (question == 'M' or question == 'm'):
                    if (Mana > 0):
                        break
                    else:
                        print "\nYou do not have enough mana to cast any magic spells"
                        question = raw_input("How will you attack the creature (W HEAL): ")
                elif (question == 'HEAL'):
                    if (heal == True):
                        break
                    else:
                        print "\nI've already healed you once this battle. I cannot do it again"
                        question = raw_input("How will you attack the creature (W M): ")
                else:
                    print "\nI'm afraid you do not have that option"
                    question = raw_input("How will you attack the creature (W M HEAL): ")
            if (question == 'W' or question == 'w'):
                if (bossStatus == 'FREEZE'):
                    Damage = weaponDamage(W) * 1.5
                else:
                    Damage = weaponDamage(W)
                print "The enemy takes",Damage,"damage!"
                BossHealth = BossHealth - Damage
            elif (question == 'M' or question == 'm'):
                Mana = Mana - 1
                Damage = magicDamage(M)
                bossStatus = status(M)
                print "The enemy takes",Damage,"damage!"
                BossHealth = BossHealth - Damage
            else:
                PlayerHealth = 500
                print "I have fully restored your health"
                print "You have",PlayerHealth,"health left"
                pStatus = 'Normal'
                heal = False
        if (bossName == 'CATIPILLAR'):
            break
        if (pStatus == 'STUN'):
            pStatus = 'Normal'
        if (bossStatus == 'STUN'):
            print "The creature is stunned and does nothing"
        elif (dodge == 1):
            print "You dodged the enemy's attack."
        else:
            #THE GATKEEPER FIGHT
            if (bossName == 'KNIGHT'):
                print
                print "The Knight attacks you."
                PDamage = random.randint(a,b)
            #THE SPIDER FIGHT
            elif (bossName == 'SPIDER'):
                attackChoice = random.randint(1,2)
                if (attackChoice == 1):
                    if (pStatus != 'POISON'):
                        print
                        print "The spider bites you!"
                        print "You are poisoned by it"
                        pStatus = 'POISON'
                        PDamage = random.randint(a,b)
                elif (attackChoice == 2):
                    print
                    print "The spider spits a ball of web at you"
                    PDamage = random.randint(c,d)
            #THE DRAGON FIGHT
            elif (bossName == 'DRAGON'):
                attackChoice = random.randint(1,2)
                if (attackChoice == 1):
                    print
                    print "The dragon envelops you in a fire blast"
                    PDamage = random.randint(a,b)
                    if (pStatus == 'Normal'):
                        pFire = random.randint(1,2)
                        if (pFire == 2):
                            print "CURSE"
                            print "You have been inflicted with a burn curse"
                            pStatus = 'BURN'
                elif (attackChoice == 2):
                    print
                    print "The dragon hits you with it's tail"
                    PDamage = random.randint(c,d)
                    if (pStatus == 'Normal'):
                        pStun = random.randint(1,3)
                        if (pStun == 2):
                            print "CURSE!"
                            print "You have been inflicted with a stun curse"
                            pStatus = 'STUN'
            if (bossStatus == 'FREEZE'):
                PDamage = (int)(PDamage/2)
            print "You take",PDamage,"damage!"
            PlayerHealth = PlayerHealth - PDamage
    #POST BATTLE DAMAGES
        ##FOR BOSS
        if (bossStatus == 'BURN'):
            burnDamage = random.randint(81,88)
            print "The",bossName,"takes",burnDamage,"damage."
            BossHealth = BossHealth - random.randint(81,88)
        if (bossStatus != 'FREEZE'):
            bossStatus = 'Normal'
        ##FOR PLAYER
        if (pStatus == 'POISON'):
            poison = random.randint(27,39)
            print "You take",poison,"damage from the poison curse."
            PlayerHealth = PlayerHealth - poison
        if (pStatus == 'BURN'):
            burn = random.randint(41,47)
            print "You take",burn,"damage from the burn curse."
            PlayerHealth = PlayerHealth - burn
            pStatus = 'Normal'
        if (PlayerHealth > 0):
            print "You have",PlayerHealth,"life left"
        else:
            print "You have no life left"
            break
        print "You have",Mana,"Mana left"
        print
    return PlayerHealth

# PART 1
def sectionOne(PlayerHealth, Mana, W, M, DR):
    play = True
    while (play == True):
        print "CHAPTER 1"
        move = raw_input("You find yourself in an old village.")
        print ("Before you move any further, a man steps in your way.")
        print "\nMAN: I know what yer after, kid. And you ain't never gonna get it unless you can get past that knight in the way. Not even a strong man like you got a chance against him in a one on one. Fortunately for you, I know the secret password that'll make sure you never hafta. All it'll cost ya are two outta five a dem mana points a yers. You in?"
        getPassword = raw_input("\nGive this man 2 mana points? (Y N): ") #CHOICE: SACRIFICE MANA TO KNOW THE PASSWORD
        while (getPassword != -2393321345):
            if (getPassword == 'Y' or getPassword == 'y'):
                Mana = Mana - 2
                print "\nYou have",Mana,"mana left"
                print "\nMAN: The password is 'Gilgamesh,' but ya gotta say it loudly. Say it strong, say it proud, and he just might let ya through."
                move = raw_input("The man runs off, and you continue to make your way to the forest.")
                break
            elif (getPassword == 'N' or getPassword == 'n'):
                print "\nMAN: Then I wish you the best of luck"
                move = raw_input("\nThe man runs off, and you continue to make your way to the forest.")
                break
            else:
                print "\nI'm sorry, I don't understand what you mean."
                getPassword = raw_input("Give this man 2 mana points? (Y N): ")
        move = raw_input("\nYou see a pathway leading into the forest. There is a tall, clocked figure blocking the path.")
        password = raw_input("\nGATEKEEPER: What is the password? (Enter Password):")
        move = raw_input("\nGATEKEEPER: Password...")
        if (password == 'GILGAMESH'):
            print "\nGATEKEEPER: Acceptable"
            print "\n The gatekeeper steps aside, and allows you to journey into the forest"
            move = raw_input("\nGUIDE: That was easy. Let's keep moving.")
            break
        else:
            print "\n GATEKEEPER: Unacceptable!"
            print "(The gatekeeper pulls out his tremendous sword, and challenges you to a duel!)"
            PlayerHealth = bossFight(500, PlayerHealth, Mana, W, M, DR, 'KNIGHT', 50, 57, 0, 0)
            if (PlayerHealth > 0):
                print "\nThe gatekeeper declares you worthy as he falls to the ground."
                move = raw_input("\nGUIDE: With that out of the way, let's move on.")
                break
            else:
                print "You failed to complete your journey."
                CONT = raw_input("Would you like to try again?(Y/N): ")
                while (CONT != 2342432):
                    if (CONT == 'Y' or CONT == 'y'):
                        PlayerHealth = 500
                        Mana = 5
                        break
                    elif (CONT == 'N' or CONT == 'n'):
                        print "GAME OVER"
                        PlayerHealth = "GAME OVER"
                        break
                    else:
                        print "I don't understand that answer."
                        CONT = raw_input("Would you like to try again?(Y/N): ")
                if (CONT == 'N' or CONT == 'n'):
                    return 'GAME OVER'
# PART 2: The Spider Fight
def sectionTwo(name, PlayerHealth, Mana, W, M, DR):
    play = True
    while (play == True):
        CONT = "THING"
        print "\n\nCHAPTER 2"
        move = raw_input("\nAs you proceed through the forest, your finding that it truly lives up to it's macabre legacy. Ther air reeks of feces and foul gasses and the stench of rotting corpses of many ugly things.")
        print "\nGUIDE: Hey,",name+"! Look what I found!"
        move = raw_input("You walk over to where the guide is.")
        print "\nGUIDE: This body looks like it's human: a treasure hunter much like you. Or...at least he used to be. He's clearly been dead for a long time."
        getMap = raw_input("\nGUIDE: It also looks like he's holding something. Do you think we should pick it up? (Y,N): ")
        while (getMap != -2393321345):
            if (getMap == 'Y' or getMap == 'y'):
                raw_input("\nGUIDE: Well talk about luck! This man was holding a map to navigate through the forest. In fact, it leads us directly to the ancient temple filled with riches! Let's not waste any more time, and go!")
                break
            elif (getMap == 'N' or getMap == 'n'):
                raw_input("\nGUIDE: You're right. It's really not polite to loot people's corpse. Besides, the less time we stay in this forest the better. Let's just go.")
                break
            else:
                print "I'm sorry, I don't understand what you mean."
                getMap = raw_input("Do you think we should pick up the map? (Y,N): ")
        move = raw_input("\nGUIDE: I said come on. Let's go.")
        move = raw_input("\nGUIDE: Hey, what's the matter? Don't you want to find this treasure?")
        move = raw_input("\nGUIDE: Oh, wait a minute! You're stuck! Looks like while we were looking at that corpse, you accidentally got your feet entangled in some kind of white glop. I'm sorry! Here. Let me try and get you out")
        print "\nGUIDE: Wow, this stuf is sticky. I'm not exactly what you'd call an expert, but this stuff kind of feels like..."
        move = raw_input("You then hear a soft, monstrous hissing from behind you.)")
        move = raw_input("\nGUIDE: Um...I...: ")
        move = raw_input("\nGUIDE: I'd recommend getting your " + W +" ready: ")
        print("(You turn around, and realize that you are entangled in the web of a tremendous mother spider. By intruding on its home, you have awakened it's slumber, and it is very angry. But also very hungry. It impatiently lurches towards you, ready to sink it's teeth into your flesh!")
        print "\nFIGHT\n"
        PlayerHealth = bossFight(500, PlayerHealth, Mana, W, M, DR, 'SPIDER', 61, 69, 42, 47) #INITIATE FIGHT WITH THE SPIDER
        if (PlayerHealth > 0):
            print "The vile arachnid falls over dead."
            if (getMap == 'Y' or getMap == 'y'):
                move = raw_input("\nGUIDE: Now let's see where this map leads us: ")
                return 501
                break
            else:
                move = raw_input("\nGUIDE: Legends say that there is a temple in the east. Let's go that way: ")
                return 500
        else:
            #GAME OVER/RETRY
            print "You failed to complete your journey."
            CONT = raw_input("Would you like to try again?(Y/N): ")
            while (CONT != 2342432):
                if (CONT == 'Y' or CONT == 'y'): #ALLOWS USER TO RETRY SECTION FROM BEGINNING
                    PlayerHealth = 500
                    Mana = 5
                    break
                elif (CONT == 'N' or CONT == 'n'): #ALLOWS USER TO QUIT WHOLE GAME
                    print "GAME OVER"
                    break
                else:
                    print "I don't understand that answer."
                    CONT = raw_input("Would you like to try again?(Y/N): ")
            if (CONT == 'N' or CONT == 'n'):
                return 'GAME OVER'
            
# THE FAKE TEMPLE (You come here if you DON'T get the map)
def fakeTemple(name, PlayerHealth, Mana, W, M, DR):
    print "\n\nCHAPTER 3"
    print ("\n(Venturing through the forest, you find a stone temple)")
    move = raw_input("\nGUIDE: Looks like we found it. It took a bit to get here, but now it's time to get our reward.")
    move = raw_input ("\nInside the temple, you find a dusty open book sitting upon a stone pillar.)")
    move = raw_input ("\nAs you approach the book, you notice that there is a small catipillar sitting on it")
    print "\nFIGHT"
    PlayerHealth = bossFight(3, PlayerHealth, Mana, W, M, DR, 'CATIPILLAR', 0, 0, 0, 0)
    print "The harmless creature dies instantly"
    move = raw_input ("\nGUIDE: Now let's close the book, and see what we have")
    print "(You close the book, and read the words engraved on the cover)"
    move = raw_input ("\nGUIDE: Webster's Dictionary. For there is no treasure greater than knowledge")
    print
    print "\nYOU HAVE COMPLETED YOUR TREASURE QUEST. THANK YOU FOR PLAYING!"
    print "For a more satisfying ending, play again"

# PART 3: THE REAL TEMPLE (You come here if you get the map)
def sectionThree(name, PlayerHealth, Mana, W, M, DR):
    play = True
    while (play == True):
        print "C\n\nHAPTER 3"
        print ("\n(Venturing through the forest, you find a stone temple)")
        move = raw_input("\nGUIDE: Looks like we found it. It took a bit to get here, but now it's time to get our reward.")
        move = raw_input("\n(You enter the temple, and find that the walls are engraved in precious gemstones. They lead towards a tremendous, golden doorway")
        move = raw_input("\nGUIDE: Oh my god! We did it! We found the precious temple!")
        print "(The ground then starts shaking below your feet)"
        move = raw_input("\nVOICE: WHO DARES DISTURB MY PRECIOUS SLUMBER!")
        print "(The golden doors suddenly fly open, and a tremendous dragon emerges from them)"
        move = raw_input("\nGUIDE: Come on, "+ name + "! Let's fight this dragon, and get the reward we deserve!")
        print "\nFIGHT"
        PlayerHealth = bossFight(700, PlayerHealth, Mana, W, M, DR, 'DRAGON', 57, 64, 44, 52)
        if (PlayerHealth > 0):
            move = raw_input("DRAGON: NOOOOOOOOO!")
            print "\n(The dragon's body bursts into flames and swiftly crumble to ash)"
            move = raw_input("GUIDE: We did it! Now let's see what's on the other side!")
            print "You enter through the golden doorway, and find gold coins and gemstones from father than the eye can see!"
            print "Enjoy",name+". For you have earned ever piece of it."
            print
            print "\nYOU HAVE COMPLETED YOUR TREASURE QUEST. THANK YOU FOR PLAYING!"
            break
        else:
            print "You failed to complete your journey."
            CONT = raw_input("Would you like to try again?(Y/N): ")
            while (CONT != 2342432):
                if (CONT == 'Y' or CONT == 'y'):
                    PlayerHealth = 500
                    Mana = 5
                    break
                elif (CONT == 'N' or CONT == 'n'):
                    print "GAME OVER"
                    PlayerHealth = "GAME OVER"
                    break
                else:
                    print "I don't understand that answer."
                    CONT = raw_input("Would you like to try again?(Y/N): ")
            if (CONT == 'N' or CONT == 'n'):
                return 'GAME OVER'
Health = 500
Mana = 5

#NAME INPUT
name = raw_input("Hello, friend. I am your spiritual guide. What is your name: ")
print "Well",name + ", you are about to embark on the journy of a lifetime."
print "There will be danger, of course, but should make it through, you shall walk away very, very rich!"
print "As your spiritual guide, I going to help through this journey. And I shall start by giving you a weapon."

#WEAPON SELECT
Weapon = raw_input("Tell me, would you like to take a sword, a bow, or an axe? (S B A): ")
while (Weapon != 34782):
    if (Weapon == 'B' or Weapon == 'b'):
        W = 'Bow'
        DR = 3 #RATE OF AVOIDING ATTACKS
        break
    elif (Weapon == 'S' or Weapon == 's'):
        W = 'Sword'
        DR = 7 #RATE OF AVOIDING ATTACKS
        break
    elif(Weapon == 'A' or Weapon == 'a'):
        W = 'Axe'
        DR = 10 #RATE OF AVOIDING ATTACKS
        break
    else:
        print "I'm afraid you do not have that option"
        Weapon = raw_input("Tell me, would you like to take a sword, a bow, or an axe? (S B A): ")
print "Excellent."
print "It also looks like you'll be able to take one spellbook with you."
print "I can give you a book that channels the power of ice, lightning or fire."

#MAGIC SELECT
Magic = raw_input("What spellbook would you like to bring? (F I L): ")
while (Magic != 34782):
    if (Magic == 'L' or Magic == 'l'): #Lightning can stun an enemy and prevent them from attacking
        M = 'Lightning'
        break
    elif (Magic == 'F' or Magic == 'f'):  #Fire can do extra damage
        M = 'Fire'
        break
    elif (Magic == 'I' or Magic == 'i'): #Ice can make an enemy weeker and your attacks stronger
        M = 'Ice'
        break
    else:
        print "I'm afraid you do not have that option"
        Magic = raw_input("What spellbook would you like to bring? (F I L): ")
print "A very fine choice!"
print "Now, you are ready to begin your adventure"
print
Play = True
Health = sectionOne(Health, Mana, W, M, DR)
if (Health != 'GAME OVER'):
    Health = sectionTwo(name, 500, Mana, W, M, DR)
if (Health != 'GAME OVER'):
    if (Health == 501):
        sectionThree(name, Health, Mana, W, M, DR)
    else:
        fakeTemple(name, Health, Mana, W, M, DR)

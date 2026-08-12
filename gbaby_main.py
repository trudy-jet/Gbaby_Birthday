import random
import streamlit as st

st.title("HAPPY BIRTHDAY BITCH 💕")
st.write("If you can see this, Gabby Game is ALIVE.")

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = [
            "EOS Lip Balm",
            "Fuzzy Crocs",
            "Push-Up Bra",
            "iPod Touch"
        ]
        self.memories = []
        self.friendship_points = 0
        self.current_era = "Middle School"
        self.soundtrack = []

    def change_health(self, amount):
        self.health += amount

        if self.health > 100:
            self.health = 100

        if self.health < 0:
            self.health = 0

    def add_memory(self, memory):
        if memory not in self.memories:
            self.memories.append(memory)

    def add_friendship_points(self, points):
        self.friendship_points += points


def divider():
    print("\n" + "=" * 55 + "\n")


def pause():
    input("\nPress ENTER to continue...")


def view_stats(player):
    divider()

    print(f"{player.name.upper()}'S STATS")
    print()
    print(f"Health: {player.health}/100")
    print(f"Friendship Points: {player.friendship_points}")
    print(f"Current Era: {player.current_era}")

    print("\nINVENTORY:")
    for item in player.inventory:
        print(f"- {item}")

    print("\nMEMORIES UNLOCKED:")
    if player.memories:
        for memory in player.memories:
            print(f"- {memory}")
    else:
        print("- None yet")

    print("\nFRIENDSHIP SOUNDTRACK:")
    if player.soundtrack:
        for song in player.soundtrack:
            print(f"- {song}")
    else:
        print("- Nothing added yet")

    pause()


def random_middle_school_event(player):
    if random.random() > 0.45:
        return

    events = [
        "noob",
        "phillip",
        "jake"
    ]

    event = random.choice(events)

    divider()

    print("⚠ RANDOM EVENT ⚠")
    print()

    if event == "noob":
        print("Someone calls Kaisha a noob.")
        print()
        print("This is devastating.")

        player.change_health(-10)

        print("\n-10 HP")
        print(f"Health: {player.health}/100")

    elif event == "phillip":
        print("You somehow get Phillip sent to the principal's office.")
        print()
        print("Unfortunately, Phillip has a flight to catch")
        print("for his family's vacation.")
        print()
        print("Phillip does not make the flight.")
        print()
        print("For reasons the game refuses to explain:")

        player.change_health(15)

        print("\n+15 HP")
        print(f"Health: {player.health}/100")

    elif event == "jake":
        print("Jake approaches.")
        print()
        print('"Do you guys wanna hear my car rev?"')
        print()
        print("There is no correct way to respond to this.")

        player.change_health(-5)

        print("\n-5 HP")
        print(f"Health: {player.health}/100")

    pause()


def how_we_met(player):
    divider()

    print("LEVEL 1: THE ORIGIN STORY")
    print()
    print("Year: 7th Grade")
    print("Location: School hallway")
    print("Friendship Status: Complete strangers")
    print()
    print("A girl approaches you.")
    print()
    print('KAISHA: "Do you know where Ms. Woyce\'s class is?"')
    print()

    while True:
        print("[1] Tell her where it is")
        print("[2] Admit you have no idea")
        print("[3] Ignore her and keep walking")

        choice = input("\n> ")

        if choice == "1":
            print("\nYou give Kaisha directions.")
            print("Whether they are correct is irrelevant.")
            print()
            print("NEW CHARACTER DISCOVERED: Kaisha")
            print("+5 Friendship Points")

            player.add_friendship_points(5)
            player.add_memory("How We Met")
            break

        elif choice == "2":
            print("\nYou have absolutely no idea.")
            print()
            print("Excellent.")
            print("Two lost seventh graders.")
            print()
            print("NEW CHARACTER DISCOVERED: Kaisha")
            print("+5 Friendship Points")

            player.add_friendship_points(5)
            player.add_memory("How We Met")
            break

        elif choice == "3":
            print("\nYou walk directly past Kaisha.")
            print()
            print("...")
            print()
            print("TIMELINE ERROR.")
            print("You have just destroyed over a decade of lore.")
            print()
            print("Please stop ruining the birthday game.")
            print()

        else:
            print("\nPick 1, 2, or 3.")

    pause()


def gas_station(player):
    divider()

    print("LEVEL 2: GAS STATION INCIDENT")
    print()
    print("MISSION: Acquire Movie Snacks")
    print("Adult Supervision: None")
    print("Situational Awareness: Concerning")
    print()
    print("You and Kaisha stop at a gas station")
    print("before heading to the movie theater.")
    print()
    print("A strange man approaches.")
    print()
    print('"Are you girls here alone?"')
    print()

    while True:
        print("[1] Say your enormous father is outside")
        print("[2] Refuse to answer")
        print("[3] Tell him the truth")

        choice = input("\n> ")

        if choice == "1":
            print("\nExcellent survival instincts.")
            print()
            print("Unfortunately, this is not historically accurate.")
            print("Try again.")
            print()

        elif choice == "2":
            print("\nResponsible. Sensible. Safe.")
            print()
            print("Unfortunately, neither of you possessed this ability yet.")
            print("Try again.")
            print()

        elif choice == "3":
            print('\n"Yeah!"')
            print()
            print("The strange man now knows you are unsupervised.")
            print()
            print('"Where are you headed?"')
            print()

            while True:
                print("[1] Lie")
                print("[2] Refuse to answer")
                print("[3] Tell him you're going to the movie theater")

                choice_two = input("\n> ")

                if choice_two == "1":
                    print("\nNice attempt.")
                    print("Unfortunately, history says otherwise.")
                    print()

                elif choice_two == "2":
                    print("\nCharacter development arrived too early.")
                    print("Try again.")
                    print()

                elif choice_two == "3":
                    print('\n"The movie theater!"')
                    print()
                    print("Incredible.")
                    print()
                    print("You have now told a strange adult:")
                    print("- You are alone")
                    print("- Where you are going")
                    print()
                    print("ACHIEVEMENT UNLOCKED:")
                    print("How Are We Still Alive?")

                    player.add_friendship_points(5)
                    player.add_memory("Gas Station Incident")

                    if "Gas Station Snacks" not in player.inventory:
                        player.inventory.append("Gas Station Snacks")

                    break

                else:
                    print("\nPick 1, 2, or 3.")

            break

        else:
            print("\nPick 1, 2, or 3.")

    pause()


def mcdonalds(player):
    divider()

    print("LEVEL 3: THE McDONALD'S PILGRIMAGE")
    print()
    print("MISSION: Acquire McDonald's")
    print("Distance: 1 mile")
    print("Transportation: Legs")
    print("Desire For Fries: Extreme")
    print()
    print("There is a McDonald's approximately one mile away.")
    print()
    print("What do you do?")
    print()

    while True:
        print("[1] Begin the pilgrimage")
        print("[2] Ask an adult to drive you")
        print("[3] Decide you don't need McDonald's")

        choice = input("\n> ")

        if choice == "1":
            print("\nTHE PILGRIMAGE BEGINS.")
            print()
            print("One mile.")
            print("On foot.")
            print("For McDonald's.")
            print()
            print("Was it worth it?")
            print()
            print("Obviously.")

            player.add_friendship_points(5)
            player.add_memory("McDonald's Pilgrimage")

            if "Questionably Earned French Fries" not in player.inventory:
                player.inventory.append("Questionably Earned French Fries")

            break

        elif choice == "2":
            print("\nAir conditioning?")
            print("Comfortable seats?")
            print()
            print("Absolutely not.")
            print()
            print("HISTORICAL INACCURACY.")
            print()

        elif choice == "3":
            print("\nYou decide you don't need McDonald's.")
            print()
            print("FATAL ERROR.")
            print("This contradicts adolescent human behavior.")
            print()

        else:
            print("\nPick 1, 2, or 3.")

    pause()


def fifty_shades(player):
    divider()

    print("LEVEL 4: THE FORBIDDEN TEXTS")
    print()
    print("Location: Kaisha's House")
    print("Parental Permission: Absolutely Not")
    print()
    print("You and Kaisha discover a mysterious trilogy.")
    print()
    print("Fifty Shades of Grey.")
    print()
    print("The books belong to Kaisha's mom.")
    print()
    print("What do you do?")
    print()

    while True:
        print("[1] Leave them alone")
        print("[2] Read the back cover and put them back")
        print("[3] Obviously read them together")

        choice = input("\n> ")

        if choice == "1":
            print("\nYou demonstrate maturity and restraint.")
            print()
            print("Who are you?")
            print()
            print("Try again.")
            print()

        elif choice == "2":
            print("\nYou read the back cover.")
            print()
            print("Gabby looks at Kaisha.")
            print("Kaisha looks at Gabby.")
            print()
            print("Yeah, no.")
            print()

        elif choice == "3":
            print("\nFORBIDDEN KNOWLEDGE ACQUIRED.")
            print()
            print("This was perhaps not age-appropriate literature.")
            print()
            print("That did not stop you.")
            print()
            print("ACHIEVEMENT UNLOCKED:")
            print("We Should Not Have Been Reading This")

            player.add_friendship_points(5)
            player.add_memory("The Forbidden Texts")
            break

        else:
            print("\nPick 1, 2, or 3.")

    pause()


def swing_chair(player):
    divider()

    print("LEVEL 5: THE FORBIDDEN CHAIR")
    print()
    print("⚔ BOSS ENCOUNTER ⚔")
    print()
    print("There is a swinging chair in Kaisha's bedroom.")
    print()
    print("There is only one rule:")
    print()
    print("GABBY MAY NOT SIT IN THE CHAIR.")
    print()
    print("The chair swings gently.")
    print()
    print("Temptingly.")
    print()

    while True:
        print("[1] Respect Kaisha's wishes")
        print("[2] Ask politely to sit in it")
        print("[3] Sit in the goddamn chair")

        choice = input("\n> ")

        if choice == "1":
            print("\nYou don't sit in the chair.")
            print()
            print("Kaisha watches suspiciously.")
            print()
            print("You survive.")
            print()
            print("But at what cost?")

            player.add_friendship_points(2)
            player.add_memory("The Forbidden Chair")
            break

        elif choice == "2":
            print('\n"Can I sit in your chair?"')
            print()
            print('KAISHA: "No."')
            print()
            print("END OF NEGOTIATIONS.")

            player.add_memory("The Forbidden Chair")
            break

        elif choice == "3":
            print("\nYou sit.")
            print()
            print("Silence.")
            print()
            print("Kaisha turns around.")
            print()
            print('"GET OUT OF MY CHAIR."')

            player.change_health(-5)

            print("\n-5 HP")
            print(f"Health: {player.health}/100")
            print()
            print("ACHIEVEMENT UNLOCKED:")
            print("Chair Criminal")

            player.add_friendship_points(5)
            player.add_memory("The Forbidden Chair")
            break

        else:
            print("\nPick 1, 2, or 3.")

    pause()


def middle_school_music(player):
    divider()

    print("LEVEL 6: AUX CORD")
    print()
    print("Every era needs a soundtrack.")
    print()
    print("You pull out the ancient iPod Touch.")
    print()
    print("What are we listening to?")
    print()

    print("[1] Blue Lips")
    print("[2] Coin-Operated Boy")
    print("[3] Tom's Diner")

    choice = input("\n> ")

    songs = {
        "1": "Blue Lips",
        "2": "Coin-Operated Boy",
        "3": "Tom's Diner"
    }

    if choice not in songs:
        choice = "3"

    selected_song = songs[choice]

    player.soundtrack.append(selected_song)
    player.add_memory("Middle School Soundtrack")
    player.add_friendship_points(5)

    print()
    print(f'SONG ADDED TO FRIENDSHIP SOUNDTRACK: "{selected_song}"')
    print()
    print("This choice will be remembered.")

    pause()


def alannas_house(player):
    divider()

    print("LEVEL 7: THE ALANNA'S HOUSE RITUAL")
    print()
    print("Step One: Acquire KFC")
    print("Step Two: Go to Alanna's")
    print("Step Three: Classified")
    print()
    print("Where do you go first?")
    print()

    while True:
        print("[1] Somewhere responsible")
        print("[2] Straight to Alanna's")
        print("[3] KFC")

        choice = input("\n> ")

        if choice == "1":
            print("\nUNKNOWN LOCATION.")
            print()
            print("No responsible location appears in the historical record.")
            print()

        elif choice == "2":
            print("\nYou arrive at Alanna's.")
            print()
            print("Something is wrong.")
            print()
            print("KFC NOT DETECTED.")
            print()
            print("You have violated the sacred order.")
            print()

        elif choice == "3":
            print("\nCORRECT.")
            print()
            print("KFC ACQUIRED.")
            print()
            print("The ritual may proceed.")

            if "KFC" not in player.inventory:
                player.inventory.append("KFC")

            player.add_memory("Alanna's House Ritual")
            player.add_friendship_points(5)
            break

        else:
            print("\nPick 1, 2, or 3.")

    pause()


def georgia_tech_party(player):
    divider()

    print("LEVEL 8: GEORGIA TECH PARTY")
    print()
    print("Mission: Survive the night")
    print("Objective: Get everyone home")
    print("Patience Remaining: 4%")
    print()
    print("One member of the party has become")
    print("unbearably annoying.")
    print()
    print("What do you do?")
    print()

    print("[1] Practice compassion")
    print("[2] Argue the entire drive")
    print("[3] Return her safely to her car at McDonald's and leave")

    choice = input("\n> ")

    if choice == "1":
        print("\nYou attempt compassion.")
        print()
        print("Patience: 2%")
        print()
        print("Patience: 0%")
        print()
        print("Compassion has failed.")

    elif choice == "2":
        print("\nEveryone begins arguing.")

        player.change_health(-10)

        print("\n-10 HP")
        print(f"Health: {player.health}/100")

    else:
        print("\nNEW DESTINATION:")
        print("McDonald's parking lot.")
        print()
        print("You return her to her vehicle.")
        print("You make sure she is safe.")
        print("Doors secured.")
        print()
        print("Everything good?")
        print()
        print("Great.")
        print()
        print("DRIVE.")

    player.add_memory("Georgia Tech Party")
    player.add_friendship_points(5)

    pause()


def foster_car(player):
    divider()

    print("LEVEL 9: FOSTER'S CAR")
    print()
    print("🚨 SURVIVAL EVENT 🚨")
    print()
    print("Driver: Foster")
    print("Speed Limit: Eventually irrelevant")
    print()
    print("Foster begins doing donuts.")
    print()
    print("What do you do?")
    print()

    print("[1] Get out immediately")
    print("[2] Tell Foster to drive responsibly")
    print("[3] Remain inside the vehicle")

    choice = input("\n> ")

    if choice == "1":
        print("\nExcellent choice.")
        print()
        print("Unfortunately:")
        print("TIMELINE ERROR.")
        print()
        print("Returning you to the vehicle.")

    elif choice == "2":
        print('\n"Foster, please obey applicable traffic laws."')
        print()
        print("Foster considers your request.")
        print()
        print("Request denied.")

    print()
    print("Foster enters the road.")
    print()
    print("SPEED LIMIT: 35 MPH")
    print("CURRENT SPEED: 100+ MPH")
    print()
    print("What do you do?")
    print()

    print("[1] Scream")
    print("[2] Pray")
    print("[3] Accept death")
    print("[4] All of the above")

    input("\n> ")

    print()
    print("Against every statistical prediction...")
    print()
    print("You survive.")

    player.change_health(-10)

    print()
    print("-10 HP")
    print()
    print("LEGENDARY ACHIEVEMENT:")
    print("Somehow Still Alive")

    player.add_memory("Foster's Car")
    player.add_friendship_points(10)

    pause()


def gossip_girl(player):
    divider()

    print("LEVEL 10: GOSSIP GIRL NIGHT")
    print()
    print("Kaisha invites you over.")
    print()
    print('"Come over! We\'ll make cookies and watch Gossip Girl!"')
    print()
    print("You arrive.")
    print()
    print("Cookies: YES")
    print("Gabby: YES")
    print("Television: YES")
    print("Gossip Girl: ...")
    print()
    print('KAISHA: "Actually I don\'t really feel like watching Gossip Girl."')
    print()

    print("[1] THEN WHY DID YOU INVITE ME OVER?")
    print("[2] Eat the cookies")
    print("[3] Try to convince Kaisha")
    print("[4] Accept that this happens every time")

    choice = input("\n> ")

    if choice == "1":
        print("\nA reasonable question.")
        print("No reasonable answer is provided.")

    elif choice == "2":
        print("\nCookies consumed.")
        player.change_health(10)
        print("+10 HP")

    elif choice == "3":
        print("\nPERSUASION CHECK...")
        print("FAILED.")
        print()
        print("Kaisha still doesn't want to watch it.")

    else:
        print("\nYou have achieved enlightenment.")
        print()
        print("ACHIEVEMENT UNLOCKED:")
        print("You Know Her Too Well")

    print()
    print("Gossip Girl may not have been watched.")
    print("Cookies were eaten.")
    print("Gabby stayed anyway.")
    print()
    print("+10 Friendship Points")

    player.add_memory("Gossip Girl Night")
    player.add_friendship_points(10)

    pause()


def fall_retreat(player):
    divider()

    print("LEVEL 11: FALL RETREAT")
    print()
    print("Frequency: Every year")
    print("Essential Equipment:")
    print("- Friends")
    print("- Snacks")
    print("- Questionable sleep schedule")
    print()
    print("Choose the Fall Retreat anthem.")
    print()

    print("[1] Gooey")
    print("[2] Car Radio")
    print("[3] Roslyn")

    choice = input("\n> ")

    songs = {
        "1": "Gooey",
        "2": "Car Radio",
        "3": "Roslyn"
    }

    if choice not in songs:
        choice = "1"

    selected_song = songs[choice]

    player.soundtrack.append(selected_song)
    player.add_memory("Fall Retreat")
    player.add_friendship_points(5)

    print()
    print(f'SONG ADDED TO FRIENDSHIP SOUNDTRACK: "{selected_song}"')
    print()
    print("You stare dramatically out the window.")
    print()
    print("+5 Friendship Points")

    pause()


def middle_school(player):
    player.current_era = "Middle School"

    divider()
    print("ERA I")
    print("MIDDLE SCHOOL")
    print()
    print("Tiny backpacks.")
    print("Bad survival instincts.")
    print("The beginning of everything.")
    pause()

    how_we_met(player)
    random_middle_school_event(player)

    gas_station(player)
    random_middle_school_event(player)

    mcdonalds(player)
    random_middle_school_event(player)

    fifty_shades(player)

    swing_chair(player)
    random_middle_school_event(player)

    middle_school_music(player)

    high_school(player)


def high_school(player):
    player.current_era = "High School"

    divider()

    print("ERA II")
    print("HIGH SCHOOL")
    print()
    print("The lore expands.")
    print("The decisions become worse.")
    print("Somehow, you both remain alive.")

    pause()

    alannas_house(player)
    georgia_tech_party(player)
    foster_car(player)
    gossip_girl(player)
    fall_retreat(player)

    high_school_complete(player)


def high_school_complete(player):
    divider()

    print("ERA COMPLETE")
    print()
    print("Middle School: Survived")
    print("High School: Somehow also survived")
    print()
    print(f"Friendship Points: {player.friendship_points}")
    print(f"Current Health: {player.health}/100")
    print()
    print("McDonald's trips became car rides.")
    print("Fall retreats ended.")
    print("The world got bigger.")
    print()
    print("But Player Two remained connected.")
    print()
    print("ERA III: ADULTHOOD")
    print()
    print("COMING SOON...")

    pause()

    ending(player)


def ending(player):
    divider()

    print("TO BE CONTINUED...")
    print()
    print("You have reached the end of the current build.")
    print()
    print("But before you go...")
    print()

    print("FRIENDSHIP SOUNDTRACK:")

    for song in player.soundtrack:
        print(f"- {song}")

    print()
    print(f"FINAL FRIENDSHIP POINTS: {player.friendship_points}")
    print()
    print("Rank:")
    print("BEST BITCHES FOR LIFE")
    print()
    print("Happy Birthday, Gabby <3")

    pause()


def main_menu(player):
    run = True

    while run:
        divider()

        print("HAPPY BIRTHDAY BITCH <3")
        print()
        print("[1] Start Game")
        print("[2] View Stats")
        print("[3] Quit")

        choice = input("\n> ")

        match choice:

            case "1":
                middle_school(player)

            case "2":
                view_stats(player)

            case "3":
                print("\nBye bitch <3")
                run = False

            case _:
                print("\nPlease choose 1, 2, or 3.")


gabby = Player("Gabby")

main_menu(gabby)



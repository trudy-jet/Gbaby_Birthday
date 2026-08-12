import streamlit as st
import base64
import random


# =========================================================
# BACKGROUND / STYLING
# =========================================================

def set_background(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()


    st.markdown(
        f"""
        <style>

        header {{
            background: transparent !important;
        }}

        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center top;
            background-repeat: no-repeat;
            background-attachment: fixed;
            padding-top: 0rem;
        }}

        .block-container {{
            background-color: rgba(255, 255, 255, 0.84);
            padding: 2rem;
            border-radius: 25px;
            margin-top: 1rem;
            margin-bottom: 3rem;
            max-width: 900px;
        }}

        div.stButton > button {{
            border-radius: 16px;
            min-height: 48px;
            font-size: 1rem;
        }}

        @media (max-width: 768px) {{

    .stApp {{
        background-position: center top;
        background-size: 100% auto;
        background-repeat: repeat-y;
        background-attachment: scroll;
    }}

    .block-container {{
        margin: 0.5rem auto;
        padding: 1.2rem;
        border-radius: 18px;
        width: 92%;
        max-width: 92%;
    }}

    h1 {{
        font-size: 2rem !important;
    }}

    h2 {{
        font-size: 1.6rem !important;
    }}
}}

        </style>
        """,
        unsafe_allow_html=True
    )


set_background("gbaby_background.png")
       
# =========================================================
# PLAYER CLASS
# =========================================================

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


# =========================================================
# SESSION STATE
# =========================================================

if "player" not in st.session_state:
    st.session_state.player = Player("Gabby")

if "scene" not in st.session_state:
    st.session_state.scene = "main_menu"

if "result" not in st.session_state:
    st.session_state.result = ""

if "next_scene" not in st.session_state:
    st.session_state.next_scene = ""

if "random_event" not in st.session_state:
    st.session_state.random_event = None

player = st.session_state.player


# =========================================================
# HELPERS
# =========================================================

def go_to(scene_name):
    st.session_state.scene = scene_name
    st.rerun()


def show_health():
    st.caption(f"❤️ Health: {player.health}/100")


def result_screen():
    st.header("✨ MEMORY COMPLETE")

    st.write(st.session_state.result)

    show_health()

    if st.button("Continue ➡️", use_container_width=True):
        go_to(st.session_state.next_scene)


def set_result(text, next_scene):
    st.session_state.result = text
    st.session_state.next_scene = next_scene
    go_to("result_screen")


# =========================================================
# MAIN MENU
# =========================================================

def main_menu():
    st.title("🎂 Happy Birthday Bitch 💕")

    st.write(
        "A completely historically accurate adventure through our friendship."
    )

    st.write("")

    if st.button("🎮 Start Game", use_container_width=True):
        go_to("how_we_met")

    if st.button("🎒 View Stats", use_container_width=True):
        go_to("stats")


# =========================================================
# STATS
# =========================================================

def view_stats():
    st.header("🎒 Gabby's Stats")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("❤️ Health", f"{player.health}/100")

    with col2:
        st.metric("💕 Friendship Points", player.friendship_points)

    st.write(f"**Current Era:** {player.current_era}")

    st.subheader("🎒 Inventory")

    for item in player.inventory:
        st.write(f"• {item}")

    st.subheader("📖 Memories")

    if player.memories:
        for memory in player.memories:
            st.write(f"✓ {memory}")
    else:
        st.write("No memories unlocked yet.")

    st.subheader("🎧 Friendship Soundtrack")

    if player.soundtrack:
        for song in player.soundtrack:
            st.write(f"🎵 {song}")
    else:
        st.write("No songs selected yet.")

    if st.button("⬅️ Back", use_container_width=True):
        go_to("main_menu")


# =========================================================
# MIDDLE SCHOOL INTRO
# =========================================================

def middle_school_intro():
    player.current_era = "Middle School"

    st.header("🎒 ERA I: MIDDLE SCHOOL")

    st.write("Tiny backpacks.")
    st.write("Bad survival instincts.")
    st.write("The beginning of everything.")

    if st.button("Begin Middle School ➡️", use_container_width=True):
        go_to("how_we_met")


# =========================================================
# HOW WE MET
# =========================================================

def how_we_met():
    st.header("🎒 LEVEL 1: THE ORIGIN STORY")

    st.write("**Year:** 7th Grade")
    st.write("**Location:** School hallway")
    st.write("**Friendship Status:** Complete strangers")

    st.divider()

    st.write("A girl approaches you.")

    st.info('KAISHA: "Do you know where Ms. Woyce\'s class is?"')

    st.write("### What do you do?")

    if st.button("🗺️ Tell her where it is", use_container_width=True):
        player.add_friendship_points(5)
        player.add_memory("How We Met")

        set_result(
            """
You give Kaisha directions.

Whether those directions are accurate is irrelevant.

**NEW CHARACTER DISCOVERED: Kaisha**

💕 +5 Friendship Points
""",
            "random_middle_school"
        )

    if st.button("🤷 Admit you have no idea", use_container_width=True):
        player.add_friendship_points(5)
        player.add_memory("How We Met")

        set_result(
            """
You have absolutely no idea.

Excellent.

Two lost seventh graders.

**NEW CHARACTER DISCOVERED: Kaisha**

💕 +5 Friendship Points
""",
            "random_middle_school"
        )

    if st.button("🚶 Ignore her", use_container_width=True):
        go_to("timeline_error")


def timeline_error():
    st.error("🚨 TIMELINE ERROR")

    st.write("""
You walk directly past Kaisha.

...

The universe begins destabilizing.

Without this interaction, over a decade of lore cannot occur.

**Please stop ruining the birthday game.**
""")

    if st.button("↩️ Fix the Timeline", use_container_width=True):
        go_to("how_we_met")


# =========================================================
# RANDOM MIDDLE SCHOOL EVENTS
# =========================================================

def random_middle_school():
    if st.session_state.random_event is None:
        st.session_state.random_event = random.choice(
            ["none", "noob", "phillip", "jake"]
        )

    event = st.session_state.random_event

    if event == "none":
        st.session_state.random_event = None
        go_to("gas_station")

    st.header("⚠️ RANDOM EVENT ⚠️")

    if event == "noob":
        st.write("Someone calls Kaisha a noob.")
        st.write("")
        st.write("This is devastating.")

        if st.button("Take the emotional damage", use_container_width=True):
            player.change_health(-10)
            st.session_state.random_event = None

            set_result(
                """
Someone called Kaisha a noob.

Absolutely unforgivable.

❤️ **-10 HP**
""",
                "gas_station"
            )

    elif event == "phillip":
        st.write("You somehow get Phillip sent to the principal's office.")
        st.write("")
        st.write("Unfortunately, Phillip has a flight for family vacation.")
        st.write("")
        st.write("Phillip misses the flight.")
        st.write("")
        st.write("For reasons the game refuses to explain:")

        if st.button("Accept the healing", use_container_width=True):
            player.change_health(15)
            st.session_state.random_event = None

            set_result(
                """
Phillip has missed his flight.

For reasons that remain ethically mysterious:

❤️ **+15 HP**
""",
                "gas_station"
            )

    elif event == "jake":
        st.write("Jake approaches.")
        st.write("")
        st.info('"Do you guys wanna hear my car rev?"')
        st.write("")
        st.write("There is no correct way to respond to this.")

        if st.button("Suffer", use_container_width=True):
            player.change_health(-5)
            st.session_state.random_event = None

            set_result(
                """
Jake asked if you wanted to hear his car rev.

You did not.

❤️ **-5 HP**
""",
                "gas_station"
            )


# =========================================================
# GAS STATION
# =========================================================

def gas_station():
    st.header("⛽ LEVEL 2: GAS STATION INCIDENT")

    st.write("**Mission:** Acquire Movie Snacks")
    st.write("**Adult Supervision:** None")
    st.write("**Situational Awareness:** Concerning")

    st.divider()

    st.write(
        "You and Kaisha stop at a gas station before heading to the movie theater."
    )

    st.write("A strange man approaches.")

    st.info('"Are you girls here alone?"')

    st.write("### What do you do?")

    if st.button(
        "💪 Say your enormous father is outside",
        use_container_width=True
    ):
        st.warning(
            "Excellent survival instincts. Unfortunately, this is not historically accurate."
        )

    if st.button(
        "🙅 Refuse to answer",
        use_container_width=True
    ):
        st.warning(
            "Responsible. Sensible. Safe. Unfortunately, neither of you did this."
        )

    if st.button(
        "🙂 Tell him the truth",
        use_container_width=True
    ):
        go_to("gas_station_question_two")


def gas_station_question_two():
    st.header("⛽ GAS STATION INCIDENT")

    st.write('You cheerfully say, **"Yeah!"**')

    st.write("The strange man now knows you are unsupervised.")

    st.info('"Where are you headed?"')

    st.write("### What do you tell him?")

    if st.button("🤥 Lie", use_container_width=True):
        st.warning("Nice try. History says otherwise.")

    if st.button("🙅 Don't answer", use_container_width=True):
        st.warning("Character development arrived too early.")

    if st.button(
        "🎬 Tell him you're going to the movie theater",
        use_container_width=True
    ):
        player.add_friendship_points(5)
        player.add_memory("Gas Station Incident")

        if "Gas Station Snacks" not in player.inventory:
            player.inventory.append("Gas Station Snacks")

        set_result(
            """
"The movie theater!"

Incredible.

You have now told a strange adult:

- You are alone
- Where you are going

🏆 **ACHIEVEMENT UNLOCKED: How Are We Still Alive?**

🎒 **ITEM ACQUIRED: Gas Station Snacks**

💕 +5 Friendship Points
""",
            "mcdonalds"
        )


# =========================================================
# MCDONALD'S
# =========================================================

def mcdonalds():
    st.header("🍟 LEVEL 3: THE McDONALD'S PILGRIMAGE")

    st.write("**Mission:** Acquire McDonald's")
    st.write("**Distance:** 1 mile")
    st.write("**Transportation:** Legs")
    st.write("**Desire For Fries:** Extreme")

    st.divider()

    st.write("There is a McDonald's approximately one mile away.")

    st.write("### What do you do?")

    if st.button("🚶 Begin the pilgrimage", use_container_width=True):
        player.add_friendship_points(5)
        player.add_memory("McDonald's Pilgrimage")

        if "Questionably Earned French Fries" not in player.inventory:
            player.inventory.append("Questionably Earned French Fries")

        set_result(
            """
**THE PILGRIMAGE BEGINS.**

One mile.

On foot.

For McDonald's.

Was it worth it?

Obviously.

🎒 **ITEM ACQUIRED: Questionably Earned French Fries**

💕 +5 Friendship Points
""",
            "fifty_shades"
        )

    if st.button("🚗 Ask an adult to drive", use_container_width=True):
        st.warning(
            "Air conditioning? Comfortable seats? Absolutely not. HISTORICAL INACCURACY."
        )

    if st.button(
        "🥗 Decide you don't need McDonald's",
        use_container_width=True
    ):
        st.error(
            "FATAL ERROR. This contradicts everything we know about adolescent human behavior."
        )


# =========================================================
# FIFTY SHADES
# =========================================================

def fifty_shades():
    st.header("📚 LEVEL 4: THE FORBIDDEN TEXTS")

    st.write("**Location:** Kaisha's House")
    st.write("**Parental Permission:** Absolutely Not")

    st.divider()

    st.write("You and Kaisha discover a mysterious trilogy.")

    st.write("**Fifty Shades of Grey.**")

    st.write("The books belong to Kaisha's mom.")

    st.write("### What do you do?")

    if st.button("😇 Leave them alone", use_container_width=True):
        st.warning(
            "You demonstrate maturity and restraint. Who are you? Try again."
        )

    if st.button(
        "👀 Read the back cover and put them back",
        use_container_width=True
    ):
        st.warning(
            "Gabby looks at Kaisha. Kaisha looks at Gabby. Yeah, no."
        )

    if st.button(
        "📖 Obviously read them together",
        use_container_width=True
    ):
        player.add_friendship_points(5)
        player.add_memory("The Forbidden Texts")

        set_result(
            """
**FORBIDDEN KNOWLEDGE ACQUIRED.**

This was perhaps not age-appropriate literature.

That did not stop you.

🏆 **ACHIEVEMENT UNLOCKED: We Should Not Have Been Reading This**

💕 +5 Friendship Points
""",
            "swing_chair"
        )


# =========================================================
# SWING CHAIR
# =========================================================

def swing_chair():
    st.header("🪑 LEVEL 5: THE FORBIDDEN CHAIR")

    st.write("⚔️ **BOSS ENCOUNTER** ⚔️")

    st.write("There is a swinging chair in Kaisha's bedroom.")

    st.write("There is only one rule.")

    st.error("GABBY MAY NOT SIT IN THE CHAIR.")

    st.write("The chair swings gently.")
    st.write("")
    st.write("Temptingly.")

    st.write("### What do you do?")

    if st.button("😇 Respect Kaisha's wishes", use_container_width=True):
        player.add_friendship_points(2)
        player.add_memory("The Forbidden Chair")

        set_result(
            """
You do not sit in the chair.

Kaisha watches suspiciously.

You survive.

But at what cost?

💕 +2 Friendship Points
""",
            "middle_school_music"
        )

    if st.button(
        "🙋 Ask politely to sit in it",
        use_container_width=True
    ):
        player.add_memory("The Forbidden Chair")

        set_result(
            """
"Can I sit in your chair?"

**KAISHA:** "No."

**END OF NEGOTIATIONS.**
""",
            "middle_school_music"
        )

    if st.button(
        "😈 Sit in the goddamn chair",
        use_container_width=True
    ):
        player.change_health(-5)
        player.add_friendship_points(5)
        player.add_memory("The Forbidden Chair")

        set_result(
            """
You sit.

Silence.

Kaisha turns around.

**"GET OUT OF MY CHAIR."**

❤️ **-5 HP**

🏆 **ACHIEVEMENT UNLOCKED: Chair Criminal**

💕 +5 Friendship Points
""",
            "middle_school_music"
        )


# =========================================================
# MIDDLE SCHOOL MUSIC
# =========================================================

def middle_school_music():
    st.header("🎧 LEVEL 6: AUX CORD")

    st.write("Every era needs a soundtrack.")

    if "iPod Touch" in player.inventory:
        st.success("You pull out the ancient iPod Touch.")

    st.write("### What are we listening to?")

    if st.button("🎵 Blue Lips", use_container_width=True):
        choose_middle_song("Blue Lips")

    if st.button("🎵 Coin-Operated Boy", use_container_width=True):
        choose_middle_song("Coin-Operated Boy")

    if st.button("🎵 Tom's Diner", use_container_width=True):
        choose_middle_song("Tom's Diner")


def choose_middle_song(song):
    if song not in player.soundtrack:
        player.soundtrack.append(song)

    player.add_memory("Middle School Soundtrack")
    player.add_friendship_points(5)

    set_result(
        f"""
🎵 **SONG ADDED TO FRIENDSHIP SOUNDTRACK**

**{song}**

This choice will be remembered.

💕 +5 Friendship Points
""",
        "high_school_intro"
    )


# =========================================================
# HIGH SCHOOL INTRO
# =========================================================

def high_school_intro():
    player.current_era = "High School"

    st.header("💿 ERA II: HIGH SCHOOL")

    st.write("The lore expands.")
    st.write("The decisions become worse.")
    st.write("Somehow, you both remain alive.")

    if st.button("Enter High School ➡️", use_container_width=True):
        go_to("alannas_house")


# =========================================================
# ALANNA'S HOUSE
# =========================================================

def alannas_house():
    st.header("🍗 LEVEL 7: THE ALANNA'S HOUSE RITUAL")

    st.write("**Step One:** Acquire KFC")
    st.write("**Step Two:** Go to Alanna's")
    st.write("**Step Three:** Classified")

    st.write("### Where do you go first?")

    if st.button("📚 Somewhere responsible", use_container_width=True):
        st.warning(
            "UNKNOWN LOCATION. No responsible location appears in the historical record."
        )

    if st.button("🏠 Straight to Alanna's", use_container_width=True):
        st.warning(
            "Something is wrong. KFC NOT DETECTED. You have violated the sacred order."
        )

    if st.button("🍗 KFC", use_container_width=True):
        if "KFC" not in player.inventory:
            player.inventory.append("KFC")

        player.add_memory("Alanna's House Ritual")
        player.add_friendship_points(5)

        set_result(
            """
**CORRECT.**

🍗 KFC ACQUIRED.

The ritual may proceed.

🏆 **ACHIEVEMENT UNLOCKED: Tradition Is Tradition**

💕 +5 Friendship Points
""",
            "georgia_tech_party"
        )


# =========================================================
# GEORGIA TECH PARTY
# =========================================================

def georgia_tech_party():
    st.header("🎉 LEVEL 8: GEORGIA TECH PARTY")

    st.write("**Mission:** Survive the night")
    st.write("**Current Objective:** Get everyone home")
    st.write("**Patience Remaining:** 4%")

    st.divider()

    st.write(
        "One member of the party has become unbearably annoying."
    )

    st.write("### What do you do?")

    if st.button("🧘 Practice compassion", use_container_width=True):
        set_result(
            """
You attempt compassion.

Patience: 2%.

Patience: 0%.

**Compassion has failed.**
""",
            "foster_car"
        )

        player.add_memory("Georgia Tech Party")
        player.add_friendship_points(5)

    if st.button("🗯️ Argue the entire drive", use_container_width=True):
        player.change_health(-10)
        player.add_memory("Georgia Tech Party")
        player.add_friendship_points(5)

        set_result(
            """
Everyone begins arguing.

This strategy has accomplished absolutely nothing.

❤️ **-10 HP**

💕 +5 Friendship Points
""",
            "foster_car"
        )

    if st.button(
        "🚗 Return her safely to her car at McDonald's and leave",
        use_container_width=True
    ):
        player.add_memory("Georgia Tech Party")
        player.add_friendship_points(5)

        set_result(
            """
**NEW DESTINATION: McDonald's Parking Lot**

You return her to her vehicle.

You make sure she is safe.

Doors secured.

Everything good?

Great.

**DRIVE.**

🏆 **ACHIEVEMENT UNLOCKED: We Have Reached Our Limit**

💕 +5 Friendship Points
""",
            "foster_car"
        )


# =========================================================
# FOSTER'S CAR
# =========================================================

def foster_car():
    st.header("🚗 LEVEL 9: FOSTER'S CAR")

    st.error("🚨 SURVIVAL EVENT 🚨")

    st.write("**Driver:** Foster")
    st.write("**Speed Limit:** Eventually irrelevant")

    st.divider()

    st.write("Foster begins doing donuts.")

    st.write("### What do you do?")

    if st.button("🚪 Get out immediately", use_container_width=True):
        st.warning(
            "Excellent choice. Unfortunately, HISTORICAL INACCURACY. Returning you to the vehicle."
        )

    if st.button(
        "📢 Tell Foster to drive responsibly",
        use_container_width=True
    ):
        st.warning(
            '"Foster, please obey applicable traffic laws." Foster has rejected your request.'
        )

    if st.button(
        "😬 Remain inside the vehicle",
        use_container_width=True
    ):
        go_to("foster_car_speed")


def foster_car_speed():
    st.header("🚗 FOSTER'S CAR")

    st.write("Foster enters the road.")

    st.error("SPEED LIMIT: 35 MPH")
    st.error("CURRENT SPEED: 100+ MPH")

    st.write("### What do you do?!")

    if st.button("😱 Scream", use_container_width=True):
        finish_foster()

    if st.button("🙏 Pray", use_container_width=True):
        finish_foster()

    if st.button("💀 Accept death", use_container_width=True):
        finish_foster()

    if st.button("🫠 All of the above", use_container_width=True):
        finish_foster()


def finish_foster():
    player.change_health(-10)
    player.add_memory("Foster's Car")
    player.add_friendship_points(10)

    set_result(
        """
Against every statistical prediction...

**You survive.**

❤️ **-10 HP**

🏆 **LEGENDARY ACHIEVEMENT: Somehow Still Alive**

💕 +10 Friendship Points
""",
        "gossip_girl"
    )


# =========================================================
# GOSSIP GIRL
# =========================================================

def gossip_girl():
    st.header("🍪 LEVEL 10: GOSSIP GIRL NIGHT")

    st.write("Kaisha invites you over.")

    st.info(
        '"Come over! We\'ll make cookies and watch Gossip Girl!"'
    )

    st.write("You arrive.")

    st.write("Cookies: ✅")
    st.write("Gabby: ✅")
    st.write("Television: ✅")
    st.write("Gossip Girl: ...")

    st.info(
        'KAISHA: "Actually I don\'t really feel like watching Gossip Girl."'
    )

    st.write("### What do you do?")

    if st.button(
        "😡 THEN WHY DID YOU INVITE ME OVER?",
        use_container_width=True
    ):
        finish_gossip(
            """
A reasonable question.

No reasonable answer is provided.
"""
        )

    if st.button("🍪 Eat the cookies", use_container_width=True):
        player.change_health(10)

        finish_gossip(
            """
Cookies consumed.

❤️ **+10 HP**

The evening has been salvaged.
"""
        )

    if st.button(
        "🗣️ Try to convince Kaisha",
        use_container_width=True
    ):
        finish_gossip(
            """
**PERSUASION CHECK...**

FAILED.

Kaisha still doesn't want to watch it.

Obviously.
"""
        )

    if st.button(
        "🧘 Accept that this happens every time",
        use_container_width=True
    ):
        finish_gossip(
            """
You have achieved enlightenment.

🏆 **ACHIEVEMENT UNLOCKED: You Know Her Too Well**
"""
        )


def finish_gossip(extra_text):
    player.add_memory("Gossip Girl Night")
    player.add_friendship_points(10)

    set_result(
        f"""
{extra_text}

Gossip Girl may not have been watched.

Cookies were eaten.

Gabby stayed anyway.

💕 **+10 Friendship Points**
""",
        "fall_retreat"
    )


# =========================================================
# FALL RETREAT
# =========================================================

def fall_retreat():
    st.header("🍂 LEVEL 11: FALL RETREAT")

    st.write("**Frequency:** Every year")

    st.write("Essential Equipment:")
    st.write("- Friends")
    st.write("- Snacks")
    st.write("- Questionable sleep schedule")

    st.write("### Choose the Fall Retreat anthem.")

    if st.button("🎵 Gooey", use_container_width=True):
        choose_retreat_song("Gooey")

    if st.button("🎵 Car Radio", use_container_width=True):
        choose_retreat_song("Car Radio")

    if st.button("🎵 Roslyn", use_container_width=True):
        choose_retreat_song("Roslyn")


def choose_retreat_song(song):
    if song not in player.soundtrack:
        player.soundtrack.append(song)

    player.add_memory("Fall Retreat")
    player.add_friendship_points(5)

    set_result(
        f"""
🎵 **SONG ADDED TO FRIENDSHIP SOUNDTRACK**

**{song}**

You stare dramatically out the window because apparently you are the main character.

💕 +5 Friendship Points
""",
        "high_school_complete"
    )


# =========================================================
# HIGH SCHOOL COMPLETE
# =========================================================

def high_school_complete():
    st.header("🎓 ERA COMPLETE")

    st.write("**Middle School:** Survived")
    st.write("**High School:** Somehow also survived")

    st.write("")

    st.metric("💕 Friendship Points", player.friendship_points)
    st.metric("❤️ Current Health", f"{player.health}/100")

    st.divider()

    st.write("McDonald's trips became car rides.")
    st.write("Fall retreats ended.")
    st.write("The world got bigger.")
    st.write("")
    st.write("But Player Two remained connected.")

    st.success("🔓 ERA III: ADULTHOOD UNLOCKED")

    if st.button("Continue ➡️", use_container_width=True):
        go_to("adulthood_placeholder")


# =========================================================
# ADULTHOOD PLACEHOLDER
# =========================================================

def adulthood_placeholder():
    player.current_era = "Adulthood"

    st.header("🌷 ERA III: ADULTHOOD")

    st.write(
        "Adult memories are coming next."
    )

    st.write(
        "For now, the current build ends here."
    )

    if st.button("See Current Ending 💕", use_container_width=True):
        go_to("ending")


# =========================================================
# ENDING
# =========================================================

def ending():
    st.header("💗 TO BE CONTINUED...")

    st.write("But before you go...")

    st.subheader("🎧 Friendship Soundtrack")

    for song in player.soundtrack:
        st.write(f"🎵 {song}")

    st.write("")

    st.metric(
        "💕 Final Friendship Points",
        player.friendship_points
    )

    st.write("### Rank:")
    st.success("BEST BITCHES FOR LIFE")

    st.write("")
    st.write("Happy Birthday, Gabby <3")

    if st.button("🎒 View Final Stats", use_container_width=True):
        go_to("stats")

    if st.button("🏠 Back to Main Menu", use_container_width=True):
        go_to("main_menu")


# =========================================================
# GAME ROUTER
# =========================================================

scene = st.session_state.scene

if scene == "main_menu":
    main_menu()

elif scene == "middle_school_intro":
    middle_school_intro()

elif scene == "stats":
    view_stats()

elif scene == "how_we_met":
    how_we_met()

elif scene == "timeline_error":
    timeline_error()

elif scene == "random_middle_school":
    random_middle_school()

elif scene == "gas_station":
    gas_station()

elif scene == "gas_station_question_two":
    gas_station_question_two()

elif scene == "mcdonalds":
    mcdonalds()

elif scene == "fifty_shades":
    fifty_shades()

elif scene == "swing_chair":
    swing_chair()

elif scene == "middle_school_music":
    middle_school_music()

elif scene == "high_school_intro":
    high_school_intro()

elif scene == "alannas_house":
    alannas_house()

elif scene == "georgia_tech_party":
    georgia_tech_party()

elif scene == "foster_car":
    foster_car()

elif scene == "foster_car_speed":
    foster_car_speed()

elif scene == "gossip_girl":
    gossip_girl()

elif scene == "fall_retreat":
    fall_retreat()

elif scene == "high_school_complete":
    high_school_complete()

elif scene == "adulthood_placeholder":
    adulthood_placeholder()

elif scene == "ending":
    ending()

elif scene == "result_screen":
    result_screen()
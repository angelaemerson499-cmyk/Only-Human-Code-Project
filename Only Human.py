import os
import random
# Clears the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Display starting menu 
def prompt():
    print("\t\t\tWelcome to my game\n\n\
          you must identify the human, visitors. among your house.\n\n\
            Your goal is to find all the visitors\n")
   
    input("Press any key to start the game...")

# Map
rooms = {
    'Main entrance of the house' : {'South': 'Living Rooms', 'North': 'Outside of the house'},
    'Living Rooms' : {'North': 'Main entrance of the house', 'East': 'Kitchen', 'item': 'Knife'},
    'Kitchen' : {'West': 'Living Rooms', 'item': 'Gun'},
    'Outside of the house' : {'South': 'Main entrance of the house', 'Entity': 'Human', 'killer' 'Visitor': 'Alien'}
}


# List to track inventory
inventory = []
# List to track found visitors
visitors_found = []

# Tracking current room
current_room = "Main entrance of the house"

# Result of the last move
msg = ""

clear()
prompt()

# Game Opening
clear()
import time
print("Actually, we just got back from our trip, Aren't you tired of staying at home?")
time.sleep(5)
print("Yeah Yeah I remember. But you know, sometimes I feel like we are not alone...")
time.sleep(3)
print("Okay, i will talk to you later.")
time.sleep(3)
print("Bye dad.")
time.sleep(2)

# Wait for user to proceed
input("Press any key to continue...")

# Start of the game
import time
print("A radio just wakes you up, and you wait for your dad while the radio talks about the news..")
time.sleep(4)
print("At 6:27AM today, there was a powerful emission of energy from the sun.")
time.sleep(4)
print("this burst of energy was far larger than scientists had predicted.")
time.sleep(4)
print("This solar flare has disrupted all forms of communication including cell phones, TV, and internet.")
time.sleep(4)
print("The government has since declare a state of emergency")
time.sleep(4)
print("We ask that viewers refrain from going outside during the day")
time.sleep(4)   
print("as the radiation levels are at an all time high.")
time.sleep(4)
print("...")
time.sleep(4)
input("Press any key to continue...")
time.sleep(4)   
print("In other news, there have been multiple reports of skin walkers sightings across the country.")
time.sleep(4)  
print("Skin walkers are called to be visitors that can take the form of humans from underground itself.")
time.sleep(4)
print("They are said to be eat and killed towards humans and have been known to abduct people.")
time.sleep(4)
print("Reports of visitors sightings have been increasing lately.")
time.sleep(4)
print("Authorities are advising people to stay indoors and report any suspicious visitors.")
time.sleep(4)
input("Press any key to start the game...") 
time.sleep(5)

clear()
# Day 1 
if True:
    clear()
    print(f"You are in the {current_room}")
    time.sleep(4)
    print(msg)

    input("Visitors huh... uh... better be careful.")
    time.sleep(3)

# transition to night
    input("It's night all of sudden.")
    time.sleep(3)
    print("It's night time now. You should be careful.")
    time.sleep(3)
# Gameplay in night time
    print(f"You are in the {current_room}")
    print(msg)
    input("It's dark outside... better stay inside.")
    time.sleep(3)


 # replace the single door-knock/encounter block with a repeat-until-5-or-dead loop
max_encounters = 5
encounters_handled = 0
alive = True 
def pick_encounter():
    entities = ['Human', 'Visitor', 'Killer']
    human_names = ['Lynda Ann Healy', 'Laura Ann Aime', 'Konerak Sinthasomphone', 'Steven Walter Tuomi', 'Bernice Worden']
    visitor_names = ['Richard Ramirez', 'Deputy Sheriff Frank Worden', 'Aileen Wuornos', 'Marcel Petiot', 'David Berkowitz']
    killer_names = ['Theodore Bundy', 'John Wayne Gacy', 'Jeffrey Dahmer', 'Gary Ridgway', 'Dennis Rader']
    encounter = random.choice(entities)
    if encounter == 'Human':
        name = random.choice(human_names)
    elif encounter == 'Visitor':
        name = random.choice(visitor_names)
    else:
        name = random.choice(killer_names)
    return encounter, name

def determine_pronouns(name):
    female_names = {'Lynda Ann Healy', 'Laura Ann Aime', 'Bernice Worden', 'Aileen Wuornos'}
    male_names = {'Konerak Sinthasomphone', 'Steven Walter Tuomi', 'Richard Ramirez', 'Marcel Petiot', 'David Berkowitz',
                  'Theodore Bundy', 'John Wayne Gacy', 'Jeffrey Dahmer', 'Gary Ridgway', 'Dennis Rader', 'Deputy Sheriff Frank Worden'}
    if name in female_names:
        return 'she', 'her'
    if name in male_names:
        return 'he', 'his'
    return 'they', 'their'

def interaction_loop(encounter, name):
    subj_pron, poss_pron = determine_pronouns(name)
    print("You encounter a person at the door.")
    time.sleep(3)
    print(f"The person's name is {name}. It's unknown whether they are human, visitor, or something else.")
    time.sleep(3)
    while True:
        print("\nAvailable actions: 'ask name', 'ask purpose', 'inspect', 'let in', 'refuse'")
        action = input("What are u doing?").strip().lower()
        time.sleep(1)

        if action == 'ask name':
            print(f"{name}: \"My name is {name}.\"")
            time.sleep(2)
            print(f"{name} smiles and greets you. {poss_pron.capitalize()} smile is warm; {subj_pron} meets your eyes with a steady gaze.")
            time.sleep(2)
            paragraph = (f"As {poss_pron} words settle into the night air, you study {poss_pron} face: a measured, easy smile, "
                         f"hands that fold and unfold with small, deliberate motions, and eyes that hold yours a fraction of a second too long. "
                         f"{poss_pron.capitalize()} voice is calm and practiced, carrying a warmth that might be genuine—or carefully copied. "
                         f"For an instant you feel reassured by the familiarity in {poss_pron} expression, then a subtle dissonance pricks at the back of your neck—"
                         f"an odd cadence, a blink that doesn't quite match the rest of the face. You can't decide if it's kindness or careful mimicry, "
                         f"but the impression remains as {subj_pron} waits for your next move.")
            print(paragraph)
            time.sleep(3)

        elif action == 'ask purpose':
            if encounter == 'Human':
                reply = f"{name}: \"I'm just passing through, heard someone call for help earlier.\""
                paragraph = (f"{reply} As the words leave {poss_pron} lips, {subj_pron} looks genuinely unsettled — "
                             f"a quick, apologetic smile, a slight tremor at the edge of {poss_pron} voice. "
                             f"You notice the small, human details: the way {poss_pron} hands fidget, the honest breaks in {poss_pron} sentence, "
                             f"all of which make {poss_pron} seem tired and harmless.")
                print(reply)
                print(paragraph)
                time.sleep(3)
            elif encounter == 'Visitor':
                reply = f"{name}: \"I... lost my way. The light outside hurt my eyes.\""
                paragraph = (f"{reply} The phrasing feels off, each clause arriving a fraction late as if copied from somewhere else. "
                             f"{poss_pron.capitalize()} eyes don't linger on yours but flick past, and there's a stillness around {poss_pron} that feels wrong — "
                             f"too composed, too precise. Tiny mismatches in {poss_pron} mannerisms set your nerves on edge.")
                print(reply)
                print(paragraph)
                time.sleep(3)
            else:  # Killer
                reply = f"{name}: \"I need help. My car broke down.\""
                paragraph = (f"{reply} The delivery is flat and practiced, as if the words were chosen for effect. "
                             f"{poss_pron.capitalize()} holds your gaze without the quick, involuntary microexpressions that give humans away; "
                             f"there is a cold efficiency to {poss_pron} speech that makes your skin crawl. Every slowed blink and measured pause feels deliberate.")
                print(reply)
                print(paragraph)
                time.sleep(3)

        elif action == 'inspect':
            if encounter == 'Human':
                paragraph = (f"You study {name} closely. {poss_pron.capitalize()} breathing is even and unforced, "
                             f"microexpressions come and go naturally, and there are small, honest hesitations in {poss_pron} speech. "
                             f"You notice the way {poss_pron} hands fidget with a ring or a sleeve, the fatigue at {poss_pron} eyes — "
                             f"all the little, human details that make you relax a fraction. This feels like someone genuinely out of sorts rather than a threat.")
                print(paragraph)
                time.sleep(3)
            elif encounter == 'Visitor':
                paragraph = (f"On inspection, something slips under your skin. {poss_pron.capitalize()} skin has an odd sheen, "
                             f"and {poss_pron} smile doesn't quite match the movement of {poss_pron} eyes. Micro-mismatches — a blink that lags, "
                             f"phrases that repeat with slightly wrong emphasis — make the whole encounter feel copied rather than lived. "
                             f"There's a mechanical precision to {poss_pron} gestures that raises the hairs on your arms.")
                print(paragraph)
                time.sleep(3)
            else:   # Killer
                paragraph = (f"Every detail reads as a warning. {poss_pron.capitalize()} movements are deliberate and too controlled, "
                             f"{poss_pron} breathing is shallow, and {poss_pron} gaze is fixed in a way that doesn't feel social. "
                             f"You notice a faint grease on {poss_pron} fingers, the too-calm cadence of {poss_pron} voice, and the absence of small, nervous ticks — "
                             f"it all points to someone who is composed for a reason other than being lost.")
                print(paragraph)
                time.sleep(3)

        elif action == 'let in':
            print(f"You step aside and gesture for {name} to enter.")
            time.sleep(2)
            if encounter == 'Human':
                print(f"{name} thanks you, stepping in with a relieved breath. {poss_pron.capitalize()} moves with ordinary clumsiness, sets {poss_pron} bag down, and chats about the weather. You feel a measure of relief.")
                time.sleep(2)
                return True, 'let_in_human'
            elif encounter == 'Visitor':
                print(f"{name} slips inside with an eerie grace. Once the door closes, you notice the air feels colder; the light seems to shift. You keep one eye on the doorway as {poss_pron} moves through your home. Something about {poss_pron} presence is wrong — you quietly make a note to lock other doors.")
                time.sleep(2)
                return True, 'let_in_visitor'
            else:  # Killer
                print(f"{name} walks in with a slow, deliberate step. {poss_pron.capitalize()} thanks you with a smile that doesn't reach {poss_pron} eyes. You suddenly regret your choice as {poss_pron} moves deeper into the house.")
                time.sleep(2)
                return False, 'let_in_killer'

        elif action == 'refuse':
            print(f"You close the door gently and put your shoulder against it. \"I'm sorry, I can't let you in right now.\"")
            time.sleep(2)
            if encounter == 'Human':
                print(f"{name} looks wounded. {poss_pron.capitalize()} voice cracks: \"Please, I'm freezing. I just need a phone, that's all.\" {subj_pron.capitalize()} pleads, eyes wet. You hold firm, offering a glass of water through the letterbox instead.")
                time.sleep(3)
                return True, 'refused_human'
            elif encounter == 'Visitor':
                print(f"{name} tilts {poss_pron} head unnaturally and smiles too widely. \"That's okay,\" {poss_pron} says, voice soft and wrong. \"I'll wait.\" The patience feels patient and patientless at once — as if {subj_pron} can wait forever for an opening. You bar the door and call out that help is coming, hoping to break whatever calm {poss_pron} brings.")
                time.sleep(3)
                print(f"The visitor's knuckles rap the door in a slow, hollow rhythm. You count the beats and feel them in your chest.")
                time.sleep(2)
                return True, 'refused_visitor'
            else:  # Killer
                print(f"{name}'s expression hardens. \"Fine,\" {poss_pron} says, voice low. \"But you won't sleep easy tonight.\" The tone leaves no room for bargaining. {subj_pron.capitalize()} walks away with long, measured steps; you can hear them pause at the curb before disappearing into the dark.")
                time.sleep(3)
                return True, 'refused_killer'
        else:
            print("Invalid choice. Please type 'ask name', 'ask purpose', 'inspect', 'let in', or 'refuse'.")
            time.sleep(3)

# main repeat encounters loop
while encounters_handled < max_encounters and alive:
    # simulate knock
    timer = 2
    start_timer = time.time()
    while time.time() - start_timer < timer:
        pass
    print("\nYou hear a knock on the door...")
    time.sleep(3)
    print("Who could that be at this hour?")
    time.sleep(3)

    # ask whether to open
    chances = 3
    door_opened = False
    while chances > 0:
        response = input("Do you want to 'open' the door or 'ignore' it? ").strip().lower()
        time.sleep(1)
        if response == 'open':
            door_opened = True
            break
        if response == 'ignore':
            chances -= 1
            if chances == 0:
                print("The knocking stops after a while.")
            else:
                print(f"You have {chances} chances left to open the door.")
        else:
            print("Please type 'open' or 'ignore'.")

    if not door_opened:
        # no encounter this knock, continue listening for next knock
        continue

    # generate an encounter and run interaction
    encounter, name = pick_encounter()
    survived, door_action = interaction_loop(encounter, name)

    # record visitors if suspicious visitor let in or refused
    if door_action == 'let_in_visitor' or door_action == 'refused_visitor':
        visitors_found.append(name)

    # handle aftermath based on door_action
    if door_action == 'let_in_human':
        print("\nInside: The visitor — actually a weary human — settles on your couch and you talk for a while. They seem harmless and passes along a small warning about strange lights to the north.")
        time.sleep(2)
        print(f"{name} leaves quietly before dawn, leaving a faint scent of rain on {determine_pronouns(name)[1]} coat.")
    elif door_action == 'let_in_visitor':
        print("\nInside: The atmosphere shifts. The temperature drops and shadows lengthen where they pass.")
        time.sleep(2)
        print(f"{name} moves through the rooms with unnerving calm. Objects near where {determine_pronouns(name)[1]} pauses feel slightly colder; a single bulb flickers then steadies.")
        time.sleep(2)
        print("You notice later that a small glass on the coffee table has been tipped and a family photo shifted. It's subtle — like a line of ink smudged at the edge of a page.")
        time.sleep(2)
        print("You mark this name as suspicious and resolve to keep a closer watch.")
    elif door_action == 'let_in_killer':
        print("\nInside: The moment the door closes the mood ruptures. You feel a presence move with intent.")
        time.sleep(2)
        print("Before you can react, there is a sudden lunge and a bright, painful shock of violence. You scramble for something to defend yourself.")
        time.sleep(2)
        print("GAME OVER — you should have not let them in.")
        alive = False
        break
    elif door_action == 'refused_human':
        print("\nAftermath: The human leaves, calling back a soft 'thank you' as they walk away. Later you find a folded scrap of paper tucked under the door with a simple message: 'Be careful.'")
        time.sleep(2)
    elif door_action == 'refused_visitor':
        print("\nAftermath: The visitor's patience becomes an echo. For hours you hear soft tapping at random windows and a faint hum outside that sounds almost like singing. When you check, there's nothing but a single, strange footprint in the mud by the side gate.")
        time.sleep(2)
        print("You add the footprint and the name to your notes; this one feels wrong in a way that doesn't end at the door.")
    elif door_action == 'refused_killer':
        print("\nAftermath: The killer walks away but the threat lingers. Late that night you hear someone pacing the far side of the house, testing locks and listening for movement.")
        time.sleep(2)
        print("You stay awake, weapon at hand, and keep the lights low. This one may have left — but it hasn't forgotten your refusal.")
        time.sleep(2)

    encounters_handled += 1

    if not survived:
        alive = False
        break

# end result branching
if not alive:
    print("\nBad Ending: You did not survive the encounter.")
    time.sleep(3)
    # here the possible or literally can end game or offer restart logic
else:
    if encounters_handled >= max_encounters:
        print(f"\nYou survived {encounters_handled} encounters. You've reached the limit of {max_encounters}.")
        time.sleep(3)
        if visitors_found:
            print("Suspicious names found during the night:")
            time.sleep(3)
            for v in visitors_found:
                print(f" - {v}")
        else:
            print("You didn't mark any suspicious visitors tonight.")
            time.sleep(3)
    else:
        print("\nThe night quiets for now.")
        time.sleep(3)

# Pale Visitor (night-end recurring antagonist)
import random
pale = {
    'name': 'Pale Visitor',
    'desc_player': (
        "He is naked except for dark pants. Pale skin hangs in strange folds — the skin looks too big for him. "
        "Broad shoulders, freakishly long, skinny arms, short black hair and an eerie grin that shows perfectly white teeth."
    ),
    'desc_bearded': (
        "Tall, naked as a babe, pale as if he'd seen death itself."
    )
}

# Trigger the Pale Visitor event at night end if the player survived the night's knocks
if encounters_handled >= max_encounters and alive:
    print("\nAs the night draws thin, something else arrives — a shape that doesn't belong to the world you know.")
    time.sleep(2)
    print(f"You remember whispers about the {pale['name']}...")
    time.sleep(2)
    print(f'Protagonist: "{pale["desc_player"]}"')
    time.sleep(2)
    print(f'Bearded Guy: "{pale["desc_bearded"]}"')
    time.sleep(2)

    pale_active = True
    barricaded = False

    while pale_active and alive:
        print("\nYou hear long, deliberate knocks that don't sound quite like wood on wood.")
        time.sleep(3)
        print("Available actions: 'barricade', 'hide', 'listen', 'confront'")
        choice = input("What do you do? ").strip().lower()
        time.sleep(3)

        if choice == 'barricade':
            if not barricaded:
                print("You throw furniture against the door and slide the heavy bolt into place. The house feels sturdier.")
                barricaded = True
                time.sleep(2)
                # chance the Pale tries but can't enter; it will return another night (remains a threat)
                if random.random() < 0.75:
                    print("Something enormous tests the door from the other side. It scrapes and sighs, then moves away into the dark.")
                    time.sleep(2)
                    print("You survive this visit, but the thing hasn't forgotten you.")
                    time.sleep(2)
                    visitors_found.append(pale['name'])
                    pale_active = False
                else:
                    print("The bolt holds, but you hear a sudden, terrible silence as it leans closer to the glass. You hold your breath until it passes.")
                    time.sleep(2)
                    visitors_found.append(pale['name'])
                    pale_active = False
            else: 
                print("The door is already well-barricaded. You wait in tense silence.")
                time.sleep(2)
                time.sleep(2)

        elif choice == 'hide':
            print("You slip into the shadows and try to make yourself as small as possible.")
            time.sleep(2)
            # hiding has a moderate chance to succeed
            if random.random() < 0.6:
                print("The Pale moves through the house like a cold wind but does not find you. After a long while it leaves.")
                time.sleep(2)
                visitors_found.append(pale['name'])
                pale_active = False
            else:
                print("A long arm brushes past your hiding place. You are found.")
                time.sleep(3)
                print("GAME OVER — the Pale Visitor takes you.")
                time.sleep(5)
                alive = False
                pale_active = False

        elif choice == 'listen':
            print("You press your ear to the wall and listen. The sound is a low, patient breathing and a wet, skeletal grin against the glass.")
            time.sleep(2)
            print("You gain a small insight: it dislikes light and strong smells.")
            time.sleep(2)
            print("Actions that use light or fire may keep it at bay next time.")
            time.sleep(3)
            visitors_found.append(pale['name'])
            pale_active = False

        elif choice == 'confront':
            print("You step forward to face it. For a heartbeat you meet that terrible grin.")
            time.sleep(3)
            # confronting is high risk
            if random.random() < 0.2:
                print("Against all odds you strike true and it recoils, slipping away into the night. You live, but the wound in your mind remains.")
                visitors_found.append(pale['name'])
                pale_active = False
            else:
                print("It moves with impossible speed. Everything goes black.")
                time.sleep(3)
                print("GAME OVER — you confronted the Pale Visitor.")
                time.sleep(5)
                alive = False
                pale_active = False 
        else:
            print("Invalid action. Try 'barricade', 'hide', 'listen', or 'confront'.")
            time.sleep(3)
    # No additional random event after the loop
else:
    # No invalid action here since it's after the if
# After the Pale Visitor event, summarize outcome
    if not alive:
        print("\nBad Ending: The Pale Visitor claimed you.")
        time.sleep(5)
    else:
        print("\nDawn approaches. For now you survived — but the Pale Visitor has left its mark on the night.")
        time.sleep(3)
        if visitors_found:
            print("Names/events noted for later:")
            time.sleep(3)
            for v in visitors_found:
                print(f" - {v}")
clear()
prompt()

# DAY 2 
import time, random, os

# Clears the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Check if player survived Day 1
if alive:
    clear()
    print("\nDAY 2 — MORNING\n")
    time.sleep(2)
    print("You wake up to faint static from the radio again. The world outside is quiet, too quiet......")
    time.sleep(3)
    print("The first rays of sunlight spill across the living room floor, filtered through dust motes that drift lazily in the still air.")
    time.sleep(4)
    print("Your mind replays the knocks from last night, every slow breath, every shadow behind the glass.")
    time.sleep(4)
    input("\nPress any key to get up...")
    clear()
    print("You stretch and check the doors. Everything’s still locked, though the air feels heavier than it should.")
    time.sleep(4)
    print("No messages. No phone signal. Only the faint hum of silence, and maybe, just maybe, a whisper behind the walls.")
    time.sleep(4)
    input("\nPress any key to continue...")

    # Start of Day 2 Gameplay

    clear()
    print("DAY 2 — EVENING\n")
    time.sleep(2)
    print("You decide to stay alert tonight. The memory of the last encounter lingers, but the air feels... different now.")
    time.sleep(4)
    print("Fewer human sounds. Fewer footsteps. More stillness — as if the world is holding its breath.")
    time.sleep(3)
    input("\nPress any key to prepare for the night...")

    clear()
    print("The second night begins. You set up a lantern, grab your notes, and wait.")
    time.sleep(3)
    print("Outside, faint lights flicker between the trees — not flashlights, but something colder.")
    time.sleep(3)

    # Night 2 — Encounters
    max_encounters_day2 = 5
    encounters_handled_day2 = 0
    alive_day2 = True

    def pick_encounter_day2():
        entities = ['Visitor', 'Visitor', 'Visitor', 'Human', 'Killer']  
        human_names = ['William', 'Sarah', 'Megan']
        visitor_names = ['Noa', 'Vel', 'Iskar', 'Tala', 'Ren']
        killer_names = ['Unknown Figure']

        encounter = random.choice(entities)
        if encounter == 'Human':
            name = random.choice(human_names)
        elif encounter == 'Visitor':
            name = random.choice(visitor_names)
        else:
            name = random.choice(killer_names)
        return encounter, name

    # Gameplay loop
    while encounters_handled_day2 < max_encounters_day2 and alive_day2:
        print("\nYou hear a soft, almost polite knock at the door...")
        time.sleep(2)
        print("It’s quieter than last night, but it feels... deeper somehow.")
        time.sleep(2)

        response = input("Do you want to 'open' the door or 'ignore' it?").strip().lower()
        time.sleep(1)

        if response != 'open':
            print("You stay quiet. The sound fades replaced by a faint hum, like metal vibrating in the walls.")
            time.sleep(3)
            encounters_handled_day2 += 1
            continue

        # Generate encounter
        encounter, name = pick_encounter_day2()
        print(f"\nYou open the door slowly and find someone — or something — standing outside.")
        time.sleep(2)
        survived, door_action = interaction_loop(encounter, name)

        if door_action == 'let in human':
            print("\nInside: The human seems calmer than most. They talk softly, as if aware of the silence pressing in from outside.")
            time.sleep(3)
            print(f"Before leaving, {name} mentions strange lights in the sky. 'They’re not stars,' {name} says, before disappearing into the fog.")
            time.sleep(3)

        elif door_action == 'let in visitor':
            print("\nInside: The figure steps in gracefully. Their movements feel almost fluid, like water remembering how to be human.")
            time.sleep(3)
            print("They glance around your living room, touching objects curiously — the photos, the books, the television.")
            time.sleep(3)
            print("When they finally speak, their voice sounds like a thousand echoes trying to mimic one person.")
            time.sleep(3)
            print(f"'{name}': 'We were here... before you knew the word home.'")
            time.sleep(3)
            print("They leave without noise, but you notice a faint light residue on the doorknob after they’re gone.")
            time.sleep(3)
            visitors_found.append(name)

        elif door_action == 'refused visitor':
            print("\nAftermath: The figure doesn’t protest. Instead, it stands there — motionless — until the fog swallows it whole.")
            time.sleep(3)
            print("Later that night, you hear a faint hum coming from under the floorboards, like a tune played on old wires.")
            time.sleep(3)
            visitors_found.append(name)

        elif door_action == 'let_in_killer':
            print("\nThe figure steps inside too quickly. The silence snaps like glass. You feel cold")

 # Day 3

import time, random, os

def clear():
    os.system('cls' if os.name == 'nt'else 'clear')
#Check if player alive in day2
if alive_day2:
    clear()
    print("\nDay 3 - MORNING\n")
    time.sleep(2)
    print("The morning light feels colder today.")
    time.sleep(2)
    print("You wake to the soft crackle of static again but the time, the voice almost sound like it's trying to form words.")
    time.sleep(3)
    print("Your notebook lies on table and open the pages even though there's no breeze.")
    time.sleep(3)
    input("\nPress any key to get up...")
    
    clear()
    print("You make Coffe though the taste feels hollow, like memory more than flavor.")
    time.sleep(3)
    print("Outside, the fog hasn't lifted. Shapes move within it's not people, not animals, just... movement.")
    time.sleep(3)
    print("The world feels slightly off now, as in someone shifted the rules overnight.")
    time.sleep(3)
    input("\nPress any key to continue...")
    
    
    #Start of Day 3 Gameplay
    clear()
    print("DAY 3 — EVENING\n")
    time.sleep(2)
    print("You sit by the windows as dusk falls, radio beside you. It build into a low, rhythmic pulse.")
    time.sleep(3)
    print("It almost syncs with your heartbeat.")
    time.sleep(2)
    print("Then, a new sound join in faint footstep outside, moving like a circle in the house.")
    time.sleep(3)
    input("\nPress any key to prepare for the night begins...")
    
    clear()
    print("The third night begins. You light your lantern again, though it's glow seems weaker than before.")
    time.sleep(3)
    print("A knock comes not at the door, but at the windows. Three times,Slow,Careful.")
    time.sleep(3)
    
    #Night 3 Encounters
    max_encounters_day3 = 6
    encounters_handled_day3 = 0
    alive_day3 = True
    
    def pick_encounter_day3():
        entities = ['Visitor', 'Human', 'Killer']
        human_names = ['Charlie', 'Cris', 'Marcus']
        visitors_names = ['Juan', 'Robby', 'Che', 'Felix']
        killer_names =['Unknown Figure'] 

        encounter = random.choice(entities)
        if encounter == 'Human':
            name = random.choice(human_names) 
        elif encounter == 'Visitor': 
            name = random.choice(visitor_names) 
        elif encounter == 'Mimic': 
            name = random.choice(mimic_names) 
        else:
            name = random.choice(killer_names)
        return encounter, name
    

    while encounters_handled_day3 < max_encounters_day3 and alive_day3:
        print("\nA knock echoes again  this time from the opposite side of the house.")
        time.sleep(2)
        print("Who ever or what ever  it is, its learning the rhythm of your breathing.")
        time.sleep(2) 


    response = input("Do you want to 'open' the door or 'stay quiet'? ").strip().lower()
    time.sleep(1)
    
    
    if response != 'open':
        print("You hold your breath. The sound lingers longer than it should as if waiting for you to slip.")
        time.sleep(3)
        encounters_handled_day3 += 1
        continue
    
    #Generate encounter 
    encounter, name = pick_encounter_day3()
    print(f"\nYou open the door slowly. Fog drift inside like it's alive.")
    time.sleep(2)
    survived, door_action = interaction_loop(encounter,name)
    
    
    if door_action == 'let_in_human':
        print(f"\nInside: {name} looks exhausted, soaked from the mist.")
        time.sleep(3)
        print(f"They whisper, 'The fog listens now. Don't talk near the windows.' Then they leave, vanishing almost instantly.")
        time.sleep(3)
        
        
    elif door_action == 'let_in_visitor':
        print("\nThe figure glides in. Their skin flickers like static under the lantern light.")
        time.sleep(3)
        print(f"'{name}': 'Your world blinks... soon ours will open again.'")
        time.sleep(3)
        visitors_found.append(name)
    
    
    elif door_action == 'refused_visitor':
        print("\nYou close the door, heart pounding.")
        time.sleep(2)
        print("The fog outside ripples, almost breathing. You hear a faint hum beneath your
floorboards again.")
        time.sleep(3)
        visitors_found.append(name)
    
    
    elif door_action == 'let_in_killer':
        print("\nThe door bursts open before you can react.")
        time.sleep(2)
        print("Cold hands seize your throat. Theres no time to scream  just the faint crackle of the radio, whispering: 'too late.'")
        time.sleep(3)
        alive_day3 = False
        break
    
    elif door_action == 'let_in_mimic':
        print(f"\nThe figure looks exactly like you, Same clothes, Same eyes.")
        time.sleep(3)
        print(f"'{name}': 'I was just making sure you're still real.")
        time.sleep(3)
        print("You blink, and they are gone, leaving only your reflection on the glass, smiling back when you dont.")
        time.sleep(3)
        
    encounters_handled_day3 +=1


if alive_day3:
    clear()
    print("\nDay 3 — SURVIVED\n")
    time.sleep(2)
    print("You made it through another night. The fog hums like its alive, but the radio... the radio is changing.")
    time.sleep(3)
    print("A voice whispers your name this time.")
    time.sleep(3)
    print("Tomorrow, it might start talking back.")
    time.sleep(3)
    input("\nPress any key to end Day 3...")
    
else:
    clear()
    print("\nGAME OVER — Day 3")
encounters_handled_day3 +=1


if alive_day3:
    clear()
    print("\nDay 3 — SURVIVED\n")
    time.sleep(2)
    print("You made it through another night. The fog hums like its alive, but the radio... the radio is changing.")
    time.sleep(3)
    print("A voice whispers your name this time.")
    time.sleep(3)
    print("Tomorrow, it might start talking back.")
    time.sleep(3)
    input("\nPress any key to end Day 3...")
    
else:
    clear()
    print("\nGAME OVER — Day 3")encounters_handled_day3 +=1


if alive_day3:
    clear()
    print("\nDay 3 — SURVIVED\n")
    time.sleep(2)
    print("You made it through another night. The fog hums like its alive, but the radio... the radio is changing.")
    time.sleep(3)
    print("A voice whispers your name this time.")
    time.sleep(3)
    print("Tomorrow, it might start talking back.")
    time.sleep(3)
    input("\nPress any key to end Day 3...")
    
else:
    clear()
    print("\nGAME OVER — Day 3")


    # === DAY 4 ===
import time, random, os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

if alive_day3:
    clear()
    print("\nDAY 4 — MORNING\n")
    time.sleep(2)
    print("You wake to the sound of whispering radio static — except this time, it’s forming words.")
    time.sleep(3)
    print("The voice isn’t quite human. It sounds like every voice you've heard before, speaking in unison.")
    time.sleep(4)
    print('"You have lasted longer than most," it says, calm and cold. "But the night wants you now."')
    time.sleep(4)
    input("\nPress any key to stand up...")

    clear()
    print("The fog outside glows faintly blue. Shapes drift through it — familiar silhouettes that shouldn’t be there.")
    time.sleep(3)
    print("When you blink, you see your own reflection waving from the window, smiling.")
    time.sleep(3)
    print("You feel a sharp pulse in your head, as though something is trying to *tune* into you.")
    time.sleep(3)
    input("\nPress any key to prepare for the final night...")

    clear()
    print("DAY 4 — NIGHTFALL\n")
    time.sleep(2)
    print("The air buzzes with invisible static. The radio hums with the rhythm of your own heartbeat.")
    time.sleep(3)
    print("You realize the Visitors have learned your voice, your habits, your name.")
    time.sleep(3)
    print("You are not just the observer tonight — you are the signal.")
    time.sleep(3)

    # Gameplay setup
    max_encounters_day4 = 7
    encounters_handled_day4 = 0
    alive_day4 = True
    radio_trust = False  # new mechanic

    def pick_encounter_day4():
        entities = ['Visitor', 'Killer', 'Mimic', 'Signal']
        visitor_names = ['Vel', 'Tala', 'Ren', 'Echo']
        killer_names = ['Unknown Figure', 'Bearded Man']
        mimic_names = ['You', 'Father']
        signal_names = ['Static Voice']
        encounter = random.choice(entities)
        if encounter == 'Visitor':
            name = random.choice(visitor_names)
        elif encounter == 'Killer':
            name = random.choice(killer_names)
        elif encounter == 'Mimic':
            name = random.choice(mimic_names)
        else:
            name = random.choice(signal_names)
        return encounter, name

    # Loop through encounters
    while encounters_handled_day4 < max_encounters_day4 and alive_day4:
        print("\nThe house hums. Then, instead of a knock, your radio clicks on by itself.")
        time.sleep(2)
        print("A voice says softly, 'Someone is at your door. Do not look directly at them.'")
        time.sleep(3)
        response = input("Do you 'trust radio' or 'check door' anyway? ").strip().lower()

        if response == 'trust radio':
            print("You stay still, eyes shut. You hear something brush against the doorframe, then retreat.")
            time.sleep(2)
            radio_trust = True
            encounters_handled_day4 += 1
            continue
        elif response == 'check door':
            print("You open the door — the fog is thicker than ever, swallowing your porch light.")
            time.sleep(3)
            encounter, name = pick_encounter_day4()
            survived, door_action = interaction_loop(encounter, name)
            
    # === Final Sequence ===
    if alive_day4:
        clear()
        print("\nFINAL SEQUENCE\n")
        time.sleep(2)
        print("The sun never rises. The fog parts to reveal thousands of shapes standing motionless — Visitors, Humans, Mimics, all facing your house.")
        time.sleep(4)
        if radio_trust:
            print("Your radio whispers, 'You listened. That means you remember what it’s like to be human.'")
            time.sleep(3)
            print("You pick up the radio and speak into it. Your voice echoes across the fog, and some of the figures lower their heads.")
            time.sleep(3)
            print("For a moment, the hum quiets. You have not defeated the Visitors — but they remember your name now.")
            time.sleep(3)
            print("ENDING: The Broadcast — You survived by trusting the unknown.")
        else:
            print("The radio bursts into static, voices screaming over each other.")
            time.sleep(3)
            print("You see your reflection in every window, each smiling wider than the last.")
            time.sleep(3)
            print("As dawn breaks, the world outside is gone — only copies remain.")
            time.sleep(3)
            print("ENDING: The Echo — You became one of them.")
    else:
        clear()
        print("\nGAME OVER — The house is silent again.")
        time.sleep(3)
        print("Somewhere in the fog, a radio hums with your voice, asking someone else: 'Do you want to open the door?'")
        time.sleep(3)
        # === DAY 4 ===
import time, random, os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

if alive_day3:
    clear()
    print("\nDAY 4 — MORNING\n")
    time.sleep(2)
    print("You wake to the sound of whispering radio static — except this time, it’s forming words.")
    time.sleep(3)
    print("The voice isn’t quite human. It sounds like every voice you've heard before, speaking in unison.")
    time.sleep(4)
    print('"You have lasted longer than most," it says, calm and cold. "But the night wants you now."')
    time.sleep(4)
    input("\nPress any key to stand up...")

    clear()
    print("The fog outside glows faintly blue. Shapes drift through it — familiar silhouettes that shouldn’t be there.")
    time.sleep(3)
    print("When you blink, you see your own reflection waving from the window, smiling.")
    time.sleep(3)
    print("You feel a sharp pulse in your head, as though something is trying to *tune* into you.")
    time.sleep(3)
    input("\nPress any key to prepare for the final night...")

    clear()
    print("DAY 4 — NIGHTFALL\n")
    time.sleep(2)
    print("The air buzzes with invisible static. The radio hums with the rhythm of your own heartbeat.")
    time.sleep(3)
    print("You realize the Visitors have learned your voice, your habits, your name.")
    time.sleep(3)
    print("You are not just the observer tonight — you are the signal.")
    time.sleep(3)

    # Gameplay setup
    max_encounters_day4 = 7
    encounters_handled_day4 = 0
    alive_day4 = True
    radio_trust = False  # new mechanic

    def pick_encounter_day4():
        entities = ['Visitor', 'Killer', 'Mimic', 'Signal']
        visitor_names = ['Vel', 'Tala', 'Ren', 'Echo']
        killer_names = ['Unknown Figure', 'Bearded Man']
        mimic_names = ['You', 'Father']
        signal_names = ['Static Voice']
        encounter = random.choice(entities)
        if encounter == 'Visitor':
            name = random.choice(visitor_names)
        elif encounter == 'Killer':
            name = random.choice(killer_names)
        elif encounter == 'Mimic':
            name = random.choice(mimic_names)
        else:
            name = random.choice(signal_names)
        return encounter, name
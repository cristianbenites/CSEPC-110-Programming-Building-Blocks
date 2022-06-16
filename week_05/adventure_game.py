"""
Title: Adventure Game
Author: Cristian Benites

"""

"""
The class Scenario set each level with its content, questions and possible answers (which are other Scenarios).
It also is prepared for invalid inputs and accepts the words QUIT and EXIT to exit the game.
Once and input matches the dictionary of Level options, it executes the proper chosen Scenario
When a Scenario doesn't have children (option paths), it its considered end game, so the text content is printed
as well as the final message.

"""
class Scenario:
    def __init__(
            self,
            options: dict = {},
            text = '',
            action_question = ''
        ):
            self.options = options
            self.text = text
            self.action_question = action_question,
            self.wrong_choice_error = "\nWHOOPS!\nI couldn't understand your choice, please write one of the words in uppercase.\n" \
                "Let's try again\n" \
                "If you want to quit the game, type QUIT or EXIT\n\n"

    def __call__(self):
        self.run()

    def has_options(self):
        return len(self.options) > 0

    def set_options(self, options: dict):
        self.options = options

    def set_text(self, text):
        self.text = text

    def set_action_question(self, action_question):
        self.action_question = action_question

    def get_next_action(self):
        action_command = input(f"{self.action_question}\n>> ").upper()
        next_action = self.options.get(action_command)

        if (next_action):
            next_action()
        elif(action_command == 'EXIT' or action_command == 'QUIT'):
            print("You left the game. See you next time! :)")
            exit()
        else:
            print(self.wrong_choice_error)
            self.get_next_action()

    def run(self):
        print(self.text)

        if(self.has_options()):
            self.get_next_action()
        else:
            print("\n\nCongratulations! You've finished the game. Try other choices and discover new paths next time!!! \\o/")


"""
First, we instantiate all scenarios, their text content and their action questions

"""
level01 = Scenario()
level01.set_text("It's the weekend, you're fishing in a forest far from the city.\n"
    "It's starting to get dark and you steer the boat towards the shore near your camp.\n"
    "Your tent is on a lawn by the river."
    "As the boat approaches, you see a shadow, a mysterious dark object, on the ground, right close to the tent, "
    "but you can't identify what it is.")
level01.set_action_question("Do you want to get off the boat and go to SEE what "
    "that \"mystery shadow\" is, or move the boat away "
    "from the shore and WAIT?")

level02_see = Scenario()
level02_see.set_text("You leave the boat and as you approach it, you realize that it is an alligator. "
    "The alligator notices your presence and runs towards you. You have a knife in your belt.")
level02_see.set_action_question("Do you want to FIGHT or RUN?")

level03_fight = Scenario()
level03_fight.set_text("You stab the alligator in the back.\n"
    "He tries to bite and you pull away, he lunges at you.\n"
    "You trip and fall into the river, it's knee-high water.\n"
    "The boat is right beside you.")
level03_fight.set_action_question("Do you want to get on the BOAT or ATTACK the alligator again?")

level04_boat = Scenario()
level04_boat.set_text("You manage to get on the boat before the alligator reaches you, he enters the water with his back bleeding and leaves.\n"
    "You feel relieved. The danger is gone. Now you can go home safely...")

level05_attack = Scenario()
level05_attack.set_text("The alligator opens its mouth towards you, you get up quickly and stab the alligator again. "
    "He stops, moves slowly towards the river and floats as if he had died. "
    "You see him floating in the current, not knowing if he actually died, "
    "until he disappears into the dark of night.\n"
    "The danger is gone, you feel relieved, after all, few survive an alligator attack.")

level06_run = Scenario()
level06_run.set_text("You run along the riverbank as the sun completely sets."
    "You don't see the alligator any more. It's dark and your references are only the "
    "river on your side and the dark forest on the other.\n"
    "You have a small flashlight in your pocket.")
level06_run.set_action_question("Do you want to go BACK and try to take you tent "
    "or enter the FOREST and look for the path that leads to the road?")

level07_back = Scenario()
level07_back.set_text("You return to camp just in time to see that the alligator "
    "entering the water and leaving. You feel relieved.\n"
    "Hopefully, the road is close to where you pitched the tent, so you can go back "
    "there and not have to spend the night in the woods. Since camping in this place "
    "proved to be quite dangerous.")

level08_forest = Scenario()
level08_forest.set_text("You enter the woods, looking for the trail that leads back to the highway. "
    "After a few minutes of walking you find it, and head towards your car, on the side of the highway. "
    "This fishing proved dangerous. You will wait the night in the car safely and only tomorrow pick up your tent.")

level09_wait = Scenario()
level09_wait.set_text("You wait for a few minutes, shining with your flashlight from time to time, "
    "towards the tent. Then, you don’t see the \"shadow\" anymore.\n"
    "You approach the tent, enter it and start getting ready for bed. Suddenly, you hear a loud, "
    "rumbling sound very close to your camp. It's a gunshot noise. You get scared and think: what "
    "could it be? Soon you hear footsteps grinding the dry leaves. You see the light of a flashlight. "
    "Footsteps approach towards you. Then, you can see: it is a hunter. He just killed an alligator.\n"
    "He bends down to see the game. You know that hunting in this place is forbidden, that is, you have just witnessed a crime.")
level09_wait.set_action_question("Do you want to TALK to the hunter, SNEAK away, "
    "or keep QUIET and hope he doesn't see your tent?")

level10_talk = Scenario()
level10_talk.set_text("You approach and start chatting amicably. The hunter is startled when he hears your voice, "
    "but as your voice sounds friendly, he responds in the same way. You say you're fishing and camping. "
    "He tells you, a little awkwardly, that he knows it's a crime, but that he had to hunt, however, "
    "without explaining why.")

level11_sneak = Scenario()
level11_sneak.set_text("You start carefully walking out of the tent. However, your footsteps make noise when stepping on dry leaves. "
    "The hunter sees you, points his rifle and asks:\n"
    "--- Who's there? Who are you?\n"
    "You respond in a calm tone, saying that you are just a fisherman and that you are camping. He says, "
    "in a threatening tone, that he's just passing through, that he's going to take the animal and leave. "
    "He ends by saying that you'd better not tell anyone what you saw. The hunter then ties the animal up, "
    "slings it over his shoulders, and leaves.\n"
    "You feel afraid and think: maybe it's better not to come alone next time...")

level12_quiet = Scenario()
level12_quiet.set_text("You know that poachers can always be dangerous, you also think that if you try to sneak out, you can make a "
    "lot of noise when stepping on dry leaves. However, he may end up seeing your tent. You decide to keep quiet "
    "anyway. You watch the hunter prepare the game by tying it with a rope. He then puts the alligator over his shoulders and walks away.\n"
    "\nIt was pure luck! You feel grateful that he's so focused on the dying alligator that he didn't observe your "
    "tent or the boat. You wonder on whether it was unwise to come camping in the forest alone...")


"""
Now, we connect all of the scenarios with theirs proper children (paths)
"""
level01.set_options({
    "SEE": level02_see,
    "WAIT": level09_wait
})

level02_see.set_options({
    "FIGHT": level03_fight,
    "RUN": level06_run
})

level03_fight.set_options({
    "BOAT": level04_boat,
    "ATTACK": level05_attack
})

level06_run.set_options({
    "BACK": level07_back,
    "FOREST": level08_forest
})

level09_wait.set_options({
    "TALK": level10_talk,
    "SNEAK": level11_sneak,
    "QUIET": level12_quiet
})

level01.run()

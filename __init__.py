from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

import requests

# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

class CoffeeSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(CoffeeSkill, self).__init__(name="CoffeeSkill")
        
        self.log.info("Barista initalized.")
        # Initialize working variables used within the skill.
        self.arduino_ip = "192.168.2.251"
        # Requests timeout in seconds
        self.timeout = 3

    # The "handle_xxxx_intent" function is triggered by Mycroft when the
    # skill's intent is matched.  The intent is defined by the IntentBuilder()
    # pieces, and is triggered when the user's utterance matches the pattern
    # defined by the keywords.  In this case, the match occurs when one word
    # is found from each of the files:
    #    vocab/en-us/Hello.voc
    #    vocab/en-us/World.voc
    # In this example that means it would match on utterances like:
    #   'Hello world'
    #   'Howdy you great big world'
    #   'Greetings planet earth'
    @intent_handler(IntentBuilder("").require("Espresso"))
    def handle_espresso_intent(self, message):
        # In this case, respond by simply speaking a canned response.
        # Mycroft will randomly speak one of the lines from the dialog file
        self.speak_dialog("barista.espresso")
        try:
            # TODO: Fix turnOnAndMakeEspresso routine on Arduino
            r = requests.get(f"http://{self.arduino_ip}/routines/espresso",timeout=self.timeout)
            r.raise_for_status()
        except requests.exceptions.Timeout:
            self.speak_dialog("some.error", data={"error": "Arduino offline"})
        except:
            self.speak_dialog("some.error", data={"some.error": "Unknown"})


    @intent_handler(IntentBuilder("").require("DoubleEspresso"))
    def handle_double_espresso_intent(self, message):
        # In this case, respond by simply speaking a canned response.
        # Mycroft will randomly speak one of the lines from the dialog file
        self.speak_dialog("barista.double.espresso")
        try:
            # TODO: Fix turnOnAndMakeEspresso routine on Arduino
            r = requests.get(f"http://{self.arduino_ip}/routines/doubleEspresso",timeout=self.timeout)
            r.raise_for_status()
        except requests.exceptions.Timeout:
            self.speak_dialog("some.error", data={"error": "Arduino offline"})
        except:
            self.speak_dialog("some.error", data={"error": "Unknown"})

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return CoffeeSkill()

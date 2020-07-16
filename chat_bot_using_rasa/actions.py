# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from  data_acronym import data
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

timezones = {
    "AAA": "Authentication Authorisation and Accounting",
    "AAD" : "Application and Data Services",
    "AADC" : "Azure AD Connect",
    "AAO" : "Advanced Anti-virus Option"
    
}

class ActionFindAndShowTimeZone(Action):

    def name(self) -> Text:
        return "action_find_and_show_time_zone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.get_slot("city")
        #print(data)
        timezone = data.get(city)

        if timezone is None:
            output = "Could not find the acronym for {}".format(city)
        else:
            output = "The Acronym for {} is {}".format(city, timezone)

        dispatcher.utter_message(text=output)

        return []

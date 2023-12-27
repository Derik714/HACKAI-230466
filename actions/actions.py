
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from random import randint
import pymongo
import spacy
import openai
client = pymongo.MongoClient("mongodb://localhost:27017")
DB = client['User_complaints']
openai.api_key = "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"
class Actionname(Action):

    def name(self) -> Text:
        return "action_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message.get('entities', [])
        name = next((entity for entity in entities if entity['entity'] == 'name'), None)
        namevalue = str(name['value'])
        k = randint(0,3)
        if k==1:
            dispatcher.utter_message("Hey there, "+namevalue+"! What can I help you with")
        elif k==2:
            dispatcher.utter_message("Hello "+ namevalue+", let me know if I can be of any help")
        else:
            dispatcher.utter_message("Hi there, "+namevalue+"! I'm here if you need any help")

class ActionComplaint(Action):

    def name(self) -> Text:
        return "action_name2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message.get('entities', [])
        name = next((entity for entity in entities if entity['entity'] == 'name'), None)
        namevalue = str(name['value'])
        k = randint(0,3)
        if k==1:
            dispatcher.utter_message("Hey there, "+namevalue+"! Please tell me your order ID")
        elif k==2:
            dispatcher.utter_message("Hello "+ namevalue+", please let me know your order ID")
        else:
            dispatcher.utter_message("Hi there, "+namevalue+"! please let me know your order ID")
class sdbnddzsnsdjvs(Action):
    def name(self) -> Text:
        return "action_productdef"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        nlp = spacy.load("en_core_web_sm")
        entities = tracker.latest_message.get('entities', [])
        name = next((entity for entity in entities if entity['entity'] == 'shoes'), None)
        namevalue = str(name['value'])
        user_input = "Information about "+ namevalue + "shoes in brief be professional"
        response = openai.Completion.create(
            engine="text-davinci-003",  # GPT-3.5 engine
            prompt=user_input,
            max_tokens=80)
        fallback_response = response.choices[0].text.strip()

        dispatcher.utter_message(text=fallback_response)
class Availability(Action):
    def name(self) -> Text:
        return "action_productavail"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        nlp = spacy.load("en_core_web_sm")
        entities = tracker.latest_message.get('entities', [])
        coll3 = DB['Shoe_availability_pricing']
        name = next((entity for entity in entities if entity['entity'] == 'shoes'), None)
        namevalue = str(name['value'])
        namevalue = namevalue.lower()
        stock_count = 0
        if namevalue != None:
            stock_count = coll3.find_one({"name":namevalue})
        
        if stock_count != 0:
            dispatcher.utter_message("There are "+ str(stock_count["stock"])+ " units left in stock")
        else:
            dispatcher.utter_message("Sorry, it's out of stock for now")
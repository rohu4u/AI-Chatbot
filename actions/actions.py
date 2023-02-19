# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime as dt

class ActionCurrentTime(Action):

     def name(self) -> Text:
         return "action_current_time"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
     	time = str(dt.now().time())
     	dispatcher.utter_message(text="Time : {}".format(time))
     	return []

class ActionStudyMaterial(Action):

     def name(self) -> Text:
         return "action_study_material"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        
        for entity in entities:
            if entity['entity']=="subject":
                subject = entity["value"]

            if entity['entity']=="material_type":
                material_type = entity['value']


        if subject =="python":
            if material_type=="interview":
                dispatcher.utter_message(text="https://www.interviewbit.com/python-interview-questions/")

            if material_type=="tutorial":
                dispatcher.utter_message(text="https://www.interviewbit.com/python-interview-questions/")

        if subject =="java":
            if material_type=="interview":
                dispatcher.utter_message(text="https://www.interviewbit.com/java-interview-questions/")

            if material_type=="tutorial":
                dispatcher.utter_message(text="https://www.interviewbit.com/java-interview-questions/")


        
        return []
from typing import Dict, Text, Any, List, Union, Optional

import os
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
import json
import requests


class ApiForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "api_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["table", "num_entries"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "table": self.from_entity(entity="table", not_intent="chitchat"),
            "num_entries": [self.from_entity(entity="num_entries", intent=["inform", "request_api"]), self.from_entity(entity="number"),],
        }

    # USED FOR DOCS: do not rename without updating in docs
    @staticmethod
    def table_db() -> List[Text]:
        """Database of supported API"""

        return ["experiments"]

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""

        try:
            int(string)
            return True
        except ValueError:
            return False

    # USED FOR DOCS: do not rename without updating in docs
    def validate_table(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> Dict[Text, Any]:
        """Validate table value."""

        if value.lower() in self.table_db():
            # validation succeeded, set the value of the "table" slot to value
            return {"table": value}
        else:
            dispatcher.utter_message(template="utter_wrong_table")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"table": None}

    def validate_num_entries(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> Dict[Text, Any]:
        """Validate num_entries value."""

        if self.is_int(value) and int(value) > 0:
            return {"num_entries": value}
        else:
            dispatcher.utter_message(template="utter_wrong_num_entries")
            # validation failed, set slot to None
            return {"num_entries": None}

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        print(tracker.get_slot("table"))
        print(tracker.get_slot("num_entries"))
        lgbsttracker_uri = os.getenv("LGBSTTRACKER_API_URI")
        res = requests.get(f"{lgbsttracker_uri}/api/v1/{tracker.get_slot('table')}")
        # utter submit template
        dispatcher.utter_message(str(json.loads(res.text)[0]))  # template="utter_submit")
        return []

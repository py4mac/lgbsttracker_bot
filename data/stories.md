## happy path
* greet
    - utter_greet
* request_api
    - api_form
    - form{"name": "api_form"}
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## unhappy path
* greet
    - utter_greet
* request_api
    - api_form
    - form{"name": "api_form"}
* chitchat
    - utter_chitchat
    - api_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## very unhappy path
* greet
    - utter_greet
* request_api
    - api_form
    - form{"name": "api_form"}
* chitchat
    - utter_chitchat
    - api_form
* chitchat
    - utter_chitchat
    - api_form
* chitchat
    - utter_chitchat
    - api_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## stop but continue path
* greet
    - utter_greet
* request_api
    - api_form
    - form{"name": "api_form"}
* stop
    - utter_ask_continue
* affirm
    - api_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## stop and really stop path
* greet
    - utter_greet
* request_api
    - api_form
    - form{"name": "api_form"}
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}

## chitchat stop but continue path
* request_api
    - api_form
    - form{"name": "api_form"}
* chitchat
    - utter_chitchat
    - api_form
* stop
    - utter_ask_continue
* affirm
    - api_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## stop but continue and chitchat path
* greet
    - utter_greet
* request_api
    - api_form
    - form{"name": "api_form"}
* stop
    - utter_ask_continue
* affirm
    - api_form
* chitchat
    - utter_chitchat
    - api_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## chitchat stop but continue and chitchat path
* greet
    - utter_greet
* request_api
    - api_form
    - form{"name": "api_form"}
* chitchat
    - utter_chitchat
    - api_form
* stop
    - utter_ask_continue
* affirm
    - api_form
* chitchat
    - utter_chitchat
    - api_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## chitchat, stop and really stop path
* greet
    - utter_greet
* request_api
    - api_form
    - form{"name": "api_form"}
* chitchat
    - utter_chitchat
    - api_form
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}

## bot challenge
* bot_challenge
  - utter_iamabot
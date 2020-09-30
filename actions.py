from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormAction

import requests
from random import choice


ENDPOINTS = {
    "base": "proyectos.json",
    "enlace": "https://gist.githubusercontent.com/rndae/47627f3ee864e3eda969f31bec008772/raw/833216812f1517819daf4be2abfe43da22231ff9/projectos.json"
}

AREAS = ["Matemáticas", "Química", "Física", "Biología",
         "Lenguaje", "Artes Plásticas", "Psicología", "Música",
          "Filosofía", "Ciencias Sociales", "Historia",
          "Educación Cívica", "Inglés", "Ciencias Naturales",
          "Geografía", "Deporte", "Educación Física", "Religión",
          "Quechua", "Computación", "Técnica Vocacional"]

def _load_json_r(path):
  r = requests.get(path)
  return r.json()
  
def _opti_leven_distance(a, b):
  dists = [ [0 for _ in range(len(b)+1)] for _ in range(len(a)+1) ]

  for i in range(1, len(a)+1):
      dists[i][0] = i
  for j in range(1, len(b)+1):
      dists[0][j] = j

  for i in range(1, len(a)+1):
      for j in range(1, len(b)+1):
          if a[i-1] == b[j-1]:
              cost = 0
          else:
              cost = 1

          dists[i][j] = min(
              dists[i-1][j] + 1,
              dists[i][j-1] + 1,
              dists[i-1][j-1] + cost
          )

  return dists[-1][-1]
  
def _most_similar_word(word_input, words):
  least = _opti_leven_distance(word_input, words[0])
  best_match = words[0]
  for word in words:
      dist = _opti_leven_distance(word_input, word)
      if least > dist:
        least = dist
        best_match = word
  return best_match 

class ActionProjectSearch(Action):
    """This action class retrieves the name of the area the user is interested in."""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "action_project_search"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:
        
        area_slot = tracker.get_slot("area")
        area = _most_similar_word(area_slot, AREAS)
        previous_project = tracker.get_slot("project")
        full_path = ENDPOINTS["enlace"]
        projects_json = _load_json_r(full_path)
        results = [project for project in projects_json if area in project["area"]]
        if results:
            selected = choice(results)
            while len(results) > 1 and selected["titulo"] == previous_project:
              selected = choice(results)
            project_name = "{}".format(selected["titulo"].title())
                
            return [SlotSet("project", project_name), SlotSet("area", area)]
        else:
            print("Most likely this action was executed "
                  "before the user choose an area."
                  "If this is a common problem in the dialogue flow, "
                  "using a form instead for this action might be appropriate.")

            return [SlotSet("project", "--?--"), SlotSet("area", area)]
        
